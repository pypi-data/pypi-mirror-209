import json
from collections import deque
from typing import Dict, List, Dict, Optional

from autogpt.llm_utils import create_chat_completion
from autogpt.config import Config

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

def task_creation_agent(objective: str, task: Dict, task_list: List[str], allowed_new_task: Optional[int] = 1):
    prompt = (
        f"You are a task management AI that uses the result of the last to create new tasks with the following objective: {objective}.\n"
        f"The last completed task has the result: {task['result']}. "
        f"This result was based on this task description: {task['task']}. "
        f"These are incomplete tasks: {', '.join(task_list)}. "
        f"Based on the result, create new tasks to be completed by the AI system that do not overlap with incomplete tasks. Up to {allowed_new_task} new tasks can be created.\n"
        "You should only respond in JSON format as described below \n"
        f"Response Format: \n{response_format} \nEnsure the response can be parsed by Python json.loads"
    )

    messages = create_message(prompt)
    response = create_chat_completion(
        model=Config().fast_llm_model,
        messages=messages,
    )

    new_tasks = json.loads(response)
    return [{"task": task["task"]} for task in new_tasks]

def prioritization_agent(this_task_id:int, objective:str, task_list:deque) -> deque:
    task_descriptions = [t["task"] for t in task_list]
    next_task_id = int(this_task_id)+1
    prompt = (
        f"You are a task prioritization AI tasked with cleaning the formatting of and reprioritizing the following tasks: {task_descriptions}. "
        f"Consider the ultimate objective of your team: {objective}. \n"
        "Tasks should be sorted from highest to lowest priority.\n"
        "Higher-priority tasks are those that act as pre-requisites or are more essential for meeting the objective.\n"
        f"Do not remove any tasks and don't add any new tasks. Return the result as a numbered list, like:\n"
        "#. First task\n"
        "#. Second task\n"
        f"Start the task list with number {next_task_id}."
    )

    messages = create_message(prompt)
    response = create_chat_completion(
        model=Config().fast_llm_model,
        messages=messages,
    )

    new_tasks = response.split('\n')
    task_list = []
    for task_string in new_tasks:
        task_parts = task_string.strip().split(".", 1)
        if len(task_parts) == 2:
            task_id = task_parts[0].strip()
            task_description = task_parts[1].strip()
            task_list.append({"id": task_id, "task": task_description})
    return task_list

def init_task_list(objective: str, max_tasks_count: Optional[int] = 4) -> List[Dict]:
    task_id_counter = 0
    prompt = (
        f"You are a task management AI tasked with creating tasks for the following objective: {objective}.\n"
        f"Up to {max_tasks_count - 1} new tasks can be created to complete this objective. "
        "You should only respond in JSON format as described below \n"
        f"Response Format: \n{response_format} \nEnsure the response can be parsed by Python json.loads"
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
        new_task.update({"task_id": task_id_counter})
        task_list.append(new_task)
    return task_list
