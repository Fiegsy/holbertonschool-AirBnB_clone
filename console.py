class Console:
    def __init__(self):
        self.commands = {
            "create": self.create_instance,
            "show": self.show_instance,
            "destroy": self.destroy_instance,
            "all": self.show_all_instances,
            "update": self.update_instance
        }

    def create_instance(self, args):
        if len(args) == 0:
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

    def show_instance(self, args):
        if len(args) == 0:
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

    def destroy_instance(self, args):
        if len(args) == 0:
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

    def show_all_instances(self, args):
        if len(args) == 0:
            print([str(storage.all()[id]) for id in storage.all()])
            return

        if args not in globals():
            print("** class doesn't exist **")
            return

        instances = [str(storage.all()[id]) for id in storage.all() if args in id]
        print(instances)

    def update_instance(self, args):
        if len(args) == 0:
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

    def run(self):
        while True:
            command = input("(hbnb) ")
            if command == "quit":
                break
            self.execute(command)

    def execute(self, command):
        parts = command.split()
        if len(parts) == 0:
            return

        if parts[0] in self.commands:
            self.commands[parts[0]](" ".join(parts[1:]))
        else:
            print("** invalid command **")

if __name__ == "__main__":
    console = Console()
    console.run()
