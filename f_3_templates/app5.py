from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    top_20_cars = [
    "Chevrolet Corvette E-Ray", "Ford Mustang", "Hyundai Kona", "Hyundai Santa Fe", 
    "Kia EV9", "Lexus GX", "Lincoln Nautilus", "Subaru Crosstrek", "Porsche 911", 
    "Toyota Prius", "Mercedes-Benz E-Class", "BMW 5 Series", "Audi Q8 e-tron", 
    "Genesis G90", "Honda Accord", "Volkswagen GTI", "Mazda MX-5 Miata", 
    "Nissan Ariya", "Jeep Grand Cherokee", "Tesla Model Y"
]
    return render_template ('index5.html', cars = top_20_cars )
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
