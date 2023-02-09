#!/usr/bin/python3
"""
create unique filestorage insatance for your application
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
