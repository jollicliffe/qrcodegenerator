from flask import Flask, json, request, render_template
import cv2
from cvtest import memegen

#companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]


api = Flask(__name__)

@api.route('/')
def home():
    return render_template('index.html')


@api.route('/images', methods=['GET'])
def get_companies():
    image = 'static/new.png'
    text = request.args.get('text')
    newImage = memegen(image, text)
    return '<img src="{}" />'.format(image)
    

if __name__ == '__main__':
    api.run()
