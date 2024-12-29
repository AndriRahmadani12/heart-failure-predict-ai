from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from typing import Dict
from src.llm_config import openai_config
from src.ml_predictor import MLPredictor
from src.llm_retriever import LLMRetriever
from src.schemas import PatientData
app = FastAPI()



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("HeartDiseasePrediction")

# Path model dan encoder
model_path = 'ml_model/random_forest_model.pkl'
encoder_paths = {
    'sex': 'ml_model/label_encoder_sex.pkl',
    'chest_pain_type': 'ml_model/label_encoder_chest_pain_type.pkl',
    'resting_ecg': 'ml_model/label_encoder_rasting_ecg.pkl',
    'exercise_angina': 'ml_model/label_encoder_exercise_angina.pkl',
    'st_slope': 'ml_model/label_encoder_st_slope.pkl'
}

try:
    ml_predictor = MLPredictor(model_path, encoder_paths)
    llm_retriever = LLMRetriever(openai_config)
except Exception as e:
    logger.error("Gagal memuat model atau encoder: %s", str(e))
    raise RuntimeError("Gagal memuat model atau konfigurasi awal")

@app.post("/predict")
async def predict(patient_data: PatientData):
    """Endpoint untuk prediksi penyakit jantung dan analisis tambahan."""
    try:
        prediction = ml_predictor.make_prediction(**patient_data.dict())
        logger.info(f"Hasil prediksi: {prediction}")

        # Analisis dari LLM
        ai_response = llm_retriever.get_ml_prediction(ml_predictor, **patient_data.dict())
        logger.info("Respons AI:")
        logger.info(ai_response)

        if prediction == 1:
            prediction = "Resiko Penyakit Jantung"
        else:
            prediction = "Normal"

        return {
            "params":patient_data.dict(),
            "prediction": prediction,
            "ai_analysis": ai_response
        }

    except Exception as e:
        logger.error("Error saat memproses data: %s", str(e))
        raise HTTPException(status_code=500, detail=str(e))
