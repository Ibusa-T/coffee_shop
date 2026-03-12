from abc import ABC, abstractmethod
from coffee_shop.container.master_factory import MasterFactory

class Baserepository(ABC):
    name = None
    master_factory = MasterFactory    
    @classmethod
    @abstractmethod
    def findAll(cls):
        pass
    
    
    @classmethod
    @abstractmethod
    def insert(cls,**kwargs):
        pass         

     
    @classmethod
    @abstractmethod
    def delete(cls):
        pass
    