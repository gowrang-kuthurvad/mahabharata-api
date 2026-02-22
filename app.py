from flask import Flask, jsonify, request

app = Flask(__name__)

# ---------------- DATA ---------------- #
characters = [
    {
        "name": "Krishna",
        "role": "Guide of Pandavas",
        "kingdom": "Dwarka",
        "description": "Avatar of Vishnu, strategist of Mahabharata"
    },
    {
        "name": "Arjuna",
        "role": "Pandava Prince",
        "kingdom": "Indraprastha",
        "description": "Great archer and warrior"
    },
    {
        "name": "Karna",
        "role": "Warrior of Kauravas",
        "kingdom": "Anga",
        "description": "Son of Kunti, loyal to Duryodhana"
    }
]

places = [
    {"name": "Hastinapura", "type": "Capital of Kauravas"},
    {"name": "Indraprastha", "type": "Capital of Pandavas"},
    {"name": "Kurukshetra", "type": "Battlefield"}
]

events = [
    {"event": "Dice Game", "description": "Pandavas lose kingdom"},
    {"event": "Exile", "description": "Pandavas go to forest for 13 years"},
    {"event": "Kurukshetra War", "description": "18-day great war"}
]

# ---------------- ROUTES ---------------- #

@app.route("/")
def home():
    return jsonify({
        "message": "Mahabharata API Tool Running",
        "routes": [
            "/characters",
            "/places",
            "/events",
            "/search?name=krishna"
        ]
    })

@app.route("/characters")
def get_characters():
    return jsonify(characters)

@app.route("/places")
def get_places():
    return jsonify(places)

@app.route("/events")
def get_events():
    return jsonify(events)

@app.route("/search")
def search():
    name = request.args.get("name", "").lower()
    results = []
    for c in characters:
        if name in c["name"].lower():
            results.append(c)
    return jsonify(results)


# ---------------- RUN ---------------- #
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
