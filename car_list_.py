<<<<<<< HEAD
import random  
from car_for_sale import cars_data,save_to_json,load_from_json
from filters import filter_cars,filter_by_brand,filter_by_Year,filter_by_model,filter_by_price,print_results


cars_for_sale=load_from_json()


def note(cars_for_sale):
    return f"The prices are in Euros. There are {len(cars_for_sale)} cars available."
    if cars_for_sale is None:
        return "No cars available"
try:             
    print(note(cars_for_sale))
except Exception as bug:
    print("Something went wrong",type(bug))
    
note(cars_for_sale)

#Here is a note that will appear to our visitors, the parameters of the def note\
#are the cars that are available for sale in our site. If the note can not run\
#in our program as we expect the message Something went wrong will appear in\
#visitors screen.

def i_feel_lucky():
    if not cars_for_sale:
        print("No cars available at this moment")
        return None
    my_lucky_car=random.choice(cars_for_sale)
    my_lucky_car["Price"] = int(my_lucky_car["Price"])
    my_lucky_car["Price"]= int(my_lucky_car["Price"]*0.9)
    save_to_json(cars_for_sale)
    return my_lucky_car
   
#Here is a random choice of a car in the list that will give you a 10%discount\n
#every time you run the code and you choose the option i feel lucky
lucky_car=i_feel_lucky()

while True: #a loop which interacts with the user from the console 
    print("\nMenu:")
    print("add a new car")
    print("i feel lucky")
    print("look for cars")
    print("I have sell my car")
    print("Exit")
    print("Choose to filter your search by brand, model, year, price type filter")
   
    choice=input("Please enter your choice:").lower().strip()
    if(choice=="add a new car"):
        new_car=cars_data()
        cars_for_sale.append(new_car)
        save_to_json(cars_for_sale)
        print("\nCar added successfuly for sale")
        print(f'''\n Your {new_car['Brand']} {new_car['Model']}, of the year {new_car['Year']},
has added succesfuly in the price of {new_car['Price']}''')
        
     
    if(choice=="i feel lucky"): 
        print (f'''\nYour lucky car is {lucky_car["Brand"]} {lucky_car["Model"]} of 
             {lucky_car["Year"]} and you won a 10% discount 
             for today the new price is {lucky_car['Price']} Euros''')   
        
    
    if(choice=="look for cars"):
        print(cars_for_sale)
        
    if(choice=="i have sell my car"):
        print("I am happy for you,give us more information about your car")
        car_brand=input("Give us the brand:").strip().lower()
        car_model=input("Give us the model:").strip().lower()
        found=False
        for car in cars_for_sale:
            if(car["Brand"].lower()==car_brand) and (car["Model"].lower()==car_model):
                cars_for_sale.remove(car)
                save_to_json(cars_for_sale)
                print(f"Your {car['Brand']} {car['Model']} has removed succesfully")
                found=True
                break
        if not found:
            print("No car found with this information")
       
            
       
    if(choice=="exit"):
        print("\nThank you for using our program")
        break

    else:
        TypeError
        print("Choose a valid option")
        
    
    if(choice=="filter"):
        choice_2=input("\nFor filter by brand type 1,for model type 2,for year type3 and for price type 4").strip()
        
        if not choice_2.isdigit():
            print("Letters are not valid please type a number in range(1-4)")
        
        if choice_2=="1":
            filter_by_brand(cars_for_sale)
            
        if choice_2=="2":
            filter_by_model(cars_for_sale)
        
        if choice_2=="3":
            filter_by_Year(cars_for_sale)
            
        if choice_2=="4":
            filter_by_price(cars_for_sale)
       
        
        else:
            print("please choose a valid option")
        
            
        
        
        
   
   
        
        
            
        



    

    




    
    

=======
import random  
from car_for_sale import cars_data,save_to_json,load_from_json
from filters import filter_cars,filter_by_brand,filter_by_Year,filter_by_model,filter_by_price,print_results


cars_for_sale=load_from_json()


def note(cars_for_sale):
    return f"The prices are in Euros. There are {len(cars_for_sale)} cars available."
    if cars_for_sale is None:
        return "No cars available"
try:             
    print(note(cars_for_sale))
except Exception as bug:
    print("Something went wrong",type(bug))
    
note(cars_for_sale)

#Here is a note that will appear to our visitors, the parameters of the def note\
#are the cars that are available for sale in our site. If the note can not run\
#in our program as we expect the message Something went wrong will appear in\
#visitors screen.

def i_feel_lucky():
    if not cars_for_sale:
        print("No cars available at this moment")
        return None
    my_lucky_car=random.choice(cars_for_sale)
    my_lucky_car["Price"] = int(my_lucky_car["Price"])
    my_lucky_car["Price"]= int(my_lucky_car["Price"]*0.9)
    save_to_json(cars_for_sale)
    return my_lucky_car
   
#Here is a random choice of a car in the list that will give you a 10%discount\n
#every time you run the code and you choose the option i feel lucky
lucky_car=i_feel_lucky()

while True: #a loop which interacts with the user from the console 
    print("\nMenu:")
    print("add a new car")
    print("i feel lucky")
    print("look for cars")
    print("I have sell my car")
    print("Exit")
    print("Choose to filter your search by brand, model, year, price type filter")
   
    choice=input("Please enter your choice:").lower().strip()
    if(choice=="add a new car"):
        new_car=cars_data()
        cars_for_sale.append(new_car)
        save_to_json(cars_for_sale)
        print("\nCar added successfuly for sale")
        print(f'''\n Your {new_car['Brand']} {new_car['Model']}, of the year {new_car['Year']},
has added succesfuly in the price of {new_car['Price']}''')
        
     
    if(choice=="i feel lucky"): 
        print (f'''\nYour lucky car is {lucky_car["Brand"]} {lucky_car["Model"]} of 
             {lucky_car["Year"]} and you won a 10% discount 
             for today the new price is {lucky_car['Price']} Euros''')   
        
    
    if(choice=="look for cars"):
        print(cars_for_sale)
        
    if(choice=="i have sell my car"):
        print("I am happy for you,give us more information about your car")
        car_brand=input("Give us the brand:").strip().lower()
        car_model=input("Give us the model:").strip().lower()
        found=False
        for car in cars_for_sale:
            if(car["Brand"].lower()==car_brand) and (car["Model"].lower()==car_model):
                cars_for_sale.remove(car)
                save_to_json(cars_for_sale)
                print(f"Your {car['Brand']} {car['Model']} has removed succesfully")
                found=True
                break
        if not found:
            print("No car found with this information")
       
            
       
    if(choice=="exit"):
        print("\nThank you for using our program")
        break

    else:
        TypeError
        print("Choose a valid option")
        
    
    if(choice=="filter"):
        choice_2=input("\nFor filter by brand type 1,for model type 2,for year type3 and for price type 4").strip()
        
        if not choice_2.isdigit():
            print("Letters are not valid please type a number in range(1-4)")
        
        if choice_2=="1":
            filter_by_brand(cars_for_sale)
            
        if choice_2=="2":
            filter_by_model(cars_for_sale)
        
        if choice_2=="3":
            filter_by_Year(cars_for_sale)
            
        if choice_2=="4":
            filter_by_price(cars_for_sale)
       
        
        else:
            print("please choose a valid option")
        
            
        
        
        
   
   
        
        
            
        



    

    




    
    

>>>>>>> d667fcd (Updated the project with script code and extra features on the HTML interface)
