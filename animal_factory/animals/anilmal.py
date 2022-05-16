

from abc import ABC, abstractmethod
from typing import Optional
from animal_factory.animals.animal_identifier import AnimalIdentifier

from animal_factory.living_conditions.living_condition import LivingCondition


class Animal(ABC):
    '''
     Subcategories : WildAnimal, DomesticAnimal
    '''
    def __init__(self, age:int, gender:str, name:AnimalIdentifier= None):
        self.name: AnimalIdentifier = AnimalIdentifier.generate() \
            if name is None \
            else name
        self.age: int = age
        self.gender: str = gender

    @abstractmethod
    def is_wild(self) -> bool:
        raise NotImplemented

    @abstractmethod
    def speak(self):
        raise NotImplementedError

    @abstractmethod
    def give_birth(self, partner:'Animal', **kwargs) -> 'Animal':
        raise NotImplemented