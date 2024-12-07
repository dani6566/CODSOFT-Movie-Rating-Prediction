# **Movie Rating Prediction**

A machine learning project aimed at predicting movie ratings based on features like genre, director, and actors. This project explores data preprocessing, feature engineering, and regression modeling techniques to uncover insights and build a predictive system.

---

## **Table of Contents**
- [Overview](#overview)  
- [Features](#features)  
- [Dataset](#dataset)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Results](#results)  
- [Future Work](#future-work)  
- [Contributing](#contributing)  
- [License](#license)

---

## **Overview**
This repository contains the implementation of a predictive model to estimate movie ratings based on historical data. The project:
- Preprocesses and cleans data to handle missing values.
- Engineers features such as actor and director popularity.
- Uses regression techniques (Random Forest Regression) to build the model.
- Evaluates performance with metrics like Mean Absolute Error (MAE) and R-squared (R²).

---

## **Features**
- Predicts movie ratings based on:
  - Genre
  - Cast (actors)
  - Director
  - Duration
  - Number of votes
- Supports feature importance analysis to identify key factors influencing ratings.
- Implements data imputation for handling missing values.

---

## **Dataset**
- **Source**: The dataset includes movie details such as title, year, duration, genre, rating, votes, director, and main actors.  
- **Size**: 15,509 records with 10 columns.  
- **Key Statistics**:
  - Rating range: 1.1 to 10.0
  - Significant missing data in features like `Duration`, `Votes`, and `Rating`.  

---

## **Installation**
### Prerequisites
- Python 3.7+
- Required libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/dani6566/CODSOFT-Movie-Rating-Prediction.git
   cd CODSOFT-Movie-Rating-Prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Results**
- **Best Model**: Random Forest Regression
- **Performance Metrics**:
  - Mean Absolute Error (MAE): 1.014
  - Root Mean Squared Error (RMSE): 1.277
  - R-squared (R²): 0.122
- **Feature Importance**:
  1. Actor Popularity  
  2. Director Popularity  
  3. Genre  
  4. Votes  
  5. Duration  

---

## **Future Work**
1. **Data Enhancement**: Include additional features such as box office revenue and critic reviews.  
2. **Advanced Models**: Experiment with XGBoost, LightGBM, and neural networks.  
3. **Recommendation Systems**: Extend the project to recommend movies based on user preferences.

---


## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---
