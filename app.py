import torch
import whisper
import os
import base64
from io import BytesIO

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global pipe
    
    pipe = whisper.load_model("base")

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global pipe
    s = os.getenv("BA","not present")
    o = os.getenv("BB","not present 2")
    
    output = {"reply":"new model updated again hoora"}
    
    # Return the results as a dictionary
    return output
