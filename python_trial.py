from os import getcwd
from os.path import abspath
from os.path import join
from os import system
current = abspath(__file__).replace('\\', '/').split('/')
cur = join(*current[0:len(current) - 1])
system('cd /' + cur)