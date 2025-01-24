from enum import Enum

class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"

class TextNode:
    def __init(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url