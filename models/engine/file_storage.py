#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    # self = <models.engine.file_storage.FileStorage object at 0x7f54106d03a0>
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            container = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    container[k] = v
            return container
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                """
                # temp = {'Place.861cb0ed-d4e2-4258-b8cc-e9893d264434':
                #  {'__class__': 'Place', 'city_id': '0001',
                #  'created_at': '2020-12-16T17:10:26.302193',
                #  'id': '861cb0ed-d4e2-4258-b8cc-e9893d264434',
                #  'latitude': '37.773972', 'longitude': '-122.431297',
                #  'max_guest': '10', 'name': 'My little house'
                # 'number_bathrooms': '2', ...},
                #  'State.2ce47b59-e40d-463b-a50f-8c127cb6385f'
                # {'_class_':'State', 'created_at':
                #  '2020-12-16T17:10:26.298419'
                # 'id': '2ce47b59-e40d-463b-a50f-8c127cb6385f',
                #  'name': 'California',
                #  'updated_at': '2020-12-16T17:10:26.298446'},
                #  'State.af7cff8d-55aa-4206-8487-af4733f701da':
                # {'__class__': 'State',
                # 'created_at': '2020-12-16T17:10:26.298761',
                # 'id': 'af7cff8d-55aa-4206-8487-af4733f701da',
                #  'name': 'Arizona', 'updated_at':
                #  '2020-12-16T17:10:26.298777'}}
                """
                temp = json.load(f)
                # 'Place.861cb0ed-d4e2-4258-b8cc-e9893d264434'
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a object inside the dict objects."""
        if obj is not None:
            del self.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)]

    def close(self):
        """Method for deserializing the JSON file to objects."""
        self.reload()
