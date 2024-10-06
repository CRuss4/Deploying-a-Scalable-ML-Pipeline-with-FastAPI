# Model Card

## Model Details
Developer Name: Corey Russell  
Date: 10/4/2024  
Model Version: 1.0  
Model Info: The model was created using logistic regression with default hyperparameters in scikit-learn 1.0.2.

## Intended Use
This model is used to predict whether an individual's income is greater than $50,000 per year based on census data.

## Training Data
The dataset used is Census Income Dataset and was obtained from https://archive.ics.uci.edu/dataset/20/census+income.  
There are 48,842 instances and 14 features with a mixture of categorical and integer feature types.

## Evaluation Data
20% of the Census Income Dataset was reserved and used for evaluation.

## Metrics
The metrics used were Precision, Recall, and F1.   
Precision: 0.7285 | Recall: 0.2699 | F1: 0.3939

## Ethical Considerations
The model is based on data from 1994. Applying this model to current data may introduce bias.  
Although the data contains sensitive personal information, there is no personally identifiable information.

## Caveats and Recommendations
Factors may need to be adjusted if this model is to be applied to current datasets.  
One of these considerations being inflation. Example: $50,000 income in 1994 vs 2024.