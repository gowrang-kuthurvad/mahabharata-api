from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open("data/characters.json","r",encoding="utf-8") as f:
    characters=json.load(f)
with open("data/places.json","r",encoding="utf-8") as f:
    places=json.load(f)
with open("data/events.json","r",encoding="utf-8") as f:
    events=json.load(f)

@app.route("/")
def home():
    return jsonify({"message":"Mahabharata API Running"})

@app.route("/characters")
def get_characters(): return jsonify(characters)

@app.route("/places")
def get_places(): return jsonify(places)

@app.route("/events")
def get_events(): return jsonify(events)

@app.route("/search")
def search():
    name=request.args.get("name","").lower()
    result=[c for c in characters if name in c["name"].lower()]
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
