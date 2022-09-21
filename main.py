from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

API_KEY = "TopSecretAPIKey"

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(250), nullable=True)
    seats = db.Column(db.String(250), nullable=True)
    has_toilet = db.Column(db.Boolean, nullable=True)
    has_wifi = db.Column(db.Boolean, nullable=True)
    has_sockets = db.Column(db.Boolean, nullable=True)
    can_take_calls = db.Column(db.Boolean, nullable=True)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    all_cafes = Cafe.query.all()
    rand_cafe = random.choice(all_cafes)
    return jsonify({
        "cafe": {
            "name": rand_cafe.name,
            "map_url": rand_cafe.map_url,
            "img_url": rand_cafe.img_url,
            "location": rand_cafe.location,
            "seats": rand_cafe.seats,
            "has_toilet": rand_cafe.has_toilet,
            "has_wifi": rand_cafe.has_wifi,
            "has_sockets": rand_cafe.has_sockets,
            "can_take_calls": rand_cafe.can_take_calls,
            "coffee_price": rand_cafe.coffee_price
        }
    })


@app.route("/all")
def get_all_cafes():
    cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location.title()).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "Successfully updated the coffee price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry cafe with entered id is not found."}), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == API_KEY:
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success": "Cafe Reported closed and Removed from Database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry cafe with entered id is not found."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry access not allowed make sure you entered proper API Key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
