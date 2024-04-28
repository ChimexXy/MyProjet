from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/T-shirt')
def Tshirt():
    return render_template('T-shirt.html')

if __name__== '__main__':
    app.run(debug=True)
