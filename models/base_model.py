#!/usr/bin/python3
"""
base module that contains BaseModel
that define common attributes/methods for other classes
"""

import sys
import uuid
import datetime
import models


class BaseModel:
    """
    defines common attr/methods for the other classes
    """

    def __init__(self, *args, **kwargs):
        """
        instatiation of the BaseModel class
        """
        if len(kwargs) != 0:
            self.id = kwargs['id']
            self.created_at = datetime.datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """
        update the attr updated at
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def __str__(self):
        """
        overide str
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        return the dict defination of the instance
        """
        a = self.__dict__
        a["__class__"] = self.__class__.__name__
        a["created_at"] = str(self.created_at.isoformat())
        a["updated_at"] = str(self.updated_at.isoformat())
        return a
