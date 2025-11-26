from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet import preprocess_input
import numpy as np, os
from PIL import Image

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model_blood_group_detection_resnet.h5")
model = load_model(MODEL_PATH)

labels = {0:"A+",1:"A-",2:"B+",3:"B-",4:"AB+",5:"AB-",6:"O+",7:"O-"}

def prepare_image(img):
    img = img.resize((256,256))
    arr = image.img_to_array(img)
    arr = np.expand_dims(arr, axis=0)
    return preprocess_input(arr)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error':'No image uploaded'}),400
    results=[]
    for f in request.files.getlist('file'):
        img=Image.open(f.stream).convert('RGB')
        arr=prepare_image(img)
        pred=model.predict(arr)
        idx=int(np.argmax(pred,axis=1)[0])
        results.append(labels.get(idx,'Unknown'))
    return jsonify({'predictions':results})

if __name__=="__main__":
    app.run(debug=True)
