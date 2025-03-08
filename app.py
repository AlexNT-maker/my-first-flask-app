from flask import Flask,render_template,request,redirect,jsonify
import json
import random

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

@app.route("/lucky_car", methods=["GET"])
def lucky_car():
    cars = load_cars()
    if not cars:
        return jsonify({"message": "No cars available!"})
    
    lucky = random.choice(cars)
    discounted_price = int(lucky["Price"] * 0.9)  # Apply 10% discount
    lucky["Price"] = discounted_price  # Update price in memory
    
    return jsonify(lucky)

@app.route("/filter_cars", methods=["GET"])
def filter_cars():
    brand = request.args.get("brand", "").lower()
    model = request.args.get("model", "").lower()
    year = request.args.get("year", "")
    price = request.args.get("price", "")

    cars = load_cars()

    filtered_cars = [
        car for car in cars
        if (not brand or car["Brand"].lower() == brand) and
           (not model or car["Model"].lower() == model) and
           (not year or car["Year"] == int(year)) and
           (not price or car["Price"] <= int(price))
    ]
    
    return jsonify(filtered_cars)


if __name__=="__main__":
    app.run(debug=True)
    
#debug=True is allowing to bugs to appear in the browser

