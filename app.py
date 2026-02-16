import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Déposez votre code à partir d'ici :

@app.route("/contact")
def MaPremiereAPI():
    return render_template("contact.html")


@app.get("/paris")
def api_paris():
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])

    n = min(len(times), len(temps))
    result = [
        {"datetime": times[i], "temperature_c": temps[i]}
        for i in range(n)
    ]

    return jsonify(result)

@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme")
def demographique():
    return render_template("graphique2.html")

@app.get("/humidite")
def humidite_versailles():

    # Coordonnées de Versailles
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=48.8049"
        "&longitude=2.1204"
        "&hourly=relativehumidity_2m"
    )

    response = requests.get(url)
    data = response.json()

    humidities = data.get("hourly", {}).get("relativehumidity_2m", [])

    # On prend la dernière valeur disponible
    current_humidity = humidities[-1] if humidities else 0

    return jsonify({
        "current_humidity": current_humidity
    })

@app.route("/atelier")
def atelier():
    return render_template("atelier.html")




# Ne rien mettre après ce commentaire
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
