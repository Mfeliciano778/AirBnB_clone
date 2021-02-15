#!/usr/bin/python3
'''Code for HBNB console, commands, and options'''

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
        pass

    def do_all(self, arg):
        '''all, prints string representation\
of all instances based or not on class name'''
        pass

    # ----- manage instances -----
    def do_create(self, arg):
        '''create, creates new instance of <classname> and prints id'''
        pass

    def do_destroy(self, arg):
        '''destroy, deletes instance based on class name and id'''
        pass

    def do_update(self, arg):
        '''update, updates an instance based on class name and id by\
 adding or updating attribute.\nex: update <classname> <id> <key> <value>'''
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
