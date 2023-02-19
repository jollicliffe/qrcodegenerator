from flask import Flask, json, request, render_template
import cv2
from cvtest import memegen



api = Flask(__name__)

@api.route('/')
def home():
    return render_template('index.html')


@api.route('/images', methods=['GET'])
def imageapi():
    image = 'static/new.png'
    serial = request.args.get('serial')
    model = request.args.get('model')
    newImage = memegen(image, serial, model)
    return '<img src="{}" />'.format(image)
    

if __name__ == '__main__':
    api.run()
