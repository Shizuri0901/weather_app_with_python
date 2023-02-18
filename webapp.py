from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# API endpoint and key
url = "https://api.weatherapi.com/v1/current.json"
key = "fce8ddc021304141954102239231302"

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/weather")
def weather():
    location = request.args.get("location")
    params = {"key": key, "q": location}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        location_name = data["location"]["name"]+','+data["location"]["country"]
        condition = data["current"]["condition"]["text"]
        temp_c = data["current"]["temp_c"]
        temp_f = data["current"]["temp_f"]
        feelslike_c = data["current"]["feelslike_c"]
        feelslike_f = data["current"]["feelslike_f"]
        humidity = data["current"]["humidity"]
        uv = data["current"]["uv"]
        img = data["current"]["condition"]["icon"]
        return render_template("/index.html",
                               location_name=location_name,
                               condition=condition,
                               temp_c=temp_c, temp_f=temp_f,
                               feelslike_c=feelslike_c, feelslike_f=feelslike_f,
                               humidity=humidity,
                               uv=uv,
                               img=img)
    else:
        error = f"Error: {response.status_code} - {response.text}"
        return render_template("error.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)