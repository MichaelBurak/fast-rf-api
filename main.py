# practice app for fastapi/ml model deployment with containerization to cloud/sql with python/more...
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
import numpy as np
import uuid


# open pickled RandomForestClassifier model from sklearn trained on Iris dataset
with open("rf.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# main app
app = FastAPI()

origins = ["http://localhost:8080", "https://iris-classifier-client.netlify.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
)

# blank root route
@app.get("/")
async def hello_world():
    return {"Nothing to see here!"}


@app.get("/predict")
async def predict_iris(
    s_length: float, s_width: float, p_length: float, p_width: float
) -> str:

    # sklearn wants an np ndarray for prediction data so converting url params
    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))

    # return prediction value of class to user as string
    return str(prediction)
