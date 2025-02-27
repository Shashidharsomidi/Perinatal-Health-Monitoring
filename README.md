# Perinatal-Health-Monitoring

## Overview
Perinatal Health Monitoring is an AI-driven system designed to support the mental well-being of pregnant women and new mothers. It utilizes machine learning and data analytics to analyze various data sources, enabling early detection of perinatal depression and anxiety symptoms. The system aims to complement professional diagnosis and improve maternal health outcomes.

## Project Explanation
This project focuses on developing an **AI-supported hybrid data management platform** for monitoring depression and anxiety symptoms in the perinatal period. It integrates **machine learning, big data processing, and real-time monitoring** to assist in early detection and intervention.

### Key Components
1. **Data Collection & Preprocessing**
   - Uses patient questionnaires, sensor data, and medical records.
   - Data is cleaned, normalized, and prepared for analysis.

2. **Feature Selection & Model Training**
   - Implements **Naïve Bayes, Random Forest, and Logistic Regression** for classification.
   - Feature selection techniques optimize prediction accuracy.

3. **Real-time Prediction System**
   - Developed using **Apache Spark** for real-time processing.
   - Utilizes **FastAPI** for serving predictions via REST API.

4. **Deployment & Integration**
   - Supports integration with **healthcare monitoring applications**.

### Objective
The system aims to provide an **instant remote health status prediction system** for detecting anxiety and depression in pregnant women. It enhances diagnosis speed, reduces questionnaire burden, and improves accessibility to mental health monitoring tools.

## Features
- **Machine Learning-Based Prediction**: Uses optimized models for perinatal mental health analysis.
- **Big Data Processing**: Implements **Apache Spark** for real-time health monitoring.
- **API-Based Accessibility**: FastAPI ensures easy integration with external systems.
- **User-Friendly Interface**: Web-based interface for clinicians and users.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Shashidharsomidi/Perinatal-Health-Monitoring.git
   cd Perinatal-Health-Monitoring
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Run the API:
   ```bash
   uvicorn main:app --reload
   ```

## Usage
- Send a **POST request** to `/predict` with patient data.
- The API returns **risk predictions** for perinatal depression/anxiety.

## Contributing
Feel free to fork the repository, create a branch, and submit a pull request for improvements.
