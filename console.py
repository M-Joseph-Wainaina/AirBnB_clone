#!/usr/bin/python3
"""
entry point to the command interpreter
"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    class defination of the command interprter
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """close the console"""
        exit()
    def do_EOF(self, args):
        """exit the program"""
        exit()


if __name__ == '__main__':
        HBNBCommand().cmdloop()
