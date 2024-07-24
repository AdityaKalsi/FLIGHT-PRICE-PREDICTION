from flask import Flask,render_template,url_for
from forms import Inputform
import pandas as pd
import joblib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KEY'

model = joblib.load('model.joblib')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title = 'Home')

@app.route('/predict',methods = ['GET','POST'])
def predict():
    form = Inputform()
    if form.validate_on_submit():
        input = pd.DataFrame(dict(
            airline = [form.airline.data],
            date_of_journey = [form.date_of_journey.data],
            source = [form.source.data],
            destination = [form.destination.data],
            dep_time = [form.dep_time.data],
            arrival_time = [form.arrival_time.data],
            duration = [form.duration.data],
            total_stops = [form.total_stops.data],
            additional_info = [form.additional_info.data],
        ))
        predicted_price = model.predict(input)[0]
        message = f"The predicted price is {predicted_price:.0f} INR"
    else:
        message = "Enter Valid Inputs"
    return render_template('predict.html',title = 'predict',form = form,message = message)

if __name__ == '__main__':
    app.run(debug=True)
