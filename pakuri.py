import math
from hashlib import md5
class Pakuri:
    def __init__(self, name, species, level = 0):

        self._name = name
        self._species = species
        self._level = level

        _1species = md5(species.encode())
        _2species = int.from_bytes(_1species.digest(), byteorder='little')
        _1name = md5(name.encode())
        _2name = int.from_bytes(_1name.digest(), byteorder='little')


        self._attack = (_2species % 16) + (_2name % 16)
        self._defense = ((_2species + 5) % 16) + ((_2name + 5) % 16)
        self._stamina = ((_2species + 11) % 16) + ((_2name + 11) % 16)

        self._hp = math.floor(self._stamina * (self._level / 6))
        self._cp = math.floor(self._attack * math.sqrt(self._defense) * math.sqrt(self._stamina) * level * 0.08)





    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level
        self._hp = math.floor(self._stamina * (self._level / 6))
        self._cp = math.floor(self._attack * math.sqrt(self._defense) * math.sqrt(self._stamina) * level * 0.08)


    @property
    def name(self):
        return self._name
    @property
    def species(self):
        return self._species
    @property
    def hp(self):
        return self._hp
    @property
    def cp(self):
        return self._cp