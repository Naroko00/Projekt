#!/usr/bin/env python3
from flask import Flask, request, jsonify, make_response, render_template
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

generator = {"login" : 0, "password" : 0}

class gen(Resource):
    def post(self):
        global generator
        data = request.get_json()
        generator = json.loads(data)
        print(data)

        return make_response(jsonify(data), 200)
    
api.add_resource(gen,"/api/gen")

@app.route('/')
def hello():
    global generator
    return render_template("templates/generator.html", login=generator["login"], password=generator["password"])

if __name__ == '__main__':
    app.run(host="localhost", port=8081, debug=True)
