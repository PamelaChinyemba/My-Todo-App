FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH):
    """Read the text file and return the todolist"""
    with open(filepath, 'r') as fp:
        todos_local = fp.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the text file with the values of the todolist"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


