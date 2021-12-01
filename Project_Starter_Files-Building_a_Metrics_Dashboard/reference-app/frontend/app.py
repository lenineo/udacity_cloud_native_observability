from flask import Flask, render_template, request,jsonify, json, render_template
from prometheus_flask_exporter import PrometheusMetrics
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")
app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info("app_info", "App Info", version="1.0.0")

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/error')
def error():
    return "error 500", 500

@app.route('/healthz')
def health_check():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
        )
    return response

if __name__ == "__main__":
    app.run()