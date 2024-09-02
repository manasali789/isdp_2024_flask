from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = 'welcome'
    myresult = 10 + 20
    result = 20 *3
    xyz = 'Python'
    name = 'anas'
    return render_template('index2.html', myvalue=myvalue, myresult=myresult, course= xyz, name = name, result = result )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
