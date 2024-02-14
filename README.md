# FutureTerrorPredictor

## About

This is a classification project which focuses on classifying (and predicting) future terrorism using dataset from [Global Terrorism Database](https://www.start.umd.edu/gtd/). For detailed walkthrough, please refer to the [source code] and the below:

1. [Data Preparation & Cleaning](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) - Data extraction, Label encoding, Omitting null values, Restructuring of data into dictionary format 
2. [Exploratory Data Analysis & Data Visualisation](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) - Waffle map showing proportion of attacks by terrorist group
3. [Analytic Visualization](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) - Time series Heat Map (Interactive) showing geographic visualization of terrorist activities over the years 
4. [Machine Learning](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) - RandomForestClassifier model is used for prediction (More on models below)
5. [Training of Model](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) - Training Classification Model to accurately predict whether a terroristic event is successful (Fine-tuned using Gini Importance)
6. [Extrapolating data](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) - Use LinearRegression to extrapolate 2022 terrorism count based on historic data from GTB
7. [Generating synthetic data](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) - Synthesize future (simulative) terrorism events based off historic data
8. [Prediction and Findings](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) - Using Classification Model to predict future successful terrorist attacks
9. [Information Presentation](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) - Interactive Chloropleth map showing predicted distribution of terrorist attacks for 2022
10. [Statistical Inference](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) - Data-driven insights can be found here
11. [Ethical Consideration](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) - Additional moral concerns
12. [Intelligent Decision](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) - Additional insights, recommendations for future-proofing strategies
  

## Problem Definition
To predict impending future terrorism events and generating possible future events based on historic data.

## Models/Tools Used

1. `RandomForestClassifier`
2. `LinearRegression`
3. `DataSynthesizer`

## Visualization Tools Used

1. Waffle Chart
2. Time Series Heat Map 
3. Bar Chart
4. Private vs Synthetic Comparison Heatmaps
5. Chloropleth Map 

## Data-driven Insights

From our predicted results, we note that:
1) Countries such as `Iraq` are under --> **High Risk** of successfully being attacked
2) ``Afghanistan``, ``Pakistan`` are under --> **Moderate to High Risk**
3) ``Colombia``, ``Peru``, `Salvador`, ``Nigeria``, ``Somalia``, ``Yemen``, ``Turkey``, ``India``, ``Thailand``, ``Philippines`` are under --> **Moderate Risk**
4) Others --> **Relatively Low Risk**

Therefore, we successfully solved our initial problem statement:
1. Predicted impending future terrorism 
2. Generated possible future events based on historical data

- Countries that not only fall within the moderate- to high-risk categories, but also countries that share borders with these nations (e.g. ``Iran``, ``Syria``, ``Oman``) need to ramp up their monitoring regimes. Although this prediction is not definitive and fails to account for 2020's drop in terrorist activity, it can give good insight as to what terrorists' next move(s) could be

## Additional Insights

- Every country plays a role in defeating world terrorism; Each country should participate in having a shared data-pool of terroristic activities in their respective countries
- With such collated data, we can build a more robust classifier with greater accuracy of predictions
- While our model can be of great use to national security teams of the above countries as they prepare to monitor future threats, such information can easily fall into the wrong hands.
- If future terrorists get their hands on such prediction insights it will make it easier for them to 'escape the radar', which leads to more damage in the long run.
- Governments may benefit from using this prediction model as part of their arsenal of anti-terrorism measures, but never in place of it
- More insights can be found at the [end](https://github.com/wlfrag/SC1015/blob/main/SC1015_DS_Mini_project_live.ipynb) of the Jupyter Notebook.


## References

- Practical Motivation - https://www.politico.eu/article/attacks-will-be-spectacular-cia-war-on-terror-bush-bin-laden/
- Definition of Terrorism - https://en.wikipedia.org/wiki/Terrorism
- Waffle Map - https://cognitiveclass.ai/courses/data-visualization-python
- RandomForestClassifier - https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
- LinearRegression - https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
- DataSynthesizer - https://faculty.washington.edu/billhowe/publications/pdfs/ping17datasynthesizer.pdf
- Folium for Visualization - https://python-visualization.github.io/folium/quickstart.html
