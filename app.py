import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import JSONResponse

app = FastAPI()


class Wine(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315: float
    proline: float


# Загрузка модели
model = joblib.load('wine_model.joblib')


@app.post('/predict')
def predict(wine: Wine):
    features = np.array([
        wine.alcohol,
        wine.malic_acid,
        wine.ash,
        wine.alcalinity_of_ash,
        wine.magnesium,
        wine.total_phenols,
        wine.flavanoids,
        wine.nonflavanoid_phenols,
        wine.proanthocyanins,
        wine.color_intensity,
        wine.hue,
        wine.od280_od315,
        wine.proline
    ]).reshape(1, -1)
    prediction = model.predict(features).tolist()
    print(prediction)
    return JSONResponse(content={'class': prediction[0]})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)