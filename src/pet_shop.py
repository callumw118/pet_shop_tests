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

def remove_pet_by_name(pet_shop, name):
    pet_to_remove = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet_to_remove)
   
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]
    
def remove_customer_cash(customers, amount):
    total = get_customer_cash(customers) - amount
    customers["cash"] = total

def get_customer_pet_count(customers):
    return len(customers["pets"])
        
def add_pet_to_customer(customer_name, new_pet):
    customer_name["pets"].append(new_pet)
    
def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]
       
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet in pet_shop["pets"] and customer["cash"] >= pet["price"]:
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        increase_pets_sold(pet_shop, get_customer_pet_count(customer))
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
       
    
   


   
