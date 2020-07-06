from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('homepage.html', title="FISH VAN")

@app.route('/orders')
def aboutus():
    return render_template('orders.html', title="FISH VAN - List Orders")


if __name__ == '__main__':
    app.run()
