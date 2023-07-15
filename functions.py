FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Opens the todos text file
    and returns the lines as a list.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the todo items in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)