import json
from abc import ABC, abstractmethod


class BaseModel(ABC):
    def __init__(self, ontology=None):
        self.ontology = self.create_ontology(ontology)

    @abstractmethod
    def create_ontology(self):
        return None

    def set_ontology(self, ontology):
        self.ontology = self.create_ontology(ontology)

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def label(self):
        pass
