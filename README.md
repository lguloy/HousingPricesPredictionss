# HousePricingPredictions

Housing Price Predictions in Ames, IA
Team: Vijitha Samarasinghe, Lawrence Guloy, Clayton Grace

Purpose/Scope:

It is widely known that there are multiple variables that impact the price of a house. This project seeks to determine which variables have the highest influence on the price of a house. This project utalizes the Ames Housing dataset, which contains 79 explanatory variables describing many aspects of residential homes in Ames, IA. The purpose of this project is to analyze the Ames Housing dataset using machine learning in order to accurately predict the price of homes.

Methodology:

The first step for this project was to clean the data. The original dataset contains 81 columns of data in various forms. CLEANING EXPLANATION.

Once the data was cleaned, feature importance was determined for the varriables. With 81 different vairables, the model would run the risk of over-fitting if all 81 variables were used. To determine feature importance the dataset was first transformed to use dummy variables throughout in order to prepare the data for catagorization. A random forest categorical analysis was used to establish the feature importance scores of the data variables. From this model 10 variables with the highest feature importance were used for orice predictions.

A Random Forest Regression analysis was used to perform the price prediction model because the data set contains both qualitative and quantitative variables. Random Forest does not require scaling the data, which was also a factor in its use. The first step in the model was to import the cleaned and transformed training dataset. The training used an 80/20 split where 80% of the data was used to train the model and 20% was reserved to test the effectiveness of the model. The model uses the 10 variables determined by the feature importance analysis. The training score of the model is 97% and the test score is 85%. After the model was trained it was finalized by fitting to 100% of the data and then saved. The saved model was subsequently used on a final dataset with no price information. The final dataset was cleaned and transformed in precisely the same manner as the train-test dataset. The model was run on the dataset and a list of prices was projected.

A web application was created so that users can input house information and run the data through the model to predict a house price. The application requires the same data inputs from the feature importance varriables. The application was deployed using heroku.

This project was derived from a Kaggle competition: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview


