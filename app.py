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
    fk_stock_id = db.Column(db.Integer, nullable=False)
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
        order_data = OrderLine(
            fk_stock_id=form.fk_order_id,
            order_date=form.order_date.data,
            quantity=form.quantity.data,
            status=form.status.data,
        )
        db.session.add(order_data)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('placeorder.html', title='Place Order', form=form)

@app.route('/create')
def create():
    db.create_all()
    post = OrderLine(fk_stock_id='1234', order_date='7/7/202', quantity=2, status=1)
    post2 = OrderLine(fk_stock_id='9233', order_date='7/7/202', quantity=4, status=1)
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
