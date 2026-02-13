# 🎵 End-to-End Music Recommendation System 
---

![Python](https://img.shields.io/badge/Python-red?logo=python)
![NumPy](https://img.shields.io/badge/NumPy-brown?logo=numpy)
![Pandas](https://img.shields.io/badge/Pandas-purple?logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-green?logo=scikit-learn)
![NLP](https://img.shields.io/badge/NLP-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-blue?logo=streamlit)


## 📌 Overview
This project implements a content-based Music Recommendation System that suggests similar songs by analyzing textual information such as song titles and artist names.<br>
The system uses Natural Language Processing (NLP) techniques and machine learning–based similarity measures to generate meaningful recommendations through an interactive Streamlit web application.

The solution is completely dataset-driven and does not rely on any third-party music APIs, making it lightweight and easy to deploy.

---

## 🎯 Problem Statement
Finding relevant songs that match a user’s musical preference can be challenging without a structured recommendation mechanism.<br>
This project addresses the problem by applying NLP-based similarity analysis to identify semantically similar songs and recommend the most relevant alternatives.

---

## 🧠 Approach & Methodology
### 1. Data Preparation

Imported the music dataset from a CSV file.<br>
Standardized column names for consistency.<br>
Removed missing or incomplete records to ensure clean input data.

### 2. Feature Engineering (NLP)
Combined song names and artist names into a single textual feature.<br>
Applied TF-IDF Vectorization to transform text into numerical vectors.

### 3. Similarity Computation
Used Cosine Similarity to compute similarity scores between songs.<br>
Ranked songs based on similarity values.

### 4. Recommendation Logic
Accepts a song selected by the user.<br>
Retrieves top similar songs based on similarity scores.<br>
Ensures fast and accurate recommendations.

### 5. User Interface
Built using Streamlit.<br>
Dropdown-based song selection.<br>
Button-triggered recommendations.<br>
Custom gradient background with card-style song display.

---

## ✨ Key Features
Content-based music recommendation system.<br>
NLP-driven similarity analysis.<br>
Simple and intuitive web interface.<br>
Lightweight and fast execution.<br>
No external API dependency.

---

## 🛠️ Tech Stack
Programming Language: Python.<br>
Libraries: Pandas, Scikit-learn.<br>
NLP Techniques: TF-IDF Vectorization, Cosine Similarity.<br>
Web Framework: Streamlit.<br>
Styling: Custom CSS.

---

## 📁 Project Structure

```text
Music-Recommendation-System/
│
├── app.py              # Streamlit application
├── Dataset.csv         # Music dataset
├── README.md           # Project documentation
├── .gitignore          # Git ignored files
└── LICENSE             # License file
```

---

## ▶️ How to Run the Project
#### Run Web Application
pip install streamlit pandas scikit-learn<br>
streamlit run app.py<br>
python -m streamlit run app.py

#### Run Jupyter Notebook
pip install pandas scikit-learn notebook<br>
jupyter notebook

---

## 📌 Development Environment
IDE: PyCharm (used for Python & Streamlit development)<br>
Notebook Environment: Jupyter Notebook (used for experimentation and analysis)<br>
Version Control: Git & GitHub

---
## 📜 License
This project is licensed under the MIT License.
