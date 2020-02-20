from sys import argv
from os import system
from translator import translate, create_fabric, create_input
from testing import *

########################################################################################################################

openfile = None
amount_of_tests = None
area = None

########################################################################################################################

fields_list = []

########################################################################################################################

try:
    openfile = argv[1]
    amount_of_tests = int(argv[2])
    area = bool(argv[3])
except:
    print('error in args')
    exit(404)

if __name__ == '__main__':
    system('mkdir working_directory')  # создаем рабочую директорию
    fields_list = translate('models/' + openfile)
    print('model translated')
    print('fields:', *fields_list)
    create_fabric(openfile.split('.')[0])
    from working_directory.methods import create_instance

    object = create_instance()
    print('instance created')
    create_input(object)
    graph = random_tests(amount_of_tests, object)
    print(graph)
    system('rm -r working_directory')  # удаляем рабочую директорию
