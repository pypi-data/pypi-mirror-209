from abc import ABC, abstractmethod  
from typing import List, Dict
  
class BaseAgent(ABC):  
  
    @abstractmethod  
    def execute(self, objective:str, task: str) -> str:  
        pass  
  
    @abstractmethod  
    def post_process(self, objective:str, task_results:List[Dict]) -> str:  
        pass  
