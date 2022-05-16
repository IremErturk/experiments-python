
from typing import TypeVar


# TLivingCondition = TypeVar("TLivingCondition", bound='LivingCondition')

class LivingCondition:
    def __init__(self, weather:str, geography:str):
        self.weather = weather
        self.geography = geography

class MammalLivingCondition(LivingCondition):
    def __init__(self, closeness_to_water:str, **kwargs):
        super().__init__(**kwargs)
        self.closeness_to_water = closeness_to_water
