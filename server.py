import numpy as np
from flask import Flask, request, jsonify, render_template
import requests
from PIL import Image 
#!pip install transformer..
from transformers import ViltProcessor
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
from transformers import ViltForQuestionAnswering 
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
import torch

import base64
import json
import cv2
import numpy as np

def VQA(url, ques):
    
    image = url
    #text = "What are cats doing?"
    text = ques
    

    encoding = processor(image, text, return_tensors="pt")
    for k,v in encoding.items():
      print(k, v.shape)


    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = torch.sigmoid(logits).argmax(-1).item()
    print("Predicted answer:", model.config.id2label[idx])
    
    return model.config.id2label[idx]

def CLIP(url):
        pass


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    url = data['url']
    url = base64.b64decode(url)
    jpg_as_np = np.frombuffer(url, dtype=np.uint8)
    url = cv2.imdecode(jpg_as_np, flags=1)
    cv2.imwrite("aa.jpg",url)
    ques = data["ques"]
    
    output = VQA(url, ques)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
    

    