import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def help_quit(self):
        print("Quit command to exit the program")

    def do_create(self, class_name):
        """Create a new instance of a class"""
        if not class_name:
            print("** class name missing **")
            return

        try:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def help_create(self):
        print("Create a new instance of a class")

    def do_show(self, args):
        """Show instance based on class name and id"""
        if not args:
            print("** class name missing **")
            return

        argv = args.split()
        if len(argv) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(argv[0], argv[1])
        all_objects = storage.all()
        if obj_key in all_objects:
            print(all_objects[obj_key])
        else:
            print("** no instance found **")

    def help_show(self):
        print("Show instance based on class name and id")

    def do_destroy(self, args):
        """Delete an instance based on class name and id"""
        if not args:
            print("** class name missing **")
            return

        argv = args.split()
        if len(argv) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(argv[0], argv[1])
        all_objects = storage.all()
        if obj_key in all_objects:
            del all_objects[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def help_destroy(self):
        print("Delete an instance based on class name and id")

    def do_all(self, class_name):
        """Show all instances or instances of a specific class"""
        all_objects = storage.all()
        if not class_name:
            print([str(obj) for obj in all_objects.values()])
        elif class_name in {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}:
            print([str(obj) for obj in all_objects.values() if type(obj).__name__ == class_name])
        else:
            print("** class doesn't exist **")

    def help_all(self):
        print("Show all instances or instances of a specific class")

    def do_update(self, args):
        """Update an instance based on class name, id, attribute name, and value"""
        if not args:
            print("** class name missing **")
            return

        argv = args.split()
        if len(argv) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(argv[0], argv[1])
        all_objects = storage.all()
        if obj_key not in all_objects:
            print("** no instance found **")
            return

        if len(argv) < 3:
            print("** attribute name missing **")
            return

        if len(argv) < 4:
            print("** value missing **")
            return

        attr_name, attr_value = argv[2], argv[3]
        setattr(all_objects[obj_key], attr_name, attr_value)
        storage.save()

    def help_update(self):
        print("Update an instance based on class name, id, attribute name, and value")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
