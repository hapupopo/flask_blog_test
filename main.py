from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, TimeField, SelectField, DateTimeField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

coffee_rating = ["☕", "☕☕", "☕☕☕","☕☕☕☕","☕☕☕☕☕", "✘"]
wifi_rating = ["💪", "💪💪", "💪💪💪","💪💪💪💪","💪💪💪💪💪", "✘"]
power_rating = ["🔌", "🔌🔌", "🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌", "✘"]
message_empty = "필수 입력 값입니다."
message_time = "제대로된 시간을 입력하세요. HH:MM 형식입니다."
message_url = "제대로된 URL을 입력하세요."

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message=message_empty)])
    location = StringField('Location', validators=[DataRequired(message=message_empty), URL(message=message_url)])
    open_time = TimeField('Open',validators=[DataRequired(message=message_time)])
    closing_time = TimeField('Close', validators=[DataRequired(message=message_time)])
    coffee_rating = SelectField('Coffee', validators=[DataRequired(message=message_empty)], choices=coffee_rating)
    wifi_rating = SelectField('Wifi', validators=[DataRequired(message=message_empty)], choices=wifi_rating)
    power_outlet_rating = SelectField('Power', validators=[DataRequired(message=message_empty)], choices=power_rating)
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', "a", newline='') as csv_file:
            new_csv_data = [form.cafe.data, form.location.data, form.open_time.data, form.closing_time.data,
                            form.coffee_rating.data, form.wifi_rating.data, form.power_outlet_rating.data]
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(new_csv_data)
        return redirect(url_for('cafes'))
    # Exercise:

    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
