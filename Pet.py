import json

class Pet:
    def __init__(self, name="none", age=0, type="none"):
        self.name = name
        self.age = age
        self.type = type

    def save_to_file(self):
        data = {"name":self.name,"age":self.age,"type":self.type}
        path_to_file = f"pets\{self.name}_pet.json"
        file = open(path_to_file, "w+")
        json.dump(data, file, ensure_ascii=False)
        file.close()

    def load_from_file(self):
        pass