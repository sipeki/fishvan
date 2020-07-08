from datetime import date

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange
from wtforms.validators import ValidationError
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.fields.html5 import DateTimeField

class  OrdersForm(FlaskForm):
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