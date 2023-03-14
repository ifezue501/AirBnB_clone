#!/usr/bin/python3
"""
Test for storage
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):
    """Test FileStorage Class"""
    def setUp(self):
        self.storage = FileStorage()

    def test_instance(self):
        """Test instantation"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_all_returns_dict(self):
        """Test that all() method returns dictionary"""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new_adds_object_to_objects(self):
        """Test that new() method adds object to __object dictionary"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj._class_._name_, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save_writes_to_file(self):
        """Test that save() method writes to file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save
        with open(FileStorage.FileStorage_file_path, mode="r") as f:
        data = json.load(f)
        key = "{}.{}".format(obj._class_._name_, obj.id)
        self.assertIn(key, data)

    def test_reload_loads_from_file(self):
        """Test that reload() method loads from file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        key = "{}.{}".format(obj._class_._name_, obj.id)
        self.storage.FileStorage_objects[key].name = "Alice"
        self.storage.reload()
        self.assertNotEqual(self.storage.FileStorage_objects[key].name, "Alice")

    if __name__ == '__main__':
        unittest.main()
