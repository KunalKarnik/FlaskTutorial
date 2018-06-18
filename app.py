from flask import Flask, render_template
from dummyArticles import Articles

Articles = Articles()

app = Flask(__name__)
#app.debug = True

@app.route('/test')
def test():
    return 'INDEX-test'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/wall')
def wall():
    return render_template('wall.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    idno = int(id)-1
    return render_template('article.html', article = Articles[idno])

if __name__ == '__main__':
    app.run(debug=True)