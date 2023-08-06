import logging, time, threading
from typing import Dict, Optional
from autoxx.agent.base import BaseAgent
from autoxx.agent.researcher import ResearchAgent
from autoxx.agi import init_task_list, task_creation_agent, prioritization_agent

class Task:
    def __init__(self, agent:BaseAgent, objective:str, max_tasks_count: Optional[int] = 3):
        if objective is None or len(objective) <= 1:  
            raise ValueError("Must provide an objective")  
        if agent is None:  
            raise ValueError("Must provide an agent")

        self.agent = agent
        self.objective = objective
        self.max_tasks_count = max_tasks_count

        self.task_list = init_task_list(objective, max_tasks_count)
        self.task_cur = 0
        self.status = "initizing"
        self.error_message = None
        self.final_answer = None

    def execute(self) -> str:
        self.status = "running"
        # Main loop
        while self.task_cur < len(self.task_list):
            # Print the task list
            incomplete_list = [self.task_list[i]  for i in range(self.task_cur, len(self.task_list))]
            logging.info(f"\033[95m\033[1m INCOMPLETE TASK LIST({self.objective}) \033[0m\033[0m {[str(t['id'])+': '+t['task'] for t in incomplete_list]}")

            # Step 1: Pull the first task
            task = incomplete_list[0]
            logging.info(f"\033[92m\033[1m NEXT TASK({self.objective}) \033[0m\033[0m" + str(task['id'])+": "+task['task'])

            try:
                # Send to execution function to complete the task based on the context
                result = self.agent.execute(self.objective, task["task"])
                this_task_id = int(task["id"])
                logging.info(f"\033[93m\033[1m TASK RESULT({self.objective}) \033[0m\033[0m {result}")
            except Exception as e:  
                logging.error(f"An error occurred while executing the task({self.objective}): {e}")
                self.status = "error"
                self.error_message = str(e)  
                return str(e)
                # You can also handle specific exceptions if needed, e.g., KeyError, ValueError, etc.  
                # To do this, add additional except blocks for each specific exception type.  

            task["result"] = result
            self.task_cur += 1

            # Step 2: Create new tasks
            task_id_counter = len(self.task_list)
            if self.max_tasks_count-task_id_counter > 0:
                new_tasks = task_creation_agent(self.objective,  task, [t["task"]  for t in self.task_list[self.task_cur:]], self.max_tasks_count-task_id_counter)

                for new_task in new_tasks:
                    task_id_counter += 1
                    new_task.update({"id": task_id_counter})
                    self.task_list.append(new_task)

                incomplete_list = incomplete_list[1:]
                # Step 3: Reprioritize task list
                if len(self.task_list)-self.task_cur > 1:
                    reprioritized_tasks = prioritization_agent(this_task_id, self.objective, self.task_list[self.task_cur:])
                    self.task_list = self.task_list[:self.task_cur] + reprioritized_tasks

            if self.task_cur >= self.max_tasks_count:
                final_result = self.agent.post_process(self.objective, self.task_list)
                self.final_answer = final_result
                self.status = "finished"
                return final_result
            time.sleep(1)  # Sleep before checking the task list again

    def stat(self) -> Dict:
        current = self.task_cur
        if current >= len(self.task_list):
            current -= 1
        return {"current_task": self.task_list[current]["id"], "task_list": self.task_list, "final_answer": self.final_answer, "status": self.status, "error_message": self.error_message}
  
class TaskManager:  
    def __init__(self):  
        self.tasks = {}  
  
    def create_task(self, objective: str, max_tasks_count: Optional[int] = 3):  
        if objective in self.tasks:
            if self.tasks[objective].status == "error":
                task = self.tasks[objective]
                task_thread = threading.Thread(target=task.execute)  
                task_thread.start()
                return
            else:
                raise ValueError(f"Task found with objective: {objective}")
        
        agent = ResearchAgent()  # Use the default ResearchAgent  
        task = Task(agent, objective, max_tasks_count) 
        self.tasks[objective] = task  
  
        # Start task execution in a separate thread  
        task_thread = threading.Thread(target=task.execute)  
        task_thread.start()
  
    def get_task_stat(self, objective: str) -> Dict:  
        if objective not in self.tasks:  
            raise ValueError(f"No task found with objective: {objective}")  
  
        return self.tasks[objective].stat()