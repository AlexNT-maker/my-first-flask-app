<<<<<<< HEAD
import json



cars_for_sale=[]

def cars_data():
    global cars_for_sale
    new_car=dict()
    new_car["Brand"]=input("Type Brand:")
    new_car["Model"]=input("Type Model:")
    new_car["Year"]=int(input("Type Year:"))
    new_car["Price"]=input("Price of sale:")
    cars_for_sale.append(new_car)
    return new_car


  #This def is made to make it import in the main program(car_list), so the code
  #can stay readable for the users 


def save_to_json(cars_for_sale):
    with open ("cars.json",'w') as file:
        json.dump(cars_for_sale,file,indent=4)
        
    #save data in json
    
    
def load_from_json():
    try:
        with open ("cars.json",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        
=======
import json



cars_for_sale=[]

def cars_data():
    global cars_for_sale
    new_car=dict()
    new_car["Brand"]=input("Type Brand:")
    new_car["Model"]=input("Type Model:")
    new_car["Year"]=int(input("Type Year:"))
    new_car["Price"]=input("Price of sale:")
    cars_for_sale.append(new_car)
    return new_car


  #This def is made to make it import in the main program(car_list), so the code
  #can stay readable for the users 


def save_to_json(cars_for_sale):
    with open ("cars.json",'w') as file:
        json.dump(cars_for_sale,file,indent=4)
        
    #save data in json
    
    
def load_from_json():
    try:
        with open ("cars.json",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        
>>>>>>> d667fcd (Updated the project with script code and extra features on the HTML interface)
    #load data from json