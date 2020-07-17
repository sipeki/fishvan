import bcrypt
from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_bcrypt import Bcrypt
from forms import OrdersForm, RegistrationForm, LoginForm, UpdateOrderForm
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, UserMixin
from datetime import datetime


app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# make more secure
app.config['SECRET_KEY'] = 'c076a09b61f56e9338a7c7d97244d5b0'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    address = db.Column(db.String(150), nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(500), nullable=False)



    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n',
                        'Name: ', self.f_name, ' ', self.l_name, '\r\n',
                        'Email: ', self.email, ' ', self.mobile, '\r\n',
                        'Address: ', self.address, ' ', 'Mobile: ', self.mobile

        ])

class Stock(db.Model):
    stock_id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Orderline', backref='orderid', lazy=True)

    def __repr__(self):
        return ''.join(
            [
                'Stock ID:  ' + self.stock_id + ' Detail:  ' + self.detail + ' Price: £' + self.price + '\n'
            ]
        )


class Orderline(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=1)
    fk_stock_id = db.Column(db.Integer, db.ForeignKey('stock.stock_id'), nullable=False)



    def __repr__(self):
        return ''.join(
            [
                'Order ID:  ' + self.order_id, '\r\n',
                'Order Date ' + self.order_date, '\r\n',
                'Quantity ' + self.quantity, '\r\n',
                'Status ' + self.status, '\r\n',
                'FK Stock ID: ', self.fk_stock_id, '\r\n',
                'FK User ID: ', self.fk_user_id, '\r\n'
                ]
        )


@app.route('/')
@app.route('/home')
def home():

    return render_template('homepage.html', title="FISH VAN")

@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

@app.route('/orders')
# @login_required
def orders():
    order = Orderline.query.all()
    return render_template('orders.html', title="FISH VAN - List Orders", fishvan=order)

@app.route('/orders/delete')
# @login_required
def orders_delete():
    db.session.query(Orderline).delete()
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/deleteaorder/<int:delete>', methods=["GET", "POST", "DELETE"])
# @login_required
def deleteaorder(delete):
    orderdelete = Orderline.__table__.delete().where(Orderline.order_id == delete)
    db.session.execute(orderdelete)
    db.session.commit()

    return redirect(url_for('orders'))


@app.route('/placeorder', methods=['GET', 'POST'])
# @login_required
def placeorder():
    form = OrdersForm()
    if form.validate_on_submit():
        order_data = Orderline(
            fk_stock_id=form.fk_stock_id.data,
            quantity=form.quantity.data
        )
        db.session.add(order_data)
        db.session.commit()
        return redirect(url_for('orders'))
    else:
        return render_template('placeorder.html', title='Place Order', form=form)

@app.route('/create')
def create():
    post = Stock(stock_id=1, detail="Haddock", price=1.20)
    post2 = Stock(stock_id=2, detail="Salmon", price=4.25)
    post3 = Stock(stock_id=3, detail="Fishcakes", price=1.75)
    post4 = Stock(stock_id=4, detail="Herring", price=1.00)
    post5 = Stock(stock_id=5, detail="Mackerel", price=1.50)
    post6 = Stock(stock_id=6, detail="Perch", price=2.65)
    post7 = Stock(stock_id=7, detail="Rainbow trout", price=3.40)
    post8 = Stock(stock_id=8, detail="Striped bass", price=4.50)
    post9 = Stock(stock_id=9, detail="Tuna", price=2.50)
    post10 = Stock(stock_id=10, detail="Sardines", price=0.75)
    post11 = Stock(stock_id=11, detail="Plaice", price=6.75)
    db.session.add(post)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.add(post6)
    db.session.add(post7)
    db.session.add(post8)
    db.session.add(post9)
    db.session.add(post9)
    db.session.add(post10)
    db.session.add(post11)
    db.create_all()
    db.session.commit()
    return "Some tables created"

@app.route('/delete')
def delete():
    db.drop_all()
    # db.session.query(Posts).delete()
    db.session.commit()
    return "Eveverything is gone"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(
            f_name=form.f_name.data,
            l_name=form.l_name.data,
            email=form.email.data,
            address=form.address,
            mobile=form.mobile,
            password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/updateorder/<int:update>', methods=['GET', 'POST'])
# @login_required
def updateorder(update):
    print(update)
    order = Orderline.query.filter_by(order_id=update).first()
    form = UpdateOrderForm()
    if form.validate_on_submit():
        order.fk_stock_id = form.fk_stock_id.data
        order.quantity = form.quantity.data
        db.session.commit()
        return redirect(url_for('orders'))
    elif request.method == 'GET':
        form.fk_stock_id.data = order.fk_stock_id
        form.quantity.data = order.quantity
    return render_template('updateorder.html', title='Update Order', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
