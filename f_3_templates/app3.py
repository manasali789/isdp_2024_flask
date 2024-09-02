from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    # Array to be passed to the template
    myarray = ['Apple', 'Banana', 'Cherry', 'Date', 'Mango']
    return render_template('index3.html', fruits=myarray)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
