from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')


class OrdersForm(FlaskForm):
    fk_stock_id = IntegerField(
        'FK Stock ID (max 9999)',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=9999)

        ]

    )


    order_date = DateField(
        'Order Date',
        default=date.today
    )

    quantity = IntegerField(
        'Quantity (max 99)',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=99)

        ]

    )

    status = IntegerField(
        'Status (0 to 4)',
        validators=[
            DataRequired(),
            NumberRange(min=0, max=4)

        ]

    )
    submit = SubmitField('Place a order')

