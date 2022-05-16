

from abc import ABC
from animal_factory.animals.anilmal import Animal

class WildAnimal(Animal, ABC):
    '''
     Subcategories : mammals, fish, birds, reptiles, and amphibians.
    '''
    def __init__(self, wildness:int = 0, **kwargs):
        super().__init__(**kwargs)
        self.wildness = wildness

    def set_wildness(self, wildness:int):
        self.wildness = wildness
        return self

    def is_wild(self) -> bool:
        return True