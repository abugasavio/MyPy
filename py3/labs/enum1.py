from enum import Enum


class Location(Enum):
    NAIROBI = 'Nai'
    MOMBASA = 'Mombasa'
    KERICHO = 'Kericho'

    @classmethod
    def choices(cls):
        return [(key, item.value) for key, item in cls.__members__.items()]


Location.choices()
 