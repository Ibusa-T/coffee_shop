from coffee_shop.master_repository.repository import (
    ConsumerRepository, DeliveryRepository, ProductRepository, ProductTypeRepository, 
    SalesInfoRepository, SalePeriodRepository, SlipRepository
)

from abc import ABC, abstractmethod

consumer = ConsumerRepository.findAll()
delivery = DeliveryRepository.findAll()
product_type = ProductTypeRepository.findAll()
sales_info = SalesInfoRepository.findAll()
sale_period = SalePeriodRepository.findAll()
product = ProductRepository.findALL()
slip = SlipRepository.findAll()

#views    
class BaseAuterSchema(ABC):
    @classmethod
    @abstractmethod
    def get_context_data(cls):

        
#日ごとの商品別売上
class DalilySalesBYProductAuterSchema(BaseAuterSchema):
    @classmethod
    def get_context_data(cls):
        pass
    
#日ごと売上
class DalilySalesAuterSchema(BaseAuterSchema):
    @classmethod
    def get_context_data(cls):
        pass
    
#商品区分ごとの売上
class TypeSalesAuterSchema(BaseAuterSchema):
    @classmethod
    def get_context_data(cls):
        pass
    
#性別毎の商品売上
class GenderSalesAuterSchema(BaseAuterSchema):
    @classmethod
    def get_context_data(cls):
        pass
    

class VisitAuterSchema(BaseAuterSchema):
    @classmethod
    def get_context_data(cls):
        pass
    