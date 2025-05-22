# ❤️ Heart Disease Risk Predictor

A lightweight machine learning web app that predicts the 10-year risk of heart disease based on key health metrics. Built using Python, scikit-learn, and Streamlit.

---

## 🚀 Live App
Try it here: [https://heart-risk-predictor.streamlit.app/](https://heart-risk-predictor.streamlit.app/)

---

## 🧠 How It Works
- Users input their age, gender, blood pressure, cholesterol, smoking habits, and other health data
- A Logistic Regression model (trained on real-world data) predicts heart disease risk
- Outputs include a clear prediction and a confidence score (probability %)

---

## 🧰 Tech Stack
- Python 3.10+
- pandas
- scikit-learn
- joblib
- Streamlit

---

## 🗂️ Project Structure
```
heart-risk-predictor/
├── data/                  # Contains CSV dataset
├── models/                # Saved ML model (.pkl)
├── src/                   # Modular Python scripts
│   ├── data_loader.py
│   ├── train_model.py
│   └── predict.py
├── streamlit_app.py       # Main app frontend
├── requirements.txt       # Dependencies
└── README.md
```

---

## 📦 Setup Instructions
```bash
# Clone the repo
git clone https://github.com/aaditnair97/heart-risk-predictor.git

# Navigate into the project
cd heart-risk-predictor

# (Optional) create and activate virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app locally
streamlit run streamlit_app.py
```

---

## ⚠️ Disclaimer
> This app is a personal learning project and **not a substitute for professional medical advice.** Please consult a doctor for health concerns.

---

## 👨‍💻 Author
**Aadit Sabareesh Nair**  
Develops safety-critical systems at Rolls-Royce. Passionate about Python, AI, and building real-world ML tools.

[LinkedIn →](https://www.linkedin.com/in/aadit-sabareesh-nair/)