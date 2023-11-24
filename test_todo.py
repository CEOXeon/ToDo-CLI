import unittest
import os
import json
from todo import add_task, remove_task, save_todo_list, load_todo_list

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        self.todo_list = []

    def test_add_task(self):
        add_task(self.todo_list, "Test task")
        self.assertEqual(self.todo_list, ["Test task"])

    def test_remove_task(self):
        add_task(self.todo_list, "Test task")
        remove_task(self.todo_list, 0)
        self.assertEqual(self.todo_list, [])

    def test_save_and_load_todo_list(self):
        add_task(self.todo_list, "Test task")
        save_todo_list(self.todo_list)
        loaded_list = load_todo_list()
        self.assertEqual(loaded_list, ["Test task"])

    def tearDown(self):
        if os.path.exists("todo_list.json"):
            os.remove("todo_list.json")

if __name__ == "__main__":
    unittest.main()