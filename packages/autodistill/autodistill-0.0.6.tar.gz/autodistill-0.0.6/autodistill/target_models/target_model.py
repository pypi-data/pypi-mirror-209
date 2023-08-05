import json
from abc import ABC, abstractmethod


class TargetModel(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def train(self):
        pass
