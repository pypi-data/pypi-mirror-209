import json, time
from typing import Dict, List, Dict, Optional
import logging

from autogpt.llm_utils import create_chat_completion
from autogpt.config import Config

from autoxx.tools.web_search.search import web_search
from autoxx.tools.llm.utils import llm_uils, create_message


class AGIExecutor:
    def __init__(self, objective:str, max_tasks_count: Optional[int] = 5):
        if objective is None or len(objective) <= 1:  
            raise ValueError("Must provide an objective")  

        self.objective = objective
        self.max_tasks_count = max_tasks_count

        self.task_list = self.init_task_list(objective)
        self.status = "initizing"
        self.error_message = None
        self.final_answer = None

    def get_task_by_id(self, task_id: int):
        for task in self.task_list:
            if task["id"] == task_id:
                return task
        return None

    def init_task_list(self, objective: str) -> List[Dict]:
        task_id_counter = 0
        prompt = (
            f"You are a QA AI tasked with creating tasks for the following objective: {objective}.\n"
            f"Create new tasks based on the following plan delimited by triple backtick if necessary for the objective. Limit tasks types to those that can be completed with the available tools listed below. Task description should be detailed. "
            f"The plan:```decelop a task list```.\n"
            f"The current tool option is [text-completion, web-search] only. What each tool does is as follows:\n"
            f"web-search: It supports only searching for information from the Internet. For tasks using [web-search], provide the search query, and only the search query to use (eg. not 'research waterproof shoes, but 'waterproof shoes').\n"
            f"text-completion: it is a text completion tool that can be used for content extraction, summarization, copywrite, translation, etc., and can also be used for LLM-based QA\n"
            f"Make sure all task IDs are in chronological order.\n"
            f"For efficiency, let's think step by step and create the tasks (up to 3 tasks) that are most critical to objective.\n"
            f"An example of the desired output format is:"
            "[{\"id\": 1, \"task\": \"https://untapped.vc\", \"tool\": \"web-scrape\", \"dependent_task_ids\": [], \"status\": \"incomplete\", \"result\": null, \"result_summary\": null}, {\"id\": 2, \"task\": \"Consider additional insights that can be reasoned from the results of...\", \"tool\": \"text-completion\", \"dependent_task_ids\": [1], \"status\": \"incomplete\", \"result\": null, \"result_summary\": null}, {\"id\": 3, \"task\": \"Untapped Capital\", \"tool\": \"web-search\", \"dependent_task_ids\": [], \"status\": \"incomplete\", \"result\": null, \"result_summary\": null}].\n"
            f"Ensure the response can be parsed by Python json.loads. JSON TASK LIST="
        )

        messages = create_message(prompt)
        response = create_chat_completion(
            model=Config().fast_llm_model,
            messages=messages,
        )

        new_tasks = json.loads(response)
        task_list = []
        for new_task in new_tasks:
            task_id_counter += 1
            new_task.update({"id": task_id_counter})
            task_list.append(new_task)
        return task_list

    def orchestrate_task(self, last_task: Dict) -> List[Dict]:
        original_task_list = self.task_list.copy()
        minified_task_list = [{k: v for k, v in task.items() if k != "result"} for task in self.task_list]
        result = last_task['result'][0:4000] #come up with better solution later.
        
        prompt = (
            f"You are a QA AI assistant tasked with cleaning the formatting of and reprioritizing the following tasks delimited by triple backtick:```{minified_task_list}```\n"
            f"the last completed task (task id = {last_task['id']}, tool = {last_task['tool']}) has the following result delimited by triple backtick: ```{last_task['result']}```\n\n"
            f"Your task: Consider the ultimate objective of your team is to answer the question {self.objective} and reflect on the result of task that has been complted, re-create the task list (up to 5 tasks) to answer the question.\n" 
            f"The current tool option is [text-completion, web-search] only. What each tool does is as follows:\n"
            f"web-search: It supports searching for information on the Internet. For tasks using [web-search], provide the search query, and only the search query to use (eg. not 'research waterproof shoes, but 'waterproof shoes').\n"
            f"text-completion: IT is a tool that can be used for content extraction, summarization, copywrite, translation, etc., and can also be used for LLM-based QA\n"
            f"dependent_task_ids should always be an empty array, or an array of numbers representing the task ID it should pull results from."
            f"Make sure all task IDs are in chronological order.\n"
            f"Don not remove the completed tasks.\n"
            f"The last task is always to provide a final answer for customer.\n"
            f"An example of the desired output format is:"
            "[{\"id\": 1, \"task\": \"https://untapped.vc\", \"tool\": \"web-scrape\", \"dependent_task_ids\": [], \"status\": \"incomplete\", \"result\": null, \"result_summary\": null}, {\"id\": 2, \"task\": \"Consider additional insights that can be reasoned from the results of...\", \"tool\": \"text-completion\", \"dependent_task_ids\": [1], \"status\": \"incomplete\", \"result\": null, \"result_summary\": null}, {\"id\": 3, \"task\": \"Untapped Capital\", \"tool\": \"web-search\", \"dependent_task_ids\": [], \"status\": \"incomplete\", \"result\": null, \"result_summary\": null}].\n"
            f"Ensure the response can be parsed by Python json.loads. JSON TASK LIST="
        )

        messages = create_message(prompt)
        result = create_chat_completion(
            model=Config().fast_llm_model,
            messages=messages,
        )

        try:
            tmp_task_list = json.loads(result)
        except Exception as error:
            print(f"fail to decode ({error}): {result}")
            return original_task_list
        # Add the 'result' field back in

        for updated_task, original_task in zip(tmp_task_list, original_task_list):
            if "result" in original_task:
                updated_task["result"] = original_task["result"]

        return tmp_task_list

    ### Agent functions ##############################
    def execute_task(self, task: Dict) -> Dict:
        # Check if dependent_task_id is completed
        dependent_task_ids = []
        dependent_task_prompt = ""
        if task["dependent_task_ids"]:
            if isinstance(task["dependent_task_ids"], list):
                dependent_task_ids = task["dependent_task_ids"]
            else:
                dependent_task_ids = [task["dependent_task_ids"]]

            for dependent_task_id in dependent_task_ids:
                dependent_task = self.get_task_by_id(dependent_task_id)
                if dependent_task and dependent_task["status"] != "completed":
                    return
                elif dependent_task:
                    dependent_task_prompt += f"\ntask ({dependent_task['id']}. {dependent_task['task']}) result: {dependent_task['result']}"

        # Execute task
        
        task_prompt = f"Complete your assigned task based on the objective: {self.objective}. Your task: {task['task']}"
        if dependent_task_prompt != "":
            task_prompt += f"\nThe previous tasks: {dependent_task_prompt}"

        task_prompt += "\nResponse:"
        if task["tool"] == "text-completion":
            result = llm_uils().text_completion(task_prompt)
            summary_result_prompt = f"Please summarize the following text:\n{result}\nSummary:"
            task["result_summary"] = llm_uils().text_completion(summary_result_prompt)
        elif task["tool"] == "web-search":
            result = str(web_search(str(task['task'])))
            summary_result_prompt = f"Please summarize the following text:\n{result}\nSummary:"
            task["result_summary"] = llm_uils().text_completion(summary_result_prompt)
        elif task["tool"] == "search-IT-knowledge-base":
            result = str(self.it_kb.similarity_search(str(task['task'])))
            summary_result_prompt = f"Please summarize the following text:\n{result}\nSummary:"
            task["result_summary"] = llm_uils().text_completion(summary_result_prompt)
        else:
            result = "Unknown tool"
        
        # Update task status and result
        task["status"] = "completed"
        task["result"] = result
        return task
    
    def execute(self) -> str:
        self.status = "running"
        # Main loop
        while any(task["status"] == "incomplete" for task in self.task_list):
              # Filter out incomplete tasks
            incomplete_tasks = [task for task in self.task_list if task["status"] == "incomplete"]
            logging.info(f"\033[95m\033[1m INCOMPLETE TASK LIST({self.objective}) \033[0m\033[0m {[str(t['id'])+': '+t['task'] + '[' + t['tool'] + ']' for t in incomplete_tasks]}")
            if incomplete_tasks:
                # Sort tasks by ID
                incomplete_tasks.sort(key=lambda x: x["id"])

                # Pull the first task
                task = incomplete_tasks[0]
                logging.info(f"\033[92m\033[1m NEXT TASK({self.objective}) \033[0m\033[0m {task['id']}:{task['task']}[{task['tool']}]")

                # Execute task & call task manager from function
                try:
                    completed_task = self.execute_task(task)
                    logging.info(f"\033[93m\033[1m TASK RESULT({self.objective}) \033[0m\033[0m {completed_task['result']}")
                except Exception as e:  
                    logging.error(f"An error occurred while executing the task({self.objective}): {e.with_traceback()}")
                    self.status = "error"
                    self.error_message = str(e)  
                    return str(e)
                if len(self.task_list) - len(incomplete_tasks) + 1 < self.max_tasks_count or len(incomplete_tasks) > 1:
                    logging.info(f"\033[90m\033[3m" + "\nOrchestrate_task list({self.objective})...\n" + "\033[0m")
                    self.task_list = self.orchestrate_task(completed_task)

            time.sleep(1)  # Sleep before checking the task list again
        self.status = "completed"

    def stat(self) -> Dict:
        return {"task_list": self.task_list, "status": self.status, "error_message": self.error_message}