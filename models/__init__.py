#!/usr/bin/python3
"""
 Create the storage instance & Load serialized objects from the JSON file
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
