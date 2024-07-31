import jupyter_to_medium

# Medium credentials
username = 'nutianirudh'
integration_token = '2c4d9e45a4102e762dbf47411834ec906c0af81102a6f4580bb5a29774a7a92ca'

# Article title and tags
title = 'End-to-End Machine Learning Application (Fire Alarm Classification) - Part 1 (Development)'
tags = ['Smoke Detectors','Machine Learning', 'EDA', 'Classification', 'Variance Inflation Facotr', 'Modular Programming']

# Converting the jupyter notebook to a Medium article
jupyter_to_medium.publish(
    'notebook/jupyter_to_medium.ipynb',
    integration_token = integration_token,
    title = title,
    tags = tags,
    publish_status = 'draft'
)