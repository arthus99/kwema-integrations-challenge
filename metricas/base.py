# metricas/base.py

from abc import ABC, abstractmethod
from typing import Dict

# Define the Metric interface
class Metric(ABC):
    @abstractmethod
    async def calculate(self, username: str) -> Dict:
        pass
