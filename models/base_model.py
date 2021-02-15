#!/usr/bin/python3
'''BaseModel class'''
import json
import uuid
from datetime import datetime as time


class BaseModel():
    '''BaseModel - defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''__init__ - instantiates attributes'''

        if len(kwargs) != 0:
            '''use given dict to create instance'''
            for key, value in kwargs.items():
                if key == '__class__':
                    setattr(self, key, type(self))
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            time.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = time.now()
            self.updated_at = self.created_at
            #storage here

    def __str__(self):
        '''__str__string rep of basemodel instance'''
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))

    def save(self):
        '''save - udpate updated_at'''
        self.updated_at = time.now()
        #storage here

    def to_dict(self):
        '''to_dict - gives dictionary rep of instance attr'''
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        new_dict['__class__'] = type(self).__name__
        return new_dict
