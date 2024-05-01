from flask import Flask, render_template
from data import Posts

app = Flask(__name__)
Posts = Posts()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/T-shirt')
def Tshirt():
    return render_template('T-shirt.html')

@app.route('/Sweats')
def Sweats():
    return render_template('Sweats.html')

@app.route('/Your DTF')
def yourdtf():
    return render_template('dtf.html', posts = Posts)

@app.route('/page')
def page():
    return render_template('page.html')

@app.route('/posts/<string:id>/')
def posts(id):
    return render_template('post.html',id=id)

if __name__== '__main__':
    app.run(debug=True)
