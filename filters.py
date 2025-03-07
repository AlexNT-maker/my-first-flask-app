    cars_for_sale=[]

def filter_cars(cars_for_sale,key,value):
    return[car for car in cars_for_sale if str(car[key]).lower()==value.lower()]




def filter_by_brand(cars_for_sale):
    brand=input("Choose the brand you prefer to look for:").lower().strip()
    result=filter_cars(cars_for_sale,"Brand",brand)
    print_results(result,"brand",brand)
        



def filter_by_model(cars_for_sale):
   model=input("Enter the model you want to look for:").lower().strip()
   result=filter_cars(cars_for_sale, "Model", model)
   print_results(result,"model",model)
    

def filter_by_Year(cars_for_sale):
   try:
       year=int(input("Please type the year of your choice")).strip()
       if not year.isdigit():
           print("Invalid input only numbers are allowed")
           
       result=[car for car in cars_for_sale if car["Year"]==year]
       print_results(result, year, year)
   except ValueError:
       print("Invalid year")
       
       
       
       
       
       
def filter_by_price():
    try:
        min_price=int(input("\nPlease enter the minimum price you are looking for(you can type 0)").strip())
        if not min_price.isdigit():
            print("Invalid input only numbers are allowed")

        max_price=int(input("\n Please enter the maximum price").strip())
        if not max_price.isdigit():
            print("Invalid input only numbers are allowed")
    
        result=[car for car in cars_for_sale if min_price<=int(car["Price"])<=max_price]
        print_results(result, f"price range {min_price}-{max_price}", "")
        
    except ValueError:
        print("Invalid price!")
   


def print_results(results,category,value):
    if results:
        print(f"\ncars available for {category} '{value}':")
        for car in results:
            print(car)
    else:
        print(f"no cars found for {category} '{value}'")
            
    

  
