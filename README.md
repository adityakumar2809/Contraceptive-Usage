# Contraceptive-Usage Prediction


Birth control, also known as contraception or family planning, is a way for a man and woman to
have sexual intercourse and avoid pregnancy. Some contraceptives, such as condoms, will also
protect a person from sexually transmitted diseases (STDs). The matter is so sensitive that we
cannot just directly ask people about the same. But, we do have some data based upon various
surveys conducted by the medical authorities based on which, we have developed our model which
shall predict whether a particular age group uses contraceptive or not.

## Dataset

 The dataset provided to me has 8 attributes which shall be taken as input from the user. Using our
 prediction model over the provided inputs, we are going to predict whether the person has used
 Contraceptive or not. The following were the attributes in the given dataset.

<img src="https://github.com/2000utkarsh/Contraceptive-Usage/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.05.25%20PM.png" width="600" height="400" />


## Graphical Depiction of the attributes

<img src="https://github.com/2000utkarsh/Contraceptive-Usage/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.02.44%20PM.png" width="600" height="400" />

<img src="https://github.com/2000utkarsh/Contraceptive-Usage/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.02.48%20PM.png" width="600" height="400" />

<img src="https://github.com/2000utkarsh/Contraceptive-Usage/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.02.52%20PM.png" width="600" height="400" />

<img src="https://github.com/2000utkarsh/Contraceptive-Usage/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.02.56%20PM.png" width="600" height="400" />


## Models Used:

• Decision Tree Classifier

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.04%20PM.png" width="500" height="600" />

• Logistic Regression

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.18%20PM.png" width="500" height="600" />

• Random Forest Classifier

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.23%20PM.png" width="500" height="600" />

• K-Neighbor Classifier

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.31%20PM.png" width="500" height="600" />

• SVC

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.37%20PM.png" width="500" height="600" />

• Multinomial NB

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.49%20PM.png" width="500" height="600" />

## Approach:
During the very first phase of the model, I cleaned the data and made it more sensible in numeric form, i.e. converted all the categorical data to numerical data and removed the NULL and missing values.
In the Second Phase, I did some visualizations over the given dataset which gave me a great view and hints for the implementation of the model.
In the third phase, I implemented various methods over the given dataset, the ones I had mentioned previously. The model gave prediction taking each and every model into consideration and then took out the average value of all the models result and then gave the result which were based on the provided input by the user.
In the final phase, I developed the UI for the model and then linked my model with the created UI for to make it ready for deployment in Django.

## User Interface:

<img src="https://github.com/2000utkarsh/Contraceptive-Usage/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.03.11%20PM.png" width="500" height="400" />

<img src="hhttps://github.com/2000utkarsh/Contraceptive-Usage/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.03.14%20PM.png" width="500" height="400" />


## Output Screen
<img src="https://github.com/2000utkarsh/Contraceptive-Usage/blob/master/app/imgs/Screenshot%202021-09-20%20at%209.03.18%20PM.png" width="500" height="400" />




## Future Scope

In the modern era, where such talks are getting more and more common and the awareness of people regarding the contraction of STDs because of not using contraceptive has increased, a model like the one I have deployed shall certainly help in people knowing whether the couple would have a safe, prosperous and healthy future or not and where the world is leading to in terms of mental and physical health.
















