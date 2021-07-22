from flask import Flask, request, jsonify
import requests

from flask_caching import Cache

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
cache = Cache(app)

@app.get("/univ")
@cache.cached(timeout=500, query_string=True)
def get_univ():
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get("country")
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)