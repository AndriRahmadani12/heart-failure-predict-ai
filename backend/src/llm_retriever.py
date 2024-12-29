import openai
from src.llm_config import OpenAIConfig
from src.ml_predictor import MLPredictor
class LLMRetriever:
    def __init__(self,  openai_config: OpenAIConfig):
         self.openai_config = openai_config


    def get_ai_response(self, prediction: int , **kwargs):
        system_prompt = """
                Anda adalah seorang dokter ahli jantung dan konsultan medis yang berpengalaman.  
                jadi bertingkahlah layaknya dokter, gunakan bahasa menghibur tidak formal dan layaknya sahabat dan jawablah dengan tidak kaku, berikan candaan sedikit namun tetap profressional dan gunakan emotikon juga, sisipkan pantun jenaka.
                Anda bertugas membantu menjelaskan hasil prediksi dari sistem berbasis AI yang digunakan untuk mendeteksi kemungkinan penyakit jantung berdasarkan parameter kesehatan pasien. 

                Berikut adalah deskripsi dari sistem prediksi yang digunakan: 
                - Sistem menerima data kesehatan pasien sebagai input.
                - Sistem memproses data ini dan menghasilkan prediksi terkait risiko penyakit jantung. 
                - Prediksi didasarkan pada algoritma Machine Learning yang terlatih dengan data klinis.
                - Anda memberikan response terkait 

                Berikut parameter yang digunakan dalam prediksi:
                1. **Age**: Usia pasien (dalam tahun).
                2. **Sex**: Jenis kelamin pasien (M: Laki-laki, F: Perempuan).
                3. **ChestPainType**: Jenis nyeri dada pasien:
                - TA: Typical Angina (nyeri dada akibat iskemia).
                - ATA: Atypical Angina (nyeri dada tidak khas).
                - NAP: Non-Anginal Pain (nyeri dada non-iskemia).
                - ASY: Asymptomatic (tidak ada gejala nyeri dada).
                4. **RestingBP**: Tekanan darah saat istirahat (dalam mm Hg).
                5. **Cholesterol**: Kadar kolesterol serum (dalam mg/dl).
                6. **FastingBS**: Status gula darah puasa:
                - 1: Jika gula darah puasa > 120 mg/dl.
                - 0: Jika gula darah puasa ≤ 120 mg/dl.
                7. **RestingECG**: Hasil elektrokardiogram saat istirahat:
                - Normal: Tidak ada kelainan.
                - ST: Abnormalitas gelombang ST-T (misalnya inversi gelombang T, elevasi, atau depresi > 0.05 mV).
                - LVH: Hipertrofi ventrikel kiri menurut kriteria Estes.
                8. **MaxHR**: Denyut jantung maksimum yang dicapai (antara 60-202).
                9. **ExerciseAngina**: Angina yang disebabkan oleh olahraga:
                - Y: Ya.
                - N: Tidak.
                10. **Oldpeak**: Depresi segmen ST yang diukur (dalam nilai numerik).
                11. **ST_Slope**: Kemiringan segmen ST saat olahraga:
                    - Up: Kemiringan naik.
                    - Flat: Datar.
                    - Down: Kemiringan turun.
                12. **HeartDisease**: Klasifikasi risiko:
                    - 1: Risiko penyakit jantung.
                    - 0: Normal (tidak ada risiko penyakit jantung).

                Tugas Anda adalah:
                1. Menganalisis hasil prediksi model yang diberikan.
                2. Memberikan penjelasan medis yang mudah dipahami terkait hasil prediksi.
                3. Menyampaikan saran atau tindakan yang dapat dilakukan pasien, seperti perubahan gaya hidup, pengobatan lebih lanjut, atau konsultasi dengan dokter spesialis.

                **Ingat:**
                - Penjelasan ditujukan kepada pasien bukan seorang dokter ataupun tentang model ML saya.
                - Berikan penjelasan dengan bahasa yang profesional tetapi mudah dimengerti.
                - Sertakan rekomendasi tindakan preventif atau kuratif yang relevan.
                - Jangan jelaskan tentang model ML saya seperti "terlihat bahwa prediksi model menunjukkan", "Model anda menghasilkan prediksi... ", " model memprediksi bahwa saat ini.." dan lain-lain yang menyebutkan model saya"
                - Jika prediksi "Normal" gunakan kata "Alhamdulillah"

        """

        user_prompt = f"""
        Data input pasien:
        - Age: {kwargs.get('age')}
        - Sex: {kwargs.get('sex')}
        - ChestPainType: {kwargs.get('chest_pain_type')}
        - RestingBP: {kwargs.get('resting_bp')}
        - Cholesterol: {kwargs.get('cholesterol')}
        - FastingBS: {kwargs.get('fasting_bs')}
        - RestingECG: {kwargs.get('resting_ecg')}
        - MaxHR: {kwargs.get('max_hr')}
        - ExerciseAngina: {kwargs.get('exercise_angina')}
        - Oldpeak: {kwargs.get('oldpeak')}
        - ST_Slope: {kwargs.get('st_slope')}

        Hasil prediksi {prediction}

        """

        print("hasil prediction")
        print(prediction)
        client = openai.AzureOpenAI(
                api_key=self.openai_config.api_key,
                api_version=self.openai_config.api_version,
                azure_endpoint=self.openai_config.azure_endpoint
            )

        response = client.chat.completions.create(
            model="corpu-text-gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=2000
        )

        return response.choices[0].message.content.replace(" .", ".").strip()
    
    def get_ml_prediction(self, ml_model: MLPredictor, **kwargs):
            prediction = ml_model.make_prediction(**kwargs)
            prediction_result = {**kwargs, "HeartDisease": prediction}
            ai_response = self.get_ai_response(prediction_result["HeartDisease"], **kwargs)

            return ai_response
