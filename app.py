from flask import Flask,render_template,request,redirect
import json

#create the flask app
app=Flask(__name__)


def load_cars():
    try:
        with open("cars.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] #returns a blank list if no file exists
    
def save_cars(cars):
    with open("cars.json",'w') as file:
        json.dump(cars, file, indent=4) #indent 4 improve the style of json file indent 4 means 4 spaces
   
        


@app.route("/")

def home():
    cars=load_cars()
    return render_template("index.html",cars=cars)

@app.route("/add_car", methods=["POST"])
def add_car():
    new_car = {
        "Brand": request.form["brand"],
        "Model": request.form["model"],
        "Year": int(request.form["year"]),
        "Price": int(request.form["price"])
    }
    cars = load_cars()
    cars.append(new_car)
    save_cars(cars)
    return redirect("/")  #return to the home page 

@app.route("/delete_car", methods=["POST"])
def delete_car():
    brand=request.form["brand"]
    model=request.form["model"]
    year=int(request.form["year"])
    
    cars=load_cars()
    
    updated_cars = [car for car in cars if not (car["Brand"] == brand and car["Model"] == model and car["Year"] == year)]
    
    save_cars(updated_cars)
    
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True)
    
#debug=True is allowing to bugs to appear in the browser

