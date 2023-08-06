from autoxx.agent.base import BaseAgent
from typing import List, Dict
from autoxx.search.simple_search import simple_search
from autogpt.llm_utils import create_chat_completion
from autogpt.config import Config

CFG = Config()

class ResearchAgent(BaseAgent):  
  
    def execute(self, objective:str, task: str) -> str:  
        return simple_search(task)
  
    def post_process(self, objective:str, task_results:List[Dict]) -> str:  
        task_context = [f"Task({task['task']}): {task['result']}" for task in task_results]
        nl = '\n'
        prompt = (
            f"Given the context {nl.join(task_context) } and objective: {objective}. "
            "Create a research report. "
        )
        messages = [
            {
                "role": "system",
                "content": "You are a research AI."
            },
            {
                "role": "user",
                "content": prompt,
            }
        ]
        return create_chat_completion(
            model=CFG.fast_llm_model,
            messages=messages,
        )
