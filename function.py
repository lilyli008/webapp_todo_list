FILEPATH='todos.txt'


def get_todos(filepath=FILEPATH):
    """ read a test file and return a list of to-do items
    :param filepath='files/todos.txt'
    :return: a list of return items
    """
    try:
        with open(filepath, 'r') as file:
            todos_local = file.readlines()
    except FileNotFoundError:
        todos_local=[]

    return todos_local


def write_todos(content,filepath=FILEPATH):
    """
    write a list of to_do items to a text file
    :param content: a list of to-do items
    :param filepath='files/todos.txt'
    :return:None
    """
    with open(filepath, 'w') as file:
        file.writelines(content)

print(__name__)

if __name__=="__main__":
    for x in get_todos('todos.txt'):
        print(x.strip())