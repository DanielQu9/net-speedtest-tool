from os import system
from getpass import getpass


def wait():
    """just wait."""
    system('')
    getpass('\033[31m>>puase \033[1;31m"Enter"\033[0m \033[31mto exit<<\033[0m')

if __name__ == '__main__':
    wait()