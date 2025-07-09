# Stacked Noise Filtering and Optimized Predictive Modeling for Real-Time Stencil Printing Process (SPP)

## 📌 Project Overview
This project presents a comprehensive approach to enhancing prediction accuracy in the **Stencil Printing Process (SPP)** by integrating advanced noise filtering techniques with machine learning models. It targets key variables crucial for quality control in Surface Mount Technology (SMT) manufacturing.

---

## 🎯 Objectives
- Improve **prediction accuracy** of Volume, Offset X, and Offset Y in the SPP.
- Apply and evaluate **signal denoising filters** to enhance data quality.
- Use **machine learning models** for robust real-time predictive analytics.
- Explore **filter stacking** strategies to optimize model performance.

---

## 🧠 Models Used
- **Decision Tree Regressor (DTR)**
- **Support Vector Regressor (SVR)**
- **Artificial Neural Networks (ANN)**

---

## 🎯 Target Variables
- **Volume**
- **Offset X**
- **Offset Y**

---

## 🧪 Filters Applied
- **Median Filter**
- **Gaussian Filter**
- **Dual-Tree Complex Wavelet Transform (DTCWT)**
- **Savitzky-Golay Filter**
- **Bilateral Filter**
- **Multivariate Moving Average Filter**

---

## 🔍 Methodology

### Phase 1: Single Filter Evaluation
- Assessed individual filter performance across all three models.
- Compared **RMSE** and **MAE** to evaluate prediction accuracy.

### Phase 2: Two-Filter Hybrid Combinations
- Explored synergistic effects of dual-filter pipelines.
- DTCWT was fixed as the base filter in all combinations.

### Phase 3: Three-Filter Stacking (DTR Only)
- Focused on advanced three-stage denoising using DTR.
- Aimed at pushing the limits of accuracy and robustness.

### ➕ Multicollinearity Analysis
- Redundant features were identified and removed using correlation matrices and VIF.
- Resulted in improved generalization and error reduction.

---

## 📈 Results Summary
- Hybrid and stacked filters consistently outperformed single-filter setups.
- Multicollinearity removal led to more stable and accurate predictions.
- DTR showed strong interpretability, while ANN and SVR provided higher precision with cleaner inputs.

---

## ⚙️ Tools & Technologies
- **Python (NumPy, Pandas, Scikit-learn, TensorFlow, Matplotlib)**
- **SPI Dataset from SMT production line**
- **Evaluation Metrics:** RMSE, MAE
- **Data Visualization:** Power BI (for supplementary dashboarding)

---

## 👨‍💻 Author
**Maanakshaa Sree R**  
B.Tech CSE (AI & DS), SASTRA Deemed University

---

## 📄 License
This project is for academic and research purposes only.
