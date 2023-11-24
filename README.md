# ToDo-CLI

## Description

> A simple command line interface for managing your tasks.

## Documentation

### Use it as it is

**Clone the Repository**

```bash	
git clone https://github.com/CEOXeon/ToDo-CLI.git
```

**Use it right away**

```bash
python3 todo.py
```


---
---
---

### Use it in your python project

```python
import todo
```

---

**Display the Todo List**

```python
todo.display_todo_list(<ToDo List Object>)
```

---

**Add Task to the Todo List**

```python
todo.add_task(<ToDo List Object>, <Task Object>)
```

---

**Remove Task from the Todo List**

```python
todo.remove_task(<ToDo List Object>, <Task Number>)
```

---

**Load Todo List from a file**

```python
todo.load_todo_list()`
```

---

**Save Todo List to a file**

```python
todo.save_todo_list(<ToDo List Object>)
```