from flask import Flask, render_template, request, jsonify

import pymongo
from flask_pymongo import PyMongo
from prometheus_flask_exporter import PrometheusMetrics
from jaeger_client import Config
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor,
)
import logging

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(ConsoleSpanExporter())
)

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'App Info', version='1.0.0')

FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()


tracer = init_tracer('service')


@app.route('/')
def homepage():
    with tracer.start_span('homepage') as span:
        return "Hello World"

@app.route('/api')
def my_api():
    with tracer.start_span('my-api') as span:
        answer = "something"
        return jsonify(repsonse=answer)


@app.route('/star', methods=['POST'])
def add_star():
    with tracer.start_span('add-star') as span:
        star = mongo.db.stars
        name = request.json['name']
        distance = request.json['distance']
        star_id = star.insert({'name': name, 'distance': distance})
        new_star = star.find_one({'_id': star_id})
        output = {'name': new_star['name'], 'distance': new_star['distance']}
        return jsonify({'result': output})


if __name__ == "__main__":
    app.run()
