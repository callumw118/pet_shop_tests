# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
    

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    total = get_total_cash(pet_shop) + cash
    pet_shop["admin"]["total_cash"] = total

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, increase_by):
    number_pets_sold = get_pets_sold(pet_shop) + increase_by
    pet_shop["admin"]["pets_sold"] = number_pets_sold

def get_stock_count(pet_shop):
    number_of_pets = len(pet_shop["pets"])
    return number_of_pets

def get_pets_by_breed(pet_shop, breed):
    total = []
    for pet in pet_shop["pets"]:
        if breed == pet["breed"]:
            total.append(pet)
    return total

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if name == pet["name"]:
            return pet
    return None
