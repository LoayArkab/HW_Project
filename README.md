# Phishing Websites Detection Using Machine Learning Ensemble Models

## Project Description
This project presents a comprehensive machine learning pipeline designed to detect malicious phishing websites using structured tabular features. Phishing remains a primary threat vector in modern cybersecurity, often leading to credential harvesting and initial network compromise. In this project, we executed an end-to-end data science workflow—including exploratory data analysis (EDA), redundancy mitigation by removing collinear features, and stratified validation. We trained and compared two distinct ensemble frameworks: a Random Forest bagging classifier and an XGBoost sequential gradient boosting architecture, evaluating their performance through operational metrics tailored for cybersecurity deployment.

## Selected References
* **Selected Tutorial/Article:** [Predicting Phishing Websites using Classification Algorithms (arXiv)](https://arxiv.org/pdf/2009.11116)
* **Original GitHub Repository:** [fafal-abnir/phishing_detection](https://github.com/fafal-abnir/phishing_detection?utm_source)

## Dataset Source
The data utilized for this reproduction study consists of 11,055 website instances evaluated across distinct cybersecurity features (such as SSL state, URL length, and prefix-suffix anchors). 
* **Dataset Location:** Shared locally in this repository as `dataset.csv`.

## Repository Structure
```text
├── src/
│   └── Project.ipynb      # Optimized training and evaluation pipeline folder
├── dataset.csv            # Tabular phishing telemetry features
├── Summary.pdf            # Comprehensive project report and evaluation document
├── requirements.txt       # Environment dependency manifest
├── test_pipeline.py       # Automated structural integrity tests
└── README.md              # Project documentation and execution guide
```

## Execution Instructions

To replicate and run this cybersecurity pipeline locally on your machine, please follow these steps:

1. Clone the repository to your local environment:
git clone [https://github.com/LoayArkab/HW_Project.git](https://github.com/LoayArkab/HW_Project.git)
cd HW_Project

2. Install Dependencies
Deploy all required mathematical modeling and classification libraries using the package manifest:
pip install -r requirements.txt

3. Run Automated Repository Tests
Before executing the pipeline, validate directory structure and dataset paths by running the automated test suite:
python test_pipeline.py

4. Run the Machine Learning Pipeline
To view the comprehensive exploratory data analysis, visual confusion matrices, and empirical error analysis, execute the main Jupyter notebook located within the source directory:
jupyter notebook src/Project.ipynb
