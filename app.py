import bcrypt
from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_bcrypt import Bcrypt
from forms import OrdersForm, RegistrationForm
from flask_login import LoginManager
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, UserMixin
from datetime import datetime


app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

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


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])

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


class Orderline(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    fk_stock_id = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return ''.join(
            [
                'Order ID:  ' + self.order_id + ' FK Stock ID:  ' + self.fk_stock_id + ' Order Date ' + self.order_date +
                ' Quantity ' + self.quantity + ' Status ' + self.status + '\n'
            ]
        )



@app.route('/home')
def home():

    return render_template('homepage.html', title="FISH VAN")

@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

@app.route('/orders')
def orders():
    order_data = Orderline.query.all()
    return render_template('orders.html', title="FISH VAN - List Orders", fishvan=order_data)


@app.route('/placeorder', methods=['GET', 'POST'])
def placeorder():
    form = OrdersForm()
    if form.validate_on_submit():
        order_data = Orderline(
            fk_stock_id=form.fk_stock_id.data,
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

        user = Users(email=form.email.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run()
