def translate(input_file):
    lines = open(input_file, 'r').readlines()
    file = open('working_directory/output.py', 'w')
    reading = False
    fields = []
    for line in lines:
        if 'def ' in line:
            reading = False
        clean_line = line.replace('\n', '').replace(' ', '').replace('\t', '')
        if reading and clean_line != "":
            fields.append(clean_line.split('=')[0])
        file.write(line)
        if 'class ' in line:
            reading = True
    file.close()
    return fields


def create_fabric(classname):
    file = open('working_directory/methods.py', 'w')
    create_create_instance(classname, file)
    # create_getter(classname, fields, file)
    file.close()


def create_create_instance(classname, file):
    file.write('def create_instance():\n')
    file.write('    from working_directory.output import ' + classname + '\n')
    file.write('    return ' + classname + '()\n\n\n')


# def create_getter(fields, file):
#     file.write('def get_fields_info(object):\n')
#     line = ''
#     for field in fields:
#         line += '"' + field + '": object.' + field + ', '
#     line = line[0:len(line) - 2]
#     file.write('    return {' + line + '}')


def create_input(object):
    file = open('working_directory/inputs.py', 'w')
    file.write('def make_input(object):\n')
    file.write('    from random import choice\n')
    line = '    object.input('
    for field in object.input_info().keys():
        line += field + '=choice(object.input_info()["' + field + '"]), '
    line = line[0:len(line) - 2]
    file.write(line + ')\n')
    file.close()
