# Phishing Websites Detection Using Machine Learning Ensemble Models

## Project Description
This project presents a comprehensive machine learning pipeline designed to detect malicious phishing websites using structured tabular features. Phishing remains a primary threat vector in modern cybersecurity, often leading to credential harvesting and initial network compromise. In this project, we executed an end-to-end data science workflow—including exploratory data analysis (EDA), redundancy mitigation by removing collinear features, and stratified validation. We trained and compared two distinct ensemble frameworks: a Random Forest bagging classifier and an XGBoost sequential gradient boosting architecture, evaluating their performance through operational metrics tailored for cybersecurity deployment.

## Selected References
* **Selected Tutorial/Article:** chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://arxiv.org/pdf/2009.11116
* **Original GitHub Repository:** https://github.com/fafal-abnir/phishing_detection?utm_source

## Dataset Source
The data utilized for this reproduction study consists of 11,055 website instances evaluated across distinct cybersecurity features (such as SSL state, URL length, and prefix-suffix anchors). 
* **Dataset Location:** Shared locally in this repository as `dataset.csv`.

## Execution Instructions
To replicate and run this cybersecurity pipeline locally on your machine, please follow these steps:

1. **Clone the repository to your local environment:**
   ```bash
   git clone https://github.com/LoayArkab/HW_Project.git