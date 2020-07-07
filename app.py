import Posts as Posts
from flask import Flask, redirect, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ

from forms import PostsForm
app = Flask(__name__)

# make more secure
app.config['SECRET_KEY'] = 'c076a09b61f56e9338a7c7d97244d5b0'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:CODeb9aGb0hrm9eN@35.189.67.84:3306/posts'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_PRJ_DB_NAME')

db = SQLAlchemy(app)

class Stock(db.Model):
    stock_id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return ''.join(
            [
                'Stock ID:  ' + self.stock_id + ' Detail:  ' + self.detail + ' Price: £' + self.price + '\n'
            ]
        )


class OrderLine(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    fk_stock_id = db.Column(db.Integer)
    order_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return ''.join(
            [
                'Order ID:  ' + self.order_id + ' FK Stock ID:  ' + self.fk_stock_id + ' Order Date ' + self.order_date +
                ' Quantity ' + self.quantity + ' Status ' + self.quantity + '\n'
            ]
        )

@app.route('/')
@app.route('/home')
def home():

    return render_template('homepage.html', title="FISH VAN")

@app.route('/orders')
def order():
    post_data = Posts.quert.all()
    return render_template('orders.html', title="FISH VAN - List Orders", posts=post_data)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = PostsForm()
    if form.validate_on_submit():
        post_data = Stock(
            stock_id=form.stock_id.data,
            detail=form.detail.data,
            price=form.price.data,
        )
        db.session.add(post_data)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('addstock.html', title='Add Stock', form=form)

@app.route('/create')
def create():
    db.create_all()
    post = Stock(detail='haddock', price='1.50', quantity='12')
    post2 = Stock(detail='salmon', price='2.50', quantity='6')
    db.session.add(post)
    db.session.add(post2)
    db.session.commit()
    return "Some Lovely data created"

@app.route('/delete')
def delete():
    db.drop_all()
    # db.session.query(Posts).delete()
    db.session.commit()
    return "Eveverything is gone"


if __name__ == '__main__':
    app.run()
