#!/usr/bin/python3
'''Code for HBNB console, commands, and options'''

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import cmd


class HBNBCommand(cmd.Cmd):
    '''class that holds commands and options for HBNBCommand'''
    prompt = '(hbnb) '

    def emptyline(self):
        '''Catches emptyline to not run anything'''
        pass

    # ----- basic commands -----
    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        '''EOF command to exit the program'''
        print('')
        return True

    # ----- view instances -----
    def do_show(self, arg):
        '''show, prints string representation\
of a instance based on class name and id'''
        if len(arg) < 1: # check for class name exist?
            print("** class name missing **")
        elif True: # search storage for matching class
            print("** class doesn't exist **")
        elif len(arg) < 2: # id arg exist?
            print("** instance id missing **")
        elif True: # search storage for matching id
            print("** no instance found **")
        else:
            # print string repr of instance
            pass

    def do_all(self, arg):
        '''all, prints string representation\
of all instances based or not on class name'''
        if arg:
            if True: # search storage for matching class
                #print all instances of class
                pass
        else:
            # print all instances
            pass

    # ----- manage instances -----
    def do_create(self, arg):
        '''create, creates new instance of <classname> and prints id'''
        if len(arg) < 1: # class name exist?
            print("** class name missing **")
        elif True: # search storage for matching class
            print("** class doesn't exist **")
        else:
            # create new instance
            # save to json
            # print id
            pass

    def do_destroy(self, arg):
        '''destroy, deletes instance based on class name and id'''
        if len(arg) < 1: # class name exist?
            print("** class name missing **")
        elif True: # search storage for matching class
            print("** class doesn't exist **")
        elif len(arg) < 2: # id arg exist?
            print("** instance id missing **")
        elif True: # search storage for matching id
            print("** no instance found **")
        else:
            # delete instance and save change
            pass

    def do_update(self, arg):
        '''update, updates an instance based on class name and id by\
 adding or updating attribute.\nex: update <classname> <id> <key> <value>'''
        if len(arg) < 1: # class name exist?
            print("** class name missing **")
        elif True: # search storage for matching class
            print("** class doesn't exist **")
        elif len(arg) < 2: # id arg exist?
            print("** instance id missing **")
        elif True: # search storage for matching id
            print("** no instance found **")
        elif len(arg) < 3: # attr arg exist?
            print("** attribute name missing **")
        elif len(arg) < 4: # val arg exist?
            print("** value missing **")
        else:
            # update instance attr with attr arg[2] and str casted val arg[3]
            pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
