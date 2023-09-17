#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

db_type = getenv('HBNB_TYPE_STORAGE')
if db_type == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
