from abc import ABC, abstractmethod
class Baserepository(ABC):
    @classmethod
    @abstractmethod
    def insert(cls,**kwargs):
        pass         

    @classmethod
    @abstractmethod
    def findAll(cls):
        pass
    
    @classmethod
    def delete(cls):
        pass
    