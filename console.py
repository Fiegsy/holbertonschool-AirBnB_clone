#!/usr/bin/python3
"""Console module"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HBNBCommand class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty line handling"""
        pass

    def do_create(self, class_name):
        """Create command to create a new instance of a class"""
        if not class_name:
            print("** class name missing **")
            return

        try:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def check_args(self, argv):
        """Check if command line arguments are valid"""
        if not argv or argv[0] is None:
            print("** class name missing **")
            return False

        if argv[0] not in storage.classes:
            print("** class doesn't exist **")
            return False

        if len(argv) < 2:
            print("** instance id missing **")
            return False

        return True

    def do_show(self, args):
        """Show command to display string representation of an instance"""
        argv = args.split()
        if self.check_args(argv):
            my_class = argv[0]
            my_id = argv[1]
            obj = "{}.{}".format(my_class, my_id)
            if obj in storage.all():
                print(storage.all()[obj])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Destroy command to delete an instance"""
        argv = args.split()
        if self.check_args(argv):
            my_class = argv[0]
            my_id = argv[1]
            obj = "{}.{}".format(my_class, my_id)
            if obj in storage.all():
                del storage.all()[obj]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """All command to display all instances of a class"""
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args in storage.classes:
            print([str(obj) for obj in objects.values() if type(obj).__name__ == args])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Update command to update an instance"""
        argv = args.split()
        if not self.check_args(argv):
            return

        my_class = argv[0]
        my_id = argv[1]
        obj = "{}.{}".format(my_class, my_id)
        if obj not in storage.all():
            print("** no instance found **")
            return

        if len(argv) < 3:
            print("** attribute name missing **")
            return

        if len(argv) < 4:
            print("** value missing **")
            return

        setattr(storage.all()[obj], argv[2], argv[3])
        storage.all()[obj].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
