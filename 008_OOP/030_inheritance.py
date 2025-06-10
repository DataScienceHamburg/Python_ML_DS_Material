#%%
class Pet:
    is_human = False  # class attribute, identical for all instances

    def __init__(self, name):
        self.name = name
    
    def hello(self):
        print(f"Hello! My name is {self.name}")


class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.species = 'dog'
        self.breed = breed

    def hello(self):
        print(f"Hello! My name is {self.name}, I am a dog of type {self.breed}")

#%% instantiation
waldo = Dog(name="Waldo", breed="wiener dog")
waldo.hello()
# %%
waldo
# %%
