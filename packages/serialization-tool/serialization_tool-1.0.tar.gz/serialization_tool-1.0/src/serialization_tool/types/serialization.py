from abc import ABC, abstractmethod
from serialization_tool.serialization.serializer import Serializer

class Serialization(ABC):
    def __init__(self):
        self.serializer = Serializer()
    
    @abstractmethod
    def dump(self, obj, file):
        pass

    @abstractmethod
    def dumps(self, obj):
        pass

    @abstractmethod
    def load(self, file):
        pass

    @abstractmethod
    def loads(self, str):
        pass
    