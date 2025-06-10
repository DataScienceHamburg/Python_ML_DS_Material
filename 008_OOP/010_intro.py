#%% class definition
class Pet:
    pass
# %% instantiate an object
kiki = Pet()
# %%
print(kiki)
# %%
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

pet_one = Pet("Kiki", "dog")
pet_two = Pet("Bubbles", "cat")
# %%
pet_one.name
# %% Object Methods
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def hello(self):
        print(f"Hello! My name is {self.name} and I am a {self.species}")

pet_one = Pet("Kiki", "dog")
pet_two = Pet("Bubbles", "cat")

# %%
pet_one.hello()
# %%
pet_new = Pet('Waldo', 'dog')
pet_new2 = Pet('Waldo', 'dog')
