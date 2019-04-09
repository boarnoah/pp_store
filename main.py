from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ppdb:swordfish@ppdbmysql.ct4sai8mxgm9.us-east-2.rds.amazonaws.com:3306/ppdb'
db = SQLAlchemy(app)


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return 'Pizza, id: {}, name: {}'.format(self.id, self.name)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey(Pizza.id), nullable=False)

# ex: how to add entries to db
# foo = Order(name='I C Wiener', address="1 Yonge St", pizza_id=pizzas[0].id)
#
# db.session.add(foo)
# db.session.commit()
    
@app.route('/')
def index():
    pizzas = Pizza.query.all()
    return render_template('index.html', pizzas=pizzas) #Renders template, with list queried from db

if __name__ == '__main__':
    print("wololo")
    app.run(port=8080, debug=True)
