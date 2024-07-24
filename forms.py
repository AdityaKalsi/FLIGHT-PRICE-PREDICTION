from flask_wtf import FlaskForm
from wtforms import SelectField,DateField,TimeField,IntegerField,SubmitField
from wtforms.validators import DataRequired
import pandas as pd

train = pd.read_csv('Data/train.csv')
val = pd.read_csv('Data/val.csv')

X_data = pd.concat([train,val],axis=0)

class Inputform(FlaskForm):
    airline = SelectField(
        'Airline',
        choices=X_data.airline.unique().tolist(),
        validators=[DataRequired()]
        )
    date_of_journey = DateField(
        'Date of Journey',
        validators=[DataRequired()]
    )
    source = SelectField(
        'Source',
        choices=X_data.source.unique().tolist(),
        validators=[DataRequired()]
    )
    destination = SelectField(
        'Destination',
        choices=X_data.destination.unique().tolist(),
        validators=[DataRequired()]
    )
    dep_time = TimeField(
        'Departure Time',
        validators=[DataRequired()]
    )
    arrival_time  = TimeField(
        'Arrival Time',
        validators=[DataRequired()]
    )
    duration = IntegerField(
        'Duration',
        validators=[DataRequired()]
    )
    total_stops = IntegerField(
        'Total Stops',
        validators=[DataRequired()]
    )
    additional_info = SelectField(
        'Additional Information',
        choices=X_data.additional_info.unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField('Predict')


    
