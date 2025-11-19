# 📱 Expresso Customer Churn Prediction App

This project is a **Streamlit web application** that predicts whether a telecom customer is likely to **churn (leave the service)** based on their behavioral usage data. The app uses a trained Machine Learning model and a scaler to make predictions.

---

## 🚀 Features

✔ Easy-to-use web interface
✔ Accepts customer feature inputs
✔ Scales input data using the saved scaler
✔ Loads a trained machine learning model (`expresso_churn_model.pkl`)
✔ Displays prediction results instantly

---

## 📂 Project Structure

```
expresso_churn/
│
├── app.py                       # Streamlit application
├── expresso_churn_model.pkl     # Trained ML model
├── scaler.pkl                   # Scaler used during training
└── README.md                    # Project documentation
```

---

## 🛠 Requirements

Before running the application, you need to install the required dependencies.

### Install dependencies

```
pip install streamlit pandas joblib scikit-learn
```

---

## ▶ Run the Streamlit App

Open Command Prompt in your project folder and run:

```
python -m streamlit run app.py
```

> ⚠ If the `streamlit` command does not work, always use:

```
python -m streamlit run app.py
```

---

## 🧠 How It Works

1. The user enters customer information (e.g., TENURE, REVENUE, DATA_VOLUME, ON_NET, etc.)
2. The input data is converted into a pandas DataFrame
3. The scaler normalizes the input to match model training conditions
4. The trained model predicts customer churn
5. The app displays one of two messages:

| Prediction | Message                        |
| ---------- | ------------------------------ |
| 1          | ⚠️ Customer is likely to churn |
| 0          | ✅ Customer is likely to stay   |

---

## 📋 Input Features Used

| Feature        | Meaning                        |
| -------------- | ------------------------------ |
| REGION         | Geographical zone              |
| TENURE         | Customer subscription duration |
| MONTANT        | Recharge amount                |
| FREQUENCE_RECH | Recharge frequency             |
| REVENUE        | Total revenue                  |
| ARPU_SEGMENT   | Average revenue per user       |
| FREQUENCE      | Call frequency                 |
| DATA_VOLUME    | Data usage                     |
| ON_NET         | Calls within same network      |
| ORANGE         | Calls to Orange network        |
| TIGO           | Calls to TIGO network          |
| ZONE1          | Zone indicator                 |
| ZONE2          | Zone indicator                 |
| MRG            | Marital status code            |
| REGULARITY     | Activity consistency           |
| TOP_PACK       | Customer package               |
| FREQ_TOP_PACK  | Frequency of package purchase  |

> ⚠ The app assumes these features match the exact model training order.

---

## 💡 Tips for Better Accuracy

🔹 Always use the **same scaler** used during model training
🔹 Do not retrain the model without updating the app input features
🔹 Ensure `expresso_churn_model.pkl` and `scaler.pkl` are in the **same folder** as `app.py`

---

## 🌍 Optional Deployment

You can deploy the application online using **Streamlit Cloud**:

1. Create a GitHub repository
2. Upload:

   * `app.py`
   * `expresso_churn_model.pkl`
   * `scaler.pkl`
   * `requirements.txt`
3. Go to [https://share.streamlit.io](https://share.streamlit.io)
4. Deploy your repository

---

## 👨‍💻 Author

Built by **[Your Name]**
For learning, testing, and research purposes — feel free to improve or extend the app!

