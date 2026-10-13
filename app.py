from flask import Flask, request, render_template
import joblib

model = joblib.load('trainedmodel.joblib')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Location = request.form.get("Location")
        Year = request.form.get("Year")
        Kilometers_Driven = request.form.get("Kilometers_Driven")
        Fuel_Type = request.form.get("Fuel_Type")
        Transmission = request.form.get("Transmission")
        Owner_Type = request.form.get("Owner_Type")
        Mileage = request.form.get("Mileage")
        Engine = request.form.get("Engine")
        Power = request.form.get("Power")
        Seats = request.form.get("Seats")
        Price = request.form.get("Price")
        Brand = request.form.get("Brand")
        Model = request.form.get("Model")
        Car_Age = request.form.get("Car_Age")
        Has_New_Price = request.form.get("Has_New_Price")
        Price_Class = model.predict([[Location, Year, Kilometers_Driven, Fuel_Type, Transmission, Owner_Type, Mileage, Engine, Power, Seats, Price, Brand, Model, Car_Age, Has_New_Price]])
        result = Price_Class[0]
        nameslist = ['Budget','Mid','Premium','Luxury']
        ranges = {
      0: '₹0.44 Lakh – ₹3.50 Lakh (₹44,000 – ₹3,50,000)',
      1: '₹3.50 Lakh – ₹5.64 Lakh (₹3,50,000 – ₹5,64,000)',
      2: '₹5.64 Lakh – ₹9.95 Lakh (₹5,64,000 – ₹9,95,000)',
      3: '₹9.95 Lakh – ₹160 Lakh (₹9,95,000 – ₹1,60,00,000)'
    }
        result = f"{nameslist[result]} ({ranges[result]})"
        return render_template('index.html', result = result)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)