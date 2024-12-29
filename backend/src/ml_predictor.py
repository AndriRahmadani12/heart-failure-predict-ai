import pickle
import logging
import numpy as np
import pandas as pd

class MLPredictor:
    def __init__(self, model_path, encoder_paths):
        self.model_path = model_path
        self.encoder_paths = encoder_paths
        self.model = self._load_model()
        self.encoders = self._load_encoders()

    def _load_model(self):
        with open(self.model_path, 'rb') as file:
            model = pickle.load(file)
        return model

    def _load_encoders(self):
        encoders = {}
        for feature, path in self.encoder_paths.items():
            with open(path, 'rb') as file:
                encoders[feature] = pickle.load(file)
        return encoders

    def _preprocessing_data(self, age, sex, chest_pain_type, resting_bp, cholesterol,
                            fasting_bs, resting_ecg, max_hr, exercise_angina,
                            oldpeak, st_slope):
        encoded_sex = self.encoders['sex'].transform([sex])[0]
        encoded_chest_pain_type = self.encoders['chest_pain_type'].transform([chest_pain_type])[0]
        encoded_resting_ecg = self.encoders['resting_ecg'].transform([resting_ecg])[0]
        encoded_exercise_angina = self.encoders['exercise_angina'].transform([exercise_angina])[0]
        encoded_st_slope = self.encoders['st_slope'].transform([st_slope])[0]

        features = np.array([age, encoded_sex, encoded_chest_pain_type, resting_bp, cholesterol, fasting_bs,
                             encoded_resting_ecg, max_hr, encoded_exercise_angina, oldpeak, encoded_st_slope])

        return features.reshape(1, -1)

    def make_prediction(self, age, sex, chest_pain_type, resting_bp, cholesterol,
                         fasting_bs, resting_ecg, max_hr, exercise_angina,
                         oldpeak, st_slope):
        data = self._preprocessing_data(age, sex, chest_pain_type, resting_bp, cholesterol,
                                        fasting_bs, resting_ecg, max_hr, exercise_angina,
                                        oldpeak, st_slope)
        prediction = self.model.predict(data)
        return int(prediction[0])