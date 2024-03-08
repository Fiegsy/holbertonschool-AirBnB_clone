class Console:
    """Interactive console for handling models"""

    def __init__(self):
        """Initialize the Console"""
        self.models = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def run(self):
        """Start the console"""
        while True:
            command = input("(hbnb) ")
            if command == "quit":
                break
            self.execute(command)

    def execute(self, command):
        """Execute the given command"""
        parts = command.split()
        if len(parts) == 0:
            return

        if parts[0] in self.models:
            model = self.models[parts[0]]
            if len(parts) > 1:
                if parts[1] == "create":
                    instance = model()
                    instance.save()
                    print(instance.id)
                elif parts[1] == "show":
                    if len(parts) < 3:
                        print("** instance id missing **")
                    else:
                        instances = storage.all()
                        key = "{}.{}".format(parts[0], parts[2])
                        if key in instances:
                            print(instances[key])
                        else:
                            print("** no instance found **")
                elif parts[1] == "destroy":
                    if len(parts) < 3:
                        print("** instance id missing **")
                    else:
                        instances = storage.all()
                        key = "{}.{}".format(parts[0], parts[2])
                        if key in instances:
                            del instances[key]
                            storage.save()
                        else:
                            print("** no instance found **")
            else:
                print("** command missing **")
        else:
            print("** invalid command **")

if __name__ == "__main__":
    console = Console()
    console.run()
