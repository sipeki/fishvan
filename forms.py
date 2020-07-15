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
    f_name = StringField('First Name',
                             validators=[
                                 DataRequired(),
                                 Length(min=2, max=30)
                             ])
    l_name = StringField('Last Name',
                validators=[
                    DataRequired(),
                    Length(min=3, max=30)
                ])
    email = StringField('Email',
                validators = [
                DataRequired(),
                Email()
                ])
    address = StringField('Address',
                validators=[
                DataRequired(),
                Length(min=1, max=150)
                ])
    mobile = IntegerField(
        'Mobile Number',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=99999999999)

        ]

    )
    password = PasswordField('Password',
                validators = [
                DataRequired()
                ])
    confirm_password = PasswordField('Confirm Password',
                validators = [
                DataRequired(),
                EqualTo('password')
                ])
    submit = SubmitField('Sign Up')


class OrdersForm(FlaskForm):
    fk_stock_id = IntegerField(
        'FK Stock ID (max 9999)',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=9999)

        ]

    )

    quantity = IntegerField(
        'Quantity (max 99)',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=99)

        ]

    )

    submit = SubmitField('Place a order')


class UpdateOrdersForm(FlaskForm):
    fk_stock_id = IntegerField(
        'FK Stock ID (max 9999)',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=9999)

        ]

    )

    quantity = IntegerField(
        'Quantity (max 99)',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=99)

        ]

    )

    submit = SubmitField('Update')


