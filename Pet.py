class Pet:
    def __init__(self, name="none", age=0, type="none"):
        self.name = name
        self.age = age
        self.type = type

    def process_pet_data(self, isCreating, petData="none"):
        if isCreating == 1:
            self.data = {"name":self.name,"age":self.age,"type":self.type}
            self.path_to_file = f"pets\{self.name}_pet.json"
        elif isCreating == 0:
            self.name = petData["name"]
            self.age = petData["age"]
            self.type = petData["type"]
        else:
            pass