from email.policy import strict
from flask import Flask
import json
from flask import Flask, request, jsonify

from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
from datetime import datetime
import re
import date as m
from flask_restful import Resource, Api, reqparse
import werkzeug
import cv2
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
todo = dict()
image_file = None


class HelloWorldforEye(Resource):
    def get(self):
       # result=m.mymain()
        global image_file
        result = m.ismain(image_file)
        return jsonify({'name': str(result['name']),
                        'age': str(result['age']),
                        'gender': str(result['gender'])})

    def post(self):
        result = m.mymain()

        # result=m.ismain(image_file)
        return jsonify({'date': result})


api.add_resource(HelloWorldforEye, '/date')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5005, debug=True)
