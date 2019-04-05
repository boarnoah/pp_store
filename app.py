from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:swordfish@localhost:5432/postgres'
db = SQLAlchemy(app)


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'Pizza, id: {self.id}, name: {self.name}'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey(Pizza.id), nullable=False)


@app.route('/')
def index():
    # pizzas = Pizza.query.all()
    # foo = Order(name='I C Wiener', address="1 Yonge St", pizza_id=pizzas[0].id)
    #
    # db.session.add(foo)
    # db.session.commit()

    return render_template('index.html', pizzas=Pizza.query.all())

if __name__ == '__main__':
    print("wololo")
    app.run(port=8080, debug=True)