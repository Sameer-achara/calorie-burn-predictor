# 🔥 Calorie Burn Prediction

A Machine Learning project that predicts the number of calories burned during physical activity based on user and exercise-related features.

## 📌 Project Overview

This project uses **Linear Regression** to predict calories burned using features such as:

- Gender
- Age
- Height
- Weight
- Duration
- Heart Rate
- Body Temperature

The project also uses a **Scikit-learn Pipeline** to handle preprocessing and model training together.

## 📊 Dataset

The dataset contains **15,000 records** and the following columns:

| Feature | Description |
|---------|-------------|
| User_ID | Unique user identifier |
| Gender | Male/Female |
| Age | Age of the person |
| Height | Height in cm |
| Weight | Weight in kg |
| Duration | Exercise duration in minutes |
| Heart_Rate | Heart rate during exercise |
| Body_Temp | Body temperature |
| Calories | Calories burned (Target) |

## ⚙️ Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning & Analysis
   ↓
Outlier Detection
   ↓
Outlier Capping using IQR
   ↓
Train-Test Split
   ↓
ColumnTransformer
   ├── Gender → OneHotEncoder
   └── Numerical Features → MinMaxScaler
   ↓
Linear Regression
   ↓
Model Evaluation