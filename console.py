#!/usr/bin/python3
'''Code for HBNB console, commands, and options'''

from models import base_model
from models import user
from models import state
from models import city
from models import place
from models import amenity
from models import review
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
        if all([class_name_exist(arg), class_exist(arg), id_arg_exist(arg),
           id_exist(arg)]):
            # print string repr of instance
            pass

    def do_all(self, arg):
        '''all, prints string representation\
of all instances based or not on class name'''
        if arg:
            if class_exist(arg):
                #print all instances of class
                pass
        else:
            # print all instances
            pass

    # ----- manage instances -----
    def do_create(self, arg):
        '''create, creates new instance of <classname> and prints id'''
        if class_name_exist(arg) and class_exist(arg):
            # create new instance
            # save to json
            # print id
            pass

    def do_destroy(self, arg):
        '''destroy, deletes instance based on class name and id'''
        if all([class_name_exist(arg), class_exist(arg), id_arg_exist(arg),
           id_exist(arg)]):
            # delete instance and save change
            pass

    def do_update(self, arg):
        '''update, updates an instance based on class name and id by\
 adding or updating attribute.\nex: update <classname> <id> <key> <value>'''
        if all([class_name_exist(arg), class_exist(arg), id_arg_exist(arg),
           id_exist(arg), attr_arg_check(arg), id_arg_exist(arg)]):
            # update instance attr with attr arg[2] and str casted val arg[3]
            pass

    @staticmethod
    def class_name_exist(arg):
        '''check arg for class name'''
        if len(arg) < 1:
            print("** class name missing **\n")
            return False
        return True

    @staticmethod
    def class_exist(arg):
        '''check arg for class existing'''
        # search storage for matching class
        return True

    @staticmethod
    def id_arg_exist(arg):
        '''check arg for id'''
        if len(arg) < 2:
            print("** instance id missing **\n")
            return False
        return True

    @staticmethod
    def id_exist(arg):
        '''check arg for id existing'''
        # search storage for matching id
        return True

    @staticmethod
    def attr_arg_check(arg):
        '''check arg for attr name'''
        if len(arg) < 3:
            print("** attribute name missing **\n")
            return False
        return True

    @staticmethod
    def val_arg_exist(arg):
        '''check arg for attribute val exist'''
        if len(arg) < 4:
            print("** value missing **\n")
            return False
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
