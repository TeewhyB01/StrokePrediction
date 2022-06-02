from turtle import onclick
import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.write("""
                # Stroke Prediction
            """)
st.header("Enter Patient's Data")

def user_input():
    col1, col2, col3 = st.columns(3)
    with col1:
        gender_names = ['Male','Female']
        gender = st.radio('Gender',gender_names)
        hypertension_class = ['Yes','No']
        hypertension = st.radio('Does the patient have Hypertension? ',hypertension_class)
        worktypeclass = ['Private','Self-Employed','Govt_job','children','Never Worked']
        worktype = st.radio('Job Type ',worktypeclass)
    with col2:
        heartDisease_class = ['Yes','No']
        
        heartDisease = st.radio('Does the patient have Heart Disease? ',heartDisease_class)
        areatypeclass = ['Urban','Rural']
        areatype = st.radio('What kind of area do you live in?',areatypeclass)
        smokesclass = ['formerly_smoked','smokes','never_smoked']
        smokes = st.radio('Smoke Status',smokesclass)
    with col3:
        married_class = ['Yes','No']
        age = st.slider('Age',1,100, value=65)
        married = st.radio('Have you ever been married? ',married_class)
        glucoselevel = st.slider('Enter your glucose level',65.0000,380.0000, value=116.5605)
    bmi = st.slider('Enter your BMI',9.0000,66.0000, value=31.3555)
    hypertension_class_no = 0
    
    heartDisease_class_no = 0
    
    
    
    if hypertension == 'Yes':
        hypertension_class_no = 1
    else:
        hypertension_class_no = 0
    
    if heartDisease == 'Yes':
        heartDisease_class_no = 1
    else:
        heartDisease_class_no = 0
    
    
    
    
    
    
   
    # def DoSomething(): 
    #     prediction = 'Hello'
    #     return prediction
    # value = st.button('Make Prediction')
    # if value:
    #     global modelprediction
    #     modelprediction == DoSomething
    printvalue = {
        'gender': gender,
        'age' : age,
        'hypertension': hypertension,
        'heart_disease': heartDisease,
        'ever_married' : married,
        'work_type': worktype,
        'avg_glucose_level': glucoselevel,
        'bmi':bmi,
        'smoking_status': smokes
    }
    printvals = pd.DataFrame(printvalue,index=[0])  
    predictformat = {
        'age': [],
        'hypertension':[],
        'heart_disease':[],
        'avg_glucose_level':[],
        'bmi':[],
        'gender_Male':[],
        'ever_married_Yes': [],
        'work_type_Private':[],
        'work_type_Never_worked':[],
        'work_type_Self-employed':[],
        'work_type_children':[],
        'Residence_type_Urban':[],
        'smoking_status_formerly smoked':[],
        'smoking_status_never smoked':[],
        'smoking_status_smokes':[]
    }
    predictformat['age'].append(age)
    predictformat['hypertension'].append(hypertension_class_no)
    predictformat['heart_disease'].append(heartDisease_class_no)
    predictformat['avg_glucose_level'].append(glucoselevel)
    predictformat['bmi'].append(bmi)
    if gender == 'Male':
        predictformat['gender_Male'].append(1)
    else:
        predictformat['gender_Male'].append(0)
    if married == 'Yes':
        predictformat['ever_married_Yes'].append(1)
    else: 
        predictformat['ever_married_Yes'].append(0)
    if worktype == 'Private':
        predictformat['work_type_Private'].append(1)
        predictformat['work_type_Never_worked'].append(0)
        predictformat['work_type_Self-employed'].append(0)
        predictformat['work_type_children'].append(0)
    elif worktype == 'Self-Employed':
        predictformat['work_type_Private'].append(0)
        predictformat['work_type_Never_worked'].append(0)
        predictformat['work_type_Self-employed'].append(1)
        predictformat['work_type_children'].append(0)
    elif worktype == 'Govt_job':
        predictformat['work_type_Private'].append(0)
        predictformat['work_type_Never_worked'].append(0)
        predictformat['work_type_Self-employed'].append(0)
        predictformat['work_type_children'].append(0)
    elif worktype == 'children':
        predictformat['work_type_Private'].append(0)
        predictformat['work_type_Never_worked'].append(0)
        predictformat['work_type_Self-employed'].append(0)
        predictformat['work_type_children'].append(1)
    elif worktype == 'Never Worked':
        predictformat['work_type_Private'].append(0)
        predictformat['work_type_Never_worked'].append(1)
        predictformat['work_type_Self-employed'].append(0)
        predictformat['work_type_children'].append(0)
    if areatype == 'Urban':
        predictformat['Residence_type_Urban'].append(1)
    else:
        predictformat['Residence_type_Urban'].append(0)
    if smokes == 'formerly_smoked':
        predictformat['smoking_status_formerly smoked'].append(1)
        predictformat['smoking_status_never smoked'].append(0)
        predictformat['smoking_status_smokes'].append(0)
    elif smokes == 'smokes':
        predictformat['smoking_status_formerly smoked'].append(0)
        predictformat['smoking_status_never smoked'].append(0)
        predictformat['smoking_status_smokes'].append(1)  
    elif smokes == 'never_smoked':
        predictformat['smoking_status_formerly smoked'].append(0)
        predictformat['smoking_status_never smoked'].append(1)
        predictformat['smoking_status_smokes'].append(0)
    predictformatDF = pd.DataFrame(predictformat,index=[0])
    return printvals,predictformatDF

printval,predictformat = user_input()
st.subheader('Values Entered')
st.write(printval)
Pred = st.button('Make Prediction')
st.write('********************************************************************************')
st.info("Your Diagnosis")
# st.write('Model Prediction ')
if Pred:
    with open('RFStrokeModel.sav','rb') as f:
        model = pickle.load(f)
    # st.write(arrayy.tolist())
    prediction = model.predict(predictformat)
    if prediction == 0:
        st.success("The patient is healthy, No sign of eminent Stroke")
        # new_title = '<p style="font-family:sans-serif; color:Green; font-size: 25px;">The patient is healthy, No sign of eminent Stroke</p>'
        # st.markdown(new_title, unsafe_allow_html=True)
        # st.write("The patient is healthy, No sign of eminent Stroke")
    else:
        st.error("The patient has stroke")
        # new_title = '<p style="font-family:sans-serif; color:Red; font-size: 25px;">The patient has stroke</p>'
        # st.markdown(new_title, unsafe_allow_html=True)


# if modelprediction == 0:
#    pass
# else:
#     st.write(modelprediction)

# st.sidebar.header('NAVIGATIONS')
# st.sidebar.write('**************************')
# pagesgroup = ['Visuals','Add to Database','Model Monitoring','Predictions']
# st.sidebar.radio('Pages',pagesgroup)
