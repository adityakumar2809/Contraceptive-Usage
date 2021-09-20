from django.shortcuts import render
import numpy as np
import pandas as pd
from . import forms
import pickle
import os

# Create your views here.

def readData(filepath='data/contraceptive_method.csv'):
    df = pd.read_csv(filepath)
    X = df.iloc[:,0:len(df.columns)-1]
    y = df.iloc[:, -1]
    return X, y


def evaluateUserInput(data_features, X_test):
    # X_test = getUserInput(data_features)
    with open(f'app/result/scaler/MinMaxScaler.sav', 'rb') as f:
        scaler = pickle.load(f)
        print(scaler)
        X_test = scaler.transform([X_test])

    model_accuracy_scores = pd.read_csv(
        'app/result/model_evaluation/ModelEvaluationScores.csv'
    )['Accuracy']

    model_list=[]
    test_results = []
    prediction_score = 0
    model_files = os.listdir('app/result/models')
    for model_file in model_files:
        with open(f'app/result/models/{model_file}', 'rb') as f:
            model = pickle.load(f)
            model_list.append(model)
            test_results.append([str(model)[ : str(model).index('(')]])

    for index, classifier in enumerate(model_list):
        y_pred = classifier.predict(X_test)
        y_pred = 'Positive' if y_pred == 1 else 'Negative'

        if y_pred == 'Positive':
            prediction_score += 1 * model_accuracy_scores[index]
        else:
            prediction_score -= 1 * model_accuracy_scores[index]

        test_results[index].append(y_pred)

    
    prediction_score = prediction_score / sum(model_accuracy_scores)
    if prediction_score < 0:
        prediction_class = 'Negative'
    elif prediction_score > 0:
        prediction_class = 'Positive'
    else:
        prediction_class = 'Indeterminate'


    results = {}
    for test_result in test_results:
        results[test_result[0]] = test_result[1]
    
    final_result = []
    final_result.append(results)
    final_result.append(prediction_score)
    final_result.append(prediction_class)

    return final_result
    


def getUserInput(data_features):
    user_input = []
    for feature in data_features.columns:
        print(f'Enter value for {feature}')
        print(f'Range is {min(data_features[feature])} to {max(data_features[feature])}')
        user_input.append(input('Your input: '))
    return user_input
    

def Home(request):
    X, y = readData(filepath='app/data/parkinsons.csv')
    
    
    if request.method == 'POST':
        form = forms.InputDataForm(request.POST)
        if form.is_valid():
            wife_age = form.cleaned_data['wife_age']
            wife_education = form.cleaned_data['wife_education']
            husband_education = form.cleaned_data['husband_education']
            number_of_children = form.cleaned_data['number_of_children']
            is_wife_islamic = form.cleaned_data['is_wife_islamic']
            is_wife_non_working = form.cleaned_data['is_wife_non_working']
            standard_of_living = form.cleaned_data['standard_of_living']
            media_exposure = form.cleaned_data['media_exposure']


            user_input = []
            user_input.append(wife_age)
            user_input.append(wife_education)
            user_input.append(husband_education)
            user_input.append(number_of_children)
            user_input.append(is_wife_islamic)
            user_input.append(is_wife_non_working)
            user_input.append(standard_of_living)
            user_input.append(media_exposure)

            results = evaluateUserInput(X, user_input)
            
            return render(request, 'result.html', {'model_results': results[0], 'prediction_score': results[1], 'prediction_class': results[2]})

            

        else:
            pass
    else:
        form = forms.InputDataForm()
        return render(request, 'home.html', {'form': form})




