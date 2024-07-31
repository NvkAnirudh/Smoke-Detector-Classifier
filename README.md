## Introduction

Welcome to the Intelligent Fire Alarm Classification System project! This repository contains the code and resources for developing a state-of-the-art machine learning model that enhances the reliability and accuracy of fire alarm systems. By leveraging advanced algorithms, this project aims to minimize false alarms and ensure timely detection of actual fire incidents, thus safeguarding lives and optimizing emergency response efforts.

## Project Overview
Accurate fire alarm classification is crucial for effective emergency responses and public safety. With the widespread adoption of smoke detectors, there has been a notable reduction in fire-related fatalities. However, the persistent issue of false alarms strains firefighting resources, highlighting the need for reliable fire alarm classification.

This project addresses this challenge by developing an intelligent fire alarm classification system using machine learning (ML). It spans the entire ML lifecycle, from data preparation and model training to deployment. Key features include:

- **Variance Inflation Factor (VIF)** for handling multicollinearity
- **Isolation Forest** for handling outliers
- **Data Version Control (DVC)** for managing data versions (*yet to be included*)
- **MLFlow** for experiment tracking and management (*yet to be included*)
- **Docker** for containerization (*yet to be included*)
- **Streamlit** application deployed on Hugging Face Spaces (*yet to be included*)

## Model Training and Evaluation

Multiple classification algorithms were trained and evaluated, including Decision Trees, Random Forests, XGBoost, CatBoost, LightGBM, and AdaBoost. Key metrics considered were:

- Precision: Measures the proportion of correct Fire Alarm predictions, minimizing false positives.
- Recall: Measures the proportion of actual fires detected, minimizing false negatives.
- Accuracy: Overall correctness of the predictions.
  
All models performed exceptionally well, with Random Forest, XGBoost, CatBoost, and AdaBoost achieving perfect scores in most cases (with no sign of overfitting), demonstrating their robustness and reliability.

## Business Impact

This project has significant potential for industry application, offering several benefits:

- Enhanced Fire Safety: Reliable fire alarm classification reduces the risk of undetected fires, ensuring timely emergency response and safeguarding lives.
- Resource Optimization: Minimizing false alarms alleviates the burden on firefighting resources, allowing for more efficient allocation and utilization.
- Scalability: The modular design and deployment strategy enable easy integration and scaling within existing fire safety systems.

## Articles

Learn more about the project in my articles below:
1) [Fire Alarm Classification - An End-to-End ML Application (Part 1)](https://medium.com/@nutianirudh/end-to-end-machine-learning-application-fire-alarm-classification-part-1-development-51bd6975b82a)
2) Fire Alarm Classification - An End-to-End ML Application (Part 2) (*yet to be published*)

## Conclusion
This repository provides a comprehensive framework for developing and deploying an intelligent fire alarm classification system. By enhancing the reliability and accuracy of fire detection, this project contributes to improved fire safety and resource management. I invite you to explore the code, experiment with the models, and contribute to the ongoing development of this important safety tool.

## License
This project is licensed under the MIT License - see the [LICENSE.md]([https://github.com/NvkAnirudh/Medical_Cost_Prediction/blob/main/LICENSE](https://github.com/NvkAnirudh/Smoke-Detector-Classifier/blob/main/LICENSE)) file for details

