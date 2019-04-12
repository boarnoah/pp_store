from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from sqlalchemy import exc as SQLAlchemyException

import secrets

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://ppdb:swordfish@ppdbmysql.ct4sai8mxgm9.us-east-2.rds.amazonaws.com:3306/ppdb'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = secrets.token_bytes(32)
app.config['WTF_CSRF_SECRET_KEY'] = secrets.token_bytes(32)

csrf = CSRFProtect(app)

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    short_desc = db.Column(db.String(80), unique=False, nullable=False)
    long_desc = db.Column(db.String(280), unique=False, nullable=False)
    img = db.Column(db.String(280), unique=False, nullable=False)

    def __repr__(self):
        return 'Pizza, id: {}, name: {}, price: {}'.format(self.id, self.name, self.price)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey(Pizza.id), nullable=False)
    pizza_count = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return 'Order, id: {}, name: {}, address: {}. Pizza: {}, count: {}'.format(self.id, self.name, self.price,
                                                                                   self.pizza_id, self.pizza_count)


class OrderForm(FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    pizza_count = IntegerField('pizza_count', validators=[DataRequired(), NumberRange(min=1, max=20)])


# ex: how to add entries to db
# foo = Order(name='I C Wiener', address="1 Yonge St", pizza_id=pizzas[0].id)
#
# db.session.add(foo)
# db.session.commit()

@app.route('/')
def index():
    try:
        pizzas = Pizza.query.all()
    except SQLAlchemyException.OperationalError:
        pizzas = []

    return render_template('index.html', pizzas=pizzas)  # Renders template, with list queried from db


@app.route('/pizza/<pizza_id>', methods=['GET', 'POST'])
def pizza(pizza_id):
    pizza = Pizza.query.filter_by(id=pizza_id).first()
    form = OrderForm(request.form)

    if form.validate_on_submit():
        new_order = Order(name=form.user_name.data, address=form.address.data, pizza_id=pizza_id,
                          pizza_count=form.pizza_count.data)

        if new_order:
            db.session.add(new_order)
            db.session.commit()

        return redirect('/success')

    if pizza:
        return render_template('pizza.html', pizza=pizza, form=form)
    else:
        return render_template("404.html")


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/success')
def success():
    return render_template('success.html')


@app.route("/ssh")
def inside_joke():
    return render_template('inside_joke.html')


if __name__ == '__main__':
    print("wololo")
    app.run(port=8080, debug=True)
    # Note requires a run before it saves db (possibly only an issue with sqlite)
    # Doesn't update with schema changes so watchout for that
    db.create_all()
