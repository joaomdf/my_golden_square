from lib.todo_list import *
import pytest

'''
#1
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.
#2
- create __init__() method with no arguments in which to assign empty list 
to be used by other class methods to store, display or update todo list
- create add_todo() method with string argument for new task to add
- create check_todo() method with no argument that displays tasks numbered and 
formatted with new lines

#1
As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.
2#
- create update_todo() method with integer argument that removes taks from list
by adding 1 to arg and using the result to eliminate that index from list.
- return string "Good job! Task completed and removed from #TODO list!"
'''

'''
check if todo list is empty
'''
def test_todo_list_is_empty():
    t = ToDo()
    assert t.check_todo() == "Good job! You have no tasks to complete!"

'''
check if add_todo adds task
'''
def test_add_task():
    t = ToDo()
    t.add_todo("Walk the dog")
    assert t.check_todo() == ["Walk the dog"]

'''
check if add_todo adds several tasks
'''
def test_adds_several_task():
    t = ToDo()
    t.add_todo("Walk the dog")
    t.check_todo()
    t.add_todo("Feed the fish")
    assert t.check_todo() == ["Walk the dog", "Feed the fish"]

'''
check if add_todo adds several tasks
and check_todo displays them correctly
'''
def test_adds_several_tasks_and_check_todo_displays_them():
    t = ToDo()
    t.add_todo("Walk the dog")
    t.add_todo("Feed the fish")
    assert t.check_todo() == ["Walk the dog", "Feed the fish"]

'''
check if add_todo errors if empty string task is given
and returns message "That's not a task!"
'''
def test_add_todo_errors_when_given_empty_task():
    t = ToDo()
    with pytest.raises(Exception) as err:
        t.add_todo("")
    error_message = str(err.value)
    assert error_message == "That is not a valid task!"

'''
check if update_todo removes task from list
'''
def test_update_removes_task_from_list():
    t = ToDo()
    t.add_todo("Walk the dog")
    t.update_todo(0)
    assert t.check_todo() == "Good job! You have no tasks to complete!"

'''
check if update_todo removes several tasks from list
'''
def test_update_removes_several_tasks_from_list():
    t = ToDo()
    t.add_todo("Walk the dog")
    t.add_todo("Feed the fish")
    t.add_todo("Stare down the cat")
    t.update_todo(0)
    assert t.check_todo() == ["Feed the fish", "Stare down the cat"]
    t.update_todo(0)
    assert t.check_todo() == ["Stare down the cat"]

'''
check if update_todo errors when there are no taks to complete
'''
def test_update_todo_errors_when_no_tasks_left():
    t = ToDo()
    t.add_todo("Walk the dog")
    t.update_todo(0)
    with pytest.raises(Exception) as err:
        t.update_todo(0)
    error_message = str(err.value)
    assert error_message == "You have no tasks left to complete!"

'''
check if check_todo is updated after running update_todo
'''
def test_update_todo_errors_when_index_is_not_valid():
    t = ToDo()
    t.add_todo("Walk the dog")
    with pytest.raises(Exception) as err:
        t.update_todo(-1)
    error_message = str(err.value)
    assert error_message == "That is not a valid task!"