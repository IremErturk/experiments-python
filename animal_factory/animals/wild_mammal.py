

from unicodedata import name
from animal_factory.animals.anilmal import Animal
from animal_factory.animals.wild_animal import WildAnimal
from animal_factory.living_conditions.living_condition import MammalLivingCondition


class WildMammal(WildAnimal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.living_condition: MammalLivingCondition = None

    def set_living_conditions(self, weather:str, geography:str,  closeness_to_water:str):
        self.living_condition = MammalLivingCondition(weather=weather, geography=geography, closeness_to_water=closeness_to_water)

    def speak(self):
        print(f"I am a Wild Mammal {self.name}") 

    def give_birth(self, partner: 'Animal', **kwargs) -> 'Animal':
        if not isinstance(partner, WildMammal):
            raise TypeError("Input to give_birth must be an WildMammal instance")
        
        newborn = WildMammal(age=0, gender='Female', wildness=self.wildness)
        newborn.living_condition = self.living_condition
        return newborn

    



    