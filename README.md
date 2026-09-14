# 🛡️ AI-Powered Mail Spam Detector & Analytics Dashboard

A production-ready, full-stack web application that leverages **Machine Learning (NLP)** and the **Django** framework to classify text messages as either **Spam** or **Ham** in real-time. Features an interactive administration dashboard with automated verification logs, feedback mechanisms, and on-demand model retraining capabilities.

---


## 🚀 Features
* **Real-Time Classification:** Instantly predicts message types using a trained NLP pipeline.
* **Dynamic UI Dashboard:** Clean, user-friendly interface that dynamically updates visual themes (e.g., color-coded labels for SPAM alerts).
* **Verification Logs:** Keeps a structured history log of checked text samples along with execution timestamps.
* **Model Management Controls:** Allows direct manual interventions to retrain the AI model or clear logs straight from the web view.
* **Isolated Environment:** Built within a dedicated Python virtual environment for reliable deployment.

---

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3
* **Backend:** Python, Django
* **Machine Learning:** Scikit-learn (sklearn), Pandas, Multinomial Naive Bayes (MultinomialNB), CountVectorizer
* **Database:** SQLite3 (Default Django DB)

---

## 📁 Key Project Structure
```text
Mail Spam Detector/
│
├── spamDetection/          # Project configuration directory
│   ├── settings.py         # Main project settings
│   └── urls.py             # Global URL routing
│
├── detector/               # App directory containing core logic
│   ├── templates/          # HTML web pages
│   ├── views.py            # Backend logic & ML model integration
│   ├── urls.py             # App-specific URL routing
│   └── models.py           # Database structure (if applicable)
│
├── myenv/                  # Python Virtual Environment
├── manage.py               # Django command-line utility
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally on your machine:

### 1. Prerequisites
Ensure you have Python installed on your system.

### 2. Clone or Extract the Project
Open your terminal or command prompt inside the project root directory.

### 3. Activate the Virtual Environment
Activate the pre-configured `myenv` environment:
* **Windows (Command Prompt):**
  ```bash
  myenv\Scripts\activate
  ```
* **Windows (PowerShell):**
  ```bash
  .\myenv\Scripts\Activate.ps1
  ```
* **Mac/Linux:**
  ```bash
  source myenv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations
```bash
python manage.py migrate
```

### 6. Start the Development Server
```bash
python manage.py runserver
```
Once the server starts, open your browser and navigate to: **`http://127.0.0`**

---

## 🧠 How It Works (System Architecture)
1. **User Input:** The user types a message into the frontend text area and clicks **"Check"**.
2. **HTTP POST Request:** The form data is routed securely to the backend via Django URLs.
3. **Inference (views.py):** The text is cleaned and vectorized. The pre-trained Machine Learning model processes the vector to calculate probabilities.
4. **Response Delivery:** The model outputs a prediction label (`spam` or `ham`), which Django passes back to the HTML template to dynamically render the results page.

---

## 📊 Future Enhancements

* Implement user authentication to provide individual user dashboards.
* Deploy the application live using platforms like Render, Heroku, or AWS.
