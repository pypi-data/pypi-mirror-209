import json, time
from typing import Dict, List, Dict

from autogpt.llm_utils import create_chat_completion
from autogpt.config import Config
from autoxx.search.simple_search import browse_website
from autogpt.commands.google_search import google_search

response_format = """[
    {
        "id": 1,
        "task": "task description",
        "tool": "tool used to complete task"
    },
    {
        "id": 2,
        "task": "task description",
        "tool": "tool used to complete task"
    }
]"""

def create_message(prompt: str) -> List[Dict]:
    """Create a message for the chat completion

    Args:
        chunk (str): The chunk of text to summarize
        question (str): The question to answer

    Returns:
        Dict[str, str]: The message to send to the chat completion
    """
    return [
        {
            "role": "system",
            "content": "You are a task manager AI."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

# Initialize task list
task_list = []

# Initialize session_summary
session_summary = ""

### Task list functions ##############################

def get_task_by_id(task_id: int):
    for task in task_list:
        if task["id"] == task_id:
            return task
    return None

def get_completed_tasks():
    return [task for task in task_list if task["status"] == "completed"]

def init_task_list(objective: str) -> List[Dict]:
    create_task_prompt = f"Complete your assigned task based on the objective: {objective}. Your task: develop a task list to complete the objective. \n Response:"
    messages = create_message(create_task_prompt)
    create_task_response = create_chat_completion(
        model=Config().fast_llm_model,
        messages=messages,
    )

    task_id_counter = 0
    prompt = (
        f"You are a task management AI tasked with creating tasks for the following objective: {objective}.\n"
        f"Create new tasks based on the following plan delimited by triple backtick if necessary for the objective. Limit tasks types to those that can be completed with the available tools listed below. Task description should be detailed. "
        f"The plan:```{create_task_response}```.\n"
        f"The current tool option is [text-completion, google-search, web-scrape] only. "
        f"For tasks using [web-scrape], provide only the URL to scrape as the task description. Do not provide placeholder URLs, but use ones provided by a search step or the initial objective. "
        f"For tasks using [web-scrape], do not select url under these domains [g2.com]. "
        f"For tasks using [google-search], provide the search query, and only the search query to use (eg. not 'research waterproof shoes, but 'waterproof shoes').\n"
        f"Make sure all task IDs are in chronological order.\n"
        f"Do not provide example URLs for [web-scrape].\n"
        f"Do not include the result from the last task in the JSON, that will be added after..\n"
        f"For efficiency, let's think step by step and create the tasks (up to 5 tasks) that are most critical to objective. The last task is always to provide a final summary report of all tasks.\n"
        f"An example of the desired output format is: "
        "[{\"id\": 1, \"task\": \"https://untapped.vc\", \"tool\": \"web-scrape\", \"dependent_task_id\": null, \"status\": \"incomplete\", \"result\": null, \"result_summary\": null}, {\"id\": 2, \"task\": \"Analyze the contents of...\", \"tool\": \"text-completion\", \"dependent_task_id\": 1, \"status\": \"incomplete\", \"result\": null, \"result_summary\": null}, {\"id\": 3, \"task\": \"Untapped Capital\", \"tool\": \"google-search\", \"dependent_task_id\": [1,2], \"status\": \"incomplete\", \"result\": null, \"result_summary\": null}]."
        f"\nEnsure the response can be parsed by Python json.loads\n"
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

def task_manager_agent(objective: str, task: Dict, result: str) -> List[Dict]:
    global task_list
    original_task_list = task_list.copy()
    minified_task_list = [{k: v for k, v in task.items() if k != "result"} for task in task_list]
    result = result[0:4000] #come up with better solution later.
    
    prompt = (
        f"You are a task management AI tasked with cleaning the formatting of and reprioritizing the following tasks delimited by triple backtick:```{minified_task_list}```\n"
        f"the last completed task (task id = {task['id']}, tool = {task['tool']}) has the following result delimited by triple backtick: ```{result}```\n\n"
        f"Your task: Consider the ultimate objective of your team: {objective} and the completed tasks, re-create the task list (up to 8 tasks) to make it better to complete the objective. Don not remove the completed tasks.\n" 
        f"The current tool option is [text-completion, google-search, web-scrape] only. "
        f"If a [google-search] task is completed, create one or two necessary [web-scrape] tasks to get objective related documents will always be useful.\n"
        f"For tasks using [web-scrape], provide only the URL to scrape as the task description. Do not provide placeholder URLs, but use ones provided by a search step or the initial objective. "
        f"For tasks using [web-scrape], do not select url under these domains [g2.com], do not provide example URLs"
        f"For tasks using [google-search], provide the search query, and only the search query to use (eg. not 'research waterproof shoes, but 'waterproof shoes'). "
        f"The dependent_task_id should always be null or a number or a number list.\n"
        f"Make sure all task IDs are in chronological order.\n"
        f"Don not remove the completed tasks.\n"
        f"Do not include the result from the last task in the JSON, that will be added after..\n"
        f"The last task is always to provide a final summary report of all tasks.\n"
        f"An example of the desired output format is: "
        "[{\"id\": 1, \"task\": \"https://untapped.vc\", \"tool\": \"web-scrape\", \"dependent_task_id\": null, \"status\": \"incomplete\", \"result_summary\": null}, {\"id\": 2, \"task\": \"Analyze the contents of...\", \"tool\": \"text-completion\", \"dependent_task_id\": 1, \"status\": \"incomplete\", \"result_summary\": null}, {\"id\": 3, \"task\": \"Untapped Capital\", \"tool\": \"google-search\", \"dependent_task_id\": [1,2], \"status\": \"incomplete\", \"result_summary\": null}]."
        f"\nEnsure the response can be parsed by Python json.loads\n"
    )
    print("\033[90m\033[3m" + "\nRunning task manager agent...\n" + "\033[0m")

    messages = create_message(prompt)
    result = create_chat_completion(
        model=Config().fast_llm_model,
        messages=messages,
    )

    print("\033[90m\033[3m" + "\nDone!\n" + "\033[0m")
    try:
      task_list = json.loads(result)
    except Exception as error:
      print(error)
    # Add the 'result' field back in

    for updated_task, original_task in zip(task_list, original_task_list):
        if "result" in original_task:
            updated_task["result"] = original_task["result"]

    return task_list

def LLM_agent(prompt: str) -> str:
    messages = create_message(prompt)
    response = create_chat_completion(
        model=Config().fast_llm_model,
        messages=messages,
    )

    return response

def overview_agent(task: Dict) -> str:
    global session_summary

    completed_tasks = get_completed_tasks()
    completed_tasks_text = "\n".join(
        [f"{task['id']}. {task['task']} - {task['result_summary']}" for task in completed_tasks]
    )

    prompt = (
        f"Here is the current session summary delimited by triple backtick: \n```{session_summary}```\n"
        f"The last completed task is task {task['task']} using tools {task['tool']}. Please update the session summary with the information of the last task:\n{completed_tasks_text}\n"
        f"For tasks using [google-search], keeps all links to the search results. And don't discard related links in updating\n"
        f"Updated session summary, which should describe all tasks in chronological order:"
    )
    messages = create_message(prompt)
    response = create_chat_completion(
        model=Config().fast_llm_model,
        messages=messages,
    )
    session_summary = response
    return session_summary

def web_browse_tool(url:str, dependent_task_ids: List, objective: str)-> str:
    question = f"Extract relevant information from this article that is useful for objective: {objective}..."

    dependent_task_description = []
    for dependent_task_id in dependent_task_ids:
        dependent_task = get_task_by_id(dependent_task_id)
        if dependent_task and dependent_task["tool"] == "google-search":
            dependent_task_description.append(dependent_task["task"])


    if len(dependent_task_description) > 0:
        question += f" and questions:[{', '.join(dependent_task_description)}]"

    print(f"web_browse_tool {url} {question}\n")

    result = '\n'.join(browse_website(url, question))
    return result

### Agent functions ##############################
def execute_task(task: Dict, objective: str):
    global task_list
    # Check if dependent_task_id is completed
    dependent_task_ids = []
    dependent_task_prompt = ""
    if task["dependent_task_id"]:
        if isinstance(task["dependent_task_id"], list):
            dependent_task_ids = task["dependent_task_id"]
        else:
            dependent_task_ids = [task["dependent_task_id"]]

        for dependent_task_id in dependent_task_ids:
            dependent_task = get_task_by_id(dependent_task_id)
            if dependent_task and dependent_task["status"] != "completed":
                return
            elif dependent_task:
                dependent_task_prompt += f"\ntask ({dependent_task['id']}. {dependent_task['task']}) result: {dependent_task['result']}"

    # Execute task
    
    print("\033[92m\033[1m"+"\n*****NEXT TASK*****\n"+"\033[0m\033[0m")
    print(str(task['id'])+": "+str(task['task'])+" ["+str(task['tool']+"]"))
    task_prompt = f"Complete your assigned task based on the objective: {objective}. Your task: {task['task']}"
    if dependent_task_prompt != "":
        task_prompt += f"\nThe previous tasks: {dependent_task_prompt}"

    task_prompt += "\nResponse:"
    if task["tool"] == "text-completion":
        result = LLM_agent(task_prompt)
        summary_result_prompt = f"Please summarize the following text:\n{result}\nSummary:"
        task["result_summary"] = LLM_agent(summary_result_prompt)
    elif task["tool"] == "google-search":
        result = google_search(str(task['task']))
        summary_result_prompt = f"Please summarize the following google search result and keep all links:\n{result}\nSummary:"
        task["result_summary"] = LLM_agent(summary_result_prompt)
    elif task["tool"] == "web-scrape":
        result = web_browse_tool(str(task['task']), dependent_task_ids, objective)
        summary_result_prompt = f"Please summarize the following text:\n{result}\nSummary:"
        task["result_summary"] = LLM_agent(summary_result_prompt)
    else:
        result = "Unknown tool"
    
    print("\033[93m\033[1m"+"\n*****TASK RESULT*****\n"+"\033[0m\033[0m")
    print_result = result[0:2000]
    if result != result[0:2000]:
      print(print_result+"...")
    else:
      print(result)
    print("\033[93m\033[1m"+"\n*****TASK RESULT Summary *****\n"+"\033[0m\033[0m")
    print(task["result_summary"])
    # Update task status and result
    task["status"] = "completed"
    task["result"] = result

    # overview_agent(task)

    # Update task_manager_agent of tasks
    task_manager_agent(
        objective,
        task,
        result, 
    )

def execute(objective: str):
    global task_list
    task_list = init_task_list(objective)
    print("\033[95m\033[1m"+"\n*****TASK LIST*****\n"+"\033[0m")
    for t in task_list:
            dependent_task = ""
            if t['dependent_task_id'] is not None:
                dependent_task = f"\033[31m<dependency: #{t['dependent_task_id']}>\033[0m"
            status_color = "\033[32m" if t['status'] == "completd" else "\033[31m"
            print(f"\033[1m{t['id']}\033[0m: {t['task']} {status_color}[{t['status']}]\033[0m \033[93m[{t['tool']}] {dependent_task}\033[0m")


    # Continue the loop while there are incomplete tasks
    while any(task["status"] == "incomplete" for task in task_list):

        # Filter out incomplete tasks
        incomplete_tasks = [task for task in task_list if task["status"] == "incomplete"]

        if incomplete_tasks:
            # Sort tasks by ID
            incomplete_tasks.sort(key=lambda x: x["id"])

            # Pull the first task
            task = incomplete_tasks[0]

            # Execute task & call task manager from function
            execute_task(task, objective)

            # Print task list and session summary
            print("\033[95m\033[1m" + "\n*****TASK LIST*****\n" + "\033[0m")
            for t in task_list:
                dependent_task = ""
                if t['dependent_task_id'] is not None:
                    dependent_task = f"\033[31m<dependency: #{t['dependent_task_id']}>\033[0m"
                status_color = "\033[32m" if t['status'] == "completed" else "\033[31m"
                print(f"\033[1m{t['id']}\033[0m: {t['task']} {status_color}[{t['status']}]\033[0m \033[93m[{t['tool']}] {dependent_task}\033[0m")
            #print("\033[93m\033[1m" + "\n*****SESSION SUMMARY*****\n" + "\033[0m\033[0m")
            #print(session_summary)

        time.sleep(1)  # Sleep before checking the task list again

    ### Objective complete ##############################

    # Print the full task list if there are no incomplete tasks
    if all(task["status"] != "incomplete" for task in task_list):
        print("\033[92m\033[1m" + "\n*****ALL TASKS COMPLETED*****\n" + "\033[0m\033[0m")
        for task in task_list:
            print(f"ID: {task['id']}, Task: {task['task']}, Result: {task['result']}")