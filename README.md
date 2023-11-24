# ToDo-CLI

## Description

> A simple command line interface for managing your tasks.

## Documentation

### Use it as it is

#### **Clone the Repository**

```bash
git clone https://github.com/CEOXeon/ToDo-CLI.git
```

#### **Use it right away**

```bash
python3 todo.py
```

---
---

### Use it in your python project

```python
# Import the todo module
import todo

# Display the Todo List
todo.display_todo_list(<ToDo List Object>)

# Add Task to the Todo List
todo.add_task(<ToDo List Object>, <Task Object>)

# Remove Task from the Todo List
todo.remove_task(<ToDo List Object>, <Task Number>)

# Load Todo List from a file
todo.load_todo_list()

# Save Todo List to a file
todo.save_todo_list(<ToDo List Object>)
```

```<ToDo List Object>``` Is the Todo List (Python Class: List)

```<Task Object>``` Is the Task (Python Class: String)

```<Task Number>``` Is the Number of the Task (Python Class: Integer)
