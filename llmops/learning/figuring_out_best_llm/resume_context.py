context = r"""
Vijay Takbhate is a Data Science and MLOps enthusiast skilled in Python, SQL, MLflow, Docker, and CI/CD. 
He has worked on multiple end-to-end machine learning projects, focusing on model deployment and automation.

Projects include:
1. Medical Insurance Cost Prediction (SVR): Built a predictive system to estimate medical insurance charges 
   using demographic and lifestyle factors like age, BMI, smoking status, and region. Improved R² from 0.72 to 0.86 
   and reduced MAE from 0.099 to 0.034. Developed a Flask web application, containerized with Docker, and deployed on AWS EC2.
   Implemented MLOps best practices like MLflow tracking, GitHub Actions CI/CD, and Kubeflow pipelines.

2. Turbofan Jet Engine Lifecycle Prediction (CNN + LSTM): Developed a Remaining Useful Life (RUL) prediction 
   system using NASA CMAPSS dataset. Built a hybrid CNN + LSTM model for temporal and spatial patterns. 
   Implemented an MLOps pipeline with data processing, training, and deployment using AWS and Docker.

Experience:
- Risk Analyst (InCred Financial Services): Designed and deployed policies in Business Rule Engine, 
  built a Python package 'Simulator' reducing policy verification time by 30%, integrated CI/CD workflows using GitHub Actions, 
  and worked with Databricks, Metabase, SQL, and Excel.
- Automation Engineer (Fox Solutions): Built automation pipelines with monitoring and reproducibility focus 
  using version control and PLC/SCADA tools.

Technical Skills:
Python, SQL, MLflow, DVC, DagsHub, Docker, GitHub Actions, Streamlit, Flask, Databricks, PySpark, AWS, GCP, Kubernetes.

Certifications:
- Complete MLOps Bootcamp with 10+ Projects (Udemy)
- MLOps Bootcamp: Mastering AI Operations (Udemy)

Education:
Bachelor of Technology in Electronics and Telecommunication, SVERI’s College of Engineering, 2024.
Diploma in Electronics and Telecommunication, 2021.

Blogging:
- "Supervised, Unsupervised, & Beyond: ML Techniques Simplified"
- "Comprehensive Docker Guide: Containerizing Flask Applications"

Soft Skills:
Critical Thinking, Problem Solving, Understanding Business Needs.
Languages: English, Marathi, Hindi.
"""

context_compressed = r"""
Vijay Takbhate – Data Science & MLOps enthusiast; skilled in Python, SQL, MLflow, Docker, CI/CD.

Projects:
1. Medical Insurance Cost Prediction (SVR): Predicted insurance charges using age, BMI, smoking, region; improved R² 0.72→0.86, MAE 0.099→0.034; deployed Flask app on AWS EC2 with Docker; tracked with MLflow, CI/CD via GitHub Actions, Kubeflow pipelines.
2. Turbofan Jet Engine RUL Prediction (CNN+LSTM): Used NASA CMAPSS dataset; hybrid CNN+LSTM for temporal/spatial patterns; deployed with AWS & Docker; full MLOps pipeline.

Experience:
- Risk Analyst, InCred: Built Business Rule Engine policies; Python 'Simulator' package reduced verification 30%; CI/CD with GitHub Actions; Databricks, SQL, Metabase.
- Automation Engineer, Fox Solutions: Automation pipelines with reproducibility & monitoring; version control & PLC/SCADA tools.

Technical Skills: Python, SQL, MLflow, DVC, DagsHub, Docker, GitHub Actions, Streamlit, Flask, Databricks, PySpark, AWS, GCP, Kubernetes.

Certifications: MLOps Bootcamp 10+ Projects (Udemy), MLOps Bootcamp: Mastering AI Operations (Udemy).

Education: B.Tech in Electronics & Telecommunication, SVERI College, 2024; Diploma, 2021.

Blogging: "Supervised, Unsupervised, & Beyond: ML Techniques Simplified", "Comprehensive Docker Guide: Containerizing Flask Apps".

Soft Skills: Critical Thinking, Problem Solving, Understanding Business Needs.
Languages: English, Marathi, Hindi.
"""


resume_qa = {
    "What is Vijay Takbhate's main field of interest?": "Data Science and MLOps.",
    "What programming languages is Vijay skilled in?": "Python and SQL.",
    "Which machine learning project did Vijay build to predict insurance charges?": "Medical Insurance Cost Prediction using Support Vector Regression (SVR).",
    "What was the improvement in R² score in the Medical Insurance Cost Prediction project?": "Improved from 0.72 to 0.86.",
    "What was the reduction in MAE in the Medical Insurance Cost Prediction project?": "Reduced from 0.099 to 0.034.",
    "Which technologies were used to deploy the Medical Insurance Cost Prediction project?": "Flask, Docker, and AWS EC2.",
    "Which MLOps tools did Vijay use in his projects?": "MLflow, GitHub Actions, and Kubeflow.",
    "What kind of hybrid model was used in the Turbofan Jet Engine Lifecycle Prediction project?": "A hybrid CNN + LSTM model.",
    "Which dataset was used for the Turbofan Jet Engine project?": "NASA CMAPSS dataset.",
    "What was the objective of the Turbofan Jet Engine project?": "To predict the Remaining Useful Life (RUL) of jet engines.",
    "Where did Vijay work as a Risk Analyst?": "At InCred Financial Services.",
    "What was Vijay’s contribution at InCred Financial Services?": "Designed and deployed policies in Business Rule Engine, built a Python package 'Simulator', and integrated CI/CD using GitHub Actions.",
    "What percentage of policy verification time was reduced by the Simulator package?": "30 percent.",
    "Which tools did Vijay use at InCred Financial Services?": "Databricks, Metabase, SQL, and Excel.",
    "Where did Vijay work as an Automation Engineer?": "At Fox Solutions.",
    "What were Vijay’s key responsibilities at Fox Solutions?": "Built automation pipelines focused on monitoring, reproducibility, and version control using PLC/SCADA tools.",
    "Which version control tools is Vijay familiar with?": "Git and GitHub.",
    "Which cloud platforms does Vijay have experience with?": "AWS and GCP.",
    "Which orchestration or container technologies has Vijay worked with?": "Docker and Kubernetes.",
    "What are Vijay’s core technical skills?": "Python, SQL, MLflow, DVC, DagsHub, Docker, GitHub Actions, Streamlit, Flask, Databricks, PySpark, AWS, GCP, and Kubernetes.",
    "Which certifications does Vijay hold?": "Complete MLOps Bootcamp with 10+ Projects and MLOps Bootcamp: Mastering AI Operations, both from Udemy.",
    "Where did Vijay complete his Bachelor’s degree?": "SVERI’s College of Engineering in Electronics and Telecommunication, 2024.",
    "When did Vijay complete his diploma?": "In 2021.",
    "What are some of Vijay’s blog topics?": "‘Supervised, Unsupervised, & Beyond: ML Techniques Simplified’ and ‘Comprehensive Docker Guide: Containerizing Flask Applications’.",
    "What soft skills does Vijay possess?": "Critical Thinking, Problem Solving, and Understanding Business Needs.",
    "Which languages can Vijay speak?": "English, Marathi, and Hindi."
}
