## ✅ `README.md` (English version)

````markdown
# Student Depression Prediction 🎓🧠

This project is a Flask web application that uses a trained Machine Learning model (Logistic Regression) to predict **signs of depression** based on students' academic and behavioral data.

---

## 🚀 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-user/backend-depression.git
cd backend-depression
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate   # On Windows
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask server

```bash
python app.py
```

Then open in your browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 AI Model

* Trained using `LogisticRegression` from `scikit-learn`
* Input features used:

  * Suicidal Thoughts
  * Financial Stress
  * Academic Pressure
  * Sleep Duration
  * Family History of Mental Illness
  * CGPA
  * Study Satisfaction
  * Work/Study Hours
  * Dietary Habits
  * Age

---

## 📡 API Documentation

### `POST /prever`

Sends a student's data to the server for prediction.

#### 🔸 Request (JSON):

```json
{
  "thoughts": 1,
  "financial": 3,
  "academic": 4,
  "sleep": 2,
  "family": 0,
  "cgpa": 7.8,
  "satisfaction": 3,
  "hours": 2,
  "diet": "Healthy",
  "age": 21
}
```

#### 🔸 Response (JSON):

```json
{
  "resultado": "No signs of depression",
  "probabilidade": 86.42
}
```

---

## 📁 Project Structure

```
backend_depression/
│
├── app.py
├── modelo/
│   └── modelo_depressao.pkl
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md
```

---

## 🛠 Technologies

* Python 3.11
* Flask
* Scikit-learn
* HTML + CSS

