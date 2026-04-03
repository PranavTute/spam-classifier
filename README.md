# spam-classifier

# 📩 Spam Message Classifier

An AI-powered web app that detects whether a message is **Spam** or **Not Spam** using Machine Learning.

---

## 🚀 Live Features

- 🔍 Real-time spam detection
- 🧠 Machine Learning model (Logistic Regression)
- 📊 TF-IDF text vectorization
- 🎨 Clean and modern Streamlit UI
- ⚡ Fast predictions

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit

---

## 🧠 How It Works

1. Text data is cleaned (lowercase, punctuation removed)
2. TF-IDF converts text into numerical features
3. Logistic Regression model is trained
4. Model predicts whether message is spam or not

---

## 📊 Model Performance

- Accuracy: **~95% to 98%**
- Dataset: SMS Spam Collection

##screenshot
<img width="1407" height="946" alt="Screenshot 2026-04-03 133059" src="https://github.com/user-attachments/assets/119844f1-343f-426d-a742-bc07af930438" />

---

## 📁 Project Structure


##🧠 Short Explanation of Approach

I built a spam message classifier using a machine learning approach. First, I loaded and cleaned the SMS dataset by converting text to lowercase and removing unnecessary characters. Then, I transformed the text data into numerical form using TF-IDF vectorization. After that, I trained a Logistic Regression model to classify messages as spam or not spam. The model achieved high accuracy on test data. Finally, I created a simple Streamlit web app where users can input a message and get real-time predictions.
