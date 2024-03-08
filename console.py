from models.base_model import BaseModel
from models import storage

class Console:
    def do_create(self, args):
        """Creates a new instance of a given class"""
        if not args:
            print("** class name missing **")
            return

        class_name, *attr_args = args.split()
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        cls = globals()[class_name]
        new_instance = cls()
        storage.save()
        print(new_instance.id)

    def do_show(self, args):
        """Shows the string representation of an instance"""
        if not args:
            print("** class name missing **")
            return

        class_name, instance_id = args.split()
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        instance_key = f"{class_name}.{instance_id}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[instance_key])

    def do_destroy(self, args):
        """Deletes an instance"""
        if not args:
            print("** class name missing **")
            return

        class_name, instance_id = args.split()
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        instance_key = f"{class_name}.{instance_id}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[instance_key]
        storage.save()

    def do_all(self, args):
        """Shows all instances of a class"""
        if not args:
            print([str(storage.all()[id]) for id in storage.all()])
            return

        if args not in globals():
            print("** class doesn't exist **")
            return

        instances = [str(storage.all()[id]) for id in storage.all() if args in id]
        print(instances)

    def do_update(self, args):
        """Updates an instance attribute"""
        if not args:
            print("** class name missing **")
            return

        class_name, instance_id, attr_name, attr_value = args.split()
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        instance_key = f"{class_name}.{instance_id}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return

        setattr(storage.all()[instance_key], attr_name, attr_value)
        storage.save()

    def do_quit(self, arg):
        """Exits the console"""
        return True

    def do_EOF(self, arg):
        """Exits the console with EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Handles empty line input"""
        pass

if __name__ == "__main__":
    console = Console()
    console.cmdloop()
