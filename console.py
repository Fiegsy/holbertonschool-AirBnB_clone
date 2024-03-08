import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def __init__(self, storage):
        super().__init__()
        self.storage = storage

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        if not args:
            print("** class name missing **")
            return

        cls_name, *attr_args = args.split()
        cls = getattr(__import__('models'), cls_name, None)
        if not cls:
            print("** class doesn't exist **")
            return

        new_instance = cls()
        self.storage.save()
        print(new_instance.id)

    def do_show(self, args):
        if not args:
            print("** class name missing **")
            return

        class_name, instance_id = args.split()
        instance_key = f"{class_name}.{instance_id}"
        instance = self.storage.all().get(instance_key)
        if not instance:
            print("** no instance found **")
            return

        print(instance)

    def do_destroy(self, args):
        if not args:
            print("** class name missing **")
            return

        class_name, instance_id = args.split()
        instance_key = f"{class_name}.{instance_id}"
        instances = self.storage.all()
        if instance_key not in instances:
            print("** no instance found **")
            return

        del instances[instance_key]
        self.storage.save()

    def do_all(self, args):
        if args:
            class_name = args.split()[0]
            instances = [str(instance) for key, instance in self.storage.all().items() if key.startswith(class_name)]
            print(instances)
        else:
            print([str(instance) for instance in self.storage.all().values()])

    def do_update(self, args):
        if not args:
            print("** class name missing **")
            return

        list_args = args.split()
        if len(list_args) < 2:
            print("** instance id missing **")
            return

        instance_key = f"{list_args[0]}.{list_args[1]}"
        instances = self.storage.all()
        if instance_key not in instances:
            print("** no instance found **")
            return

        if len(list_args) < 3:
            print("** attribute name missing **")
            return

        if len(list_args) < 4:
            print("** value missing **")
            return

        setattr(instances[instance_key], list_args[2], list_args[3])
        self.storage.save()

if __name__ == '__main__':
    storage = FileStorage()
    storage.reload()
    HBNBCommand(storage).cmdloop()
