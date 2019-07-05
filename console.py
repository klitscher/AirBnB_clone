#!/usr/bin/python3
"""Define Holberton BnB console"""
import cmd
import sys
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
        Starting point of command interpreter
    """

    prompt = ("(hbnb) ")

    def emptyline(self):
        """pass and do nothing with input line"""
        pass

    def do_quit(self, args):
        return True

    def do_EOF(self, args):
        return True

    def default(self, args):
        """ Default catches all function names not spcifically defined"""
        functs = {"all": self.do_all,
                  "update": self.do_update,
                  "show": self.do_show,
                  "count": self.do_count,
                  "destroy": self.do_destroy}
        args = (args.replace("(", ".").replace(")", ".")
                    .replace('"', "").replace(",", "").split("."))

        try:
            commands = args[0] + " " + args[2]
            func = functs[args[1]]
            func(commands)
        except:
            print("*** Unknown syntax:", args[0])

    def do_create(self, args):
        """Creates new instance of class BaseModel
        saves it to json file
        """

        if len(args) == 0:
            print("** class name missing **")
            return

        try:
            args = shlex.split(args)
            newModel = eval(args[0])()
            newModel.save()
            print(newModel.id)

        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
           prints string reps of instance based on class name and ID
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        object_dict = storage.all()

        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        keys = args[0] + "." + args[1]
        keys = args[0] + "." + args[1]
        try:
            Value = object_dict[keys]
            print(Value)
        except KeyError:
            print("** no instance found **")

    def do_count(self, args):
        """
            counts numb of instances
        """
        object_list = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for keys, value in objects.items():
            if len(args) != 0:
                if type(value) is eval(args):
                    object_list.append(value)
            else:
                object_list.append(value)
        print(len(object_list))

    def do_destroy(self, args):
        """ deletes instance base on class name and id """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        classN = args[0]
        classI = args[1]
        storage = FileStorage()
        storage.reload()
        object_dict = storage.all()
        try:
            eval(classN)
        except NameError:
            print("** class doesn't exist **")
            return
        keys = classN + "." + classI
        try:
            del object_dict[keys]
        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_update(self, args):
        """ Updates instance on name and ID passed in """
        storage = FileStorage()
        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        keys = args[0] + "." + args[1]
        object_dict = storage.all()
        try:
            object_value = object_dict[keys]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attribute_type = type(getattr(object_value, args[2]))
            args[3] = attribute_type(args[3])
        except AttributeError:
            pass
        setattr(object_value, args[2], args[3])
        object_value.save()

    def do_all(self, args):
        """ Prints all string reps of all instances """
        object_list = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for keys, value in objects.items():
            if len(args) != 0:
                if type(value) is eval(args):
                    object_list.append(value.__str__())
            else:
                object_list.append(value.__str__())
        print(object_list)

if __name__ == "__main__":
    """ Start point for loop """
    HBNBCommand().cmdloop()
