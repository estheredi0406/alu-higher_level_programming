
import json
from base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

