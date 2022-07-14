# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 09:43:01 2022

@author: NITESH MAURYA
"""
from PIL import Image

import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

diabeties = pickle.load(open('DiabetesModel.sav', 'rb'))
heart = pickle.load(open('HeartDeaseas.sav','rb'))
parking = pickle.load(open('parkingSons.sav','rb'))

#sideBar Navigation

with st.sidebar:
    selected = option_menu('Choose Your Disease', 
                           ['Home','Diabetes','Heart Disease','ParkingSons'], 
                           default_index=0,
                           icons=['house','activity','heart','person']
                           ,styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
   }
                           )
logo = Image.open(r'logo.png')
profile = Image.open(r'health.jpg')
#Diabetes PRediction
if selected=="Home":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Welcome to Multiple Disease Prediction App</p>', unsafe_allow_html=True)    
    with col2:               # To display brand log
        st.image(logo, width=130 )
    
    st.write("Health is fundamental for a good quality of life. Being free from illness or injury directly affects our capacity to enjoy life. Historical data shows that global life expectancy has increased drastically over the last couple of centuries, with substantial long-run improvements in all countries around the world") 
    st.write("In this app you can predict your diabetes and Heart Disese by providing some information about your blood test results. This app will compare your data with the previous medical data set.")
    st.image(profile, width=700 )
    
def diabetesSoltutions():
    st.write("<h3>Manage Your Diabetes for Life</h3>", unsafe_allow_html = True)
    dontWorry = Image.open(r'dontWorry.jpg')
    st.image(dontWorry,width=700)
    st.write("<p>It is common to feel overwhelmed, sad, or angry when you are living with diabetes. You may know the steps you should take to stay healthy, but have trouble sticking with your plan over time. This section has tips on how to cope with your diabetes, eat well, and be active.</p>",unsafe_allow_html=True)
    st.write("<h5>Cope with your diabetes.</h5><br><p><b>1.</b> Stress can raise your blood sugar. Learn ways to lower your stress. Try deep breathing, gardening, taking a walk, meditating, working on your hobby, or listening to your favorite music.</p>",unsafe_allow_html=True)
    st.write("<p><b>2.</b>Ask for help if you feel down. A mental health counselor, support group, member of the clergy, friend, or family member who will listen to your concerns may help you feel better.</p><br><h5>Eat well.</h5>",unsafe_allow_html = True)
    khana  = Image.open(r'diaThali.png')
    st.image(khana,width=550)
    st.write("<p> Make a diabetes meal plan with help from your health care team. Choose foods that are lower in calories, saturated fat, trans fat, sugar, and salt. Eat foods with more fiber, such as whole grain cereals, breads, crackers, rice, or pasta.Choose foods such as fruits, vegetables, whole grains, bread and cereals, and low-fat or skim milk and cheese. Drink water instead of juice and regular soda. When eating a meal, fill half of your plate with fruits and vegetables, one quarter with a lean protein, such as beans, or chicken or turkey without the skin, and one quarter with a whole grain, such as brown rice or whole wheat pasta.",unsafe_allow_html=True)
    st.write("<h5>Be active.</h5>",unsafe_allow_html = True)
    st.write("<p>Set a goal to be more active most days of the week. Start slow by taking 10 minute walks, 3 times a day.Twice a week, work to increase your muscle strength. Use stretch bands, do yoga, heavy gardening (digging and planting with tools), or try push-ups.Stay at or get to a healthy weight by using your meal plan and moving more.</p>",unsafe_allow_html=True)    
    st.write("<h5>Know what to do every day.</h5>",unsafe_allow_html=True)
    st.write("<p>Take your medicines for diabetes and any other health problems even when you feel good. Ask your doctor if you need aspirin to prevent a heart attack or stroke. Tell your doctor if you cannot afford your medicines or if you have any side effects.Check your feet every day for cuts, blisters, red spots, and swelling. Call your health care team right away about any sores that do not go away.Brush your teeth and floss every day to keep your mouth, teeth, and gums healthy.Stop smoking. Ask for help to quit. Call 1-800-QUITNOW (1-800-784-8669).Keep track of your blood sugar. You may want to check it one or more times a day. Use the card at the back of this booklet to keep a record of your blood sugar numbers. Be sure to talk about it with your health care team.Check your blood pressure if your doctor advises and keep a record of it.<p>", unsafe_allow_html= True)
    st.write("<h5>Talk to your health care team.</h3>",unsafe_allow_html=True)
    st.write("<p>Ask your doctor if you have any questions about your diabetes.Report any changes in your health.</p>", unsafe_allow_html = True)
    
def healthyDia():
    st.write("<b>Yeah It is very good news but don't be lazy in your daily life. Follow these tips to avoid diabetes in future</b>",unsafe_allow_html=True)
    st.write("<h3>Lose extra weight</h3>",unsafe_allow_html =True)
    weight = Image.open(r'extraWeight.jfif')
    st.image(weight,width=700)
    st.write("<p>Losing weight reduces the risk of diabetes. People in one large study reduced their risk of developing diabetes by almost 60% after losing approximately 7% of their body weight with changes in exercise and diet. The American Diabetes Association recommends that people with prediabetes lose at least 7% to 10% of their body weight to prevent disease progression. More weight loss will translate into even greater benefits. Set a weight-loss goal based on your current body weight. Talk to your doctor about reasonable short-term goals and expectations, such as a losing 1 to 2 pounds a week.</p>",unsafe_allow_html=True)
    st.write("<h3>Following a healthy eating plan</h3>",unsafe_allow_html = True)
    eating = Image.open(r'healthyEating.jpg')
    st.image(eating,width=700)
    st.write("<p> It is important to reduce the amount of calories you eat and drink each day, so you can lose weight and keep it off. To do that, your diet should include smaller portions and less fat and sugar. You should also eat a variety of foods from each food group, including plenty of whole grains, fruits, and vegetables. It's also a good idea to limit red meat, and avoid processed meats</p>",unsafe_allow_html=True)
    st.write("<h3>Get regular exercise</h3>",unsafe_allow_html=True)
    exercise = Image.open(r'exersize.jfif')
    st.image(exercise,width=700)
    st.write("<p>Exercise has many health benefits, including helping you to lose weight and lower your blood sugar levels. These both lower your risk of type 2 diabetes. Try to get at least 30 minutes of physical activity 5 days a week. If you have not been active, talk with your health care professional to figure out which types of exercise are best for you. You can start slowly and work up to your goa</p>",unsafe_allow_html=True)
    st.write("<h3>Don't smoke</h3>",unsafe_allow_html=True)
    smoke = Image.open(r'smoke.jfif')
    st.image(smoke,width=700)
    st.write("<p>Smoking can contribute to insulin resistance, which can lead to type 2 diabetes. If you already smoke, try to quit.</p>",unsafe_allow_html=True)
    st.write("<h3>Talk to your health care provider </h3>",unsafe_allow_html=True)
    doctor = Image.open(r'doctorPhoto.jfif')
    st.image(doctor,width=700)
    st.write("<p>Talk to your health care provider to see whether there is anything else you can do to delay or to prevent type 2 diabetes. If you are at high risk, your provider may suggest that you take one of a few types of diabetes medicines</p>",unsafe_allow_html=True)
    st.write("<h3>Light to moderate alcohol consumption</h3>",unsafe_allow_html=True)
    alcohol = Image.open(r'alcohol.jfif')
    st.image(alcohol,width=700)
    st.write("<p>Evidence has consistently linked moderate alcohol consumption with reduced risk of heart disease. The same may be true for type 2 diabetes. Moderate amounts of alcohol—up to a drink a day for women, up to two drinks a day for men—increases the efficiency of insulin at getting glucose inside cells. And some studies indicate that moderate alcohol consumption decreases the risk of type 2 diabetes. [1, 34-39], but excess alcohol intake actually increases the risk. If you already drink alcohol, the key is to keep your consumption in the moderate range, as higher amounts of alcohol could increase diabetes risk. [40] If you don’t drink alcohol, there’s no need to start—you can get the same benefits by losing weight, exercising more, and changing your eating patterns</p>",unsafe_allow_html=True)
    
    
    
if(selected == 'Diabetes'):
    st.title("Diabetes Prediction")
    st.write("<b>Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.<b>",unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregenencies ')
    with col2:
        Glucose = st.text_input("Glucose Level ")
    with col3:
        BloodPressure = st.text_input("Blood Pressure ")
    with col1:
        SkinThickness = st.text_input('Skin Thickness value(MM)')
    with col2:
        Insulin=  st.text_input("Insuline level")
    with col3:
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Family diabetic History ")
    with col2:
        Age = st.text_input("Age ")
    
    #button For PRediction
    dia = ""
    
    if(st.button('Predict')):
        a = [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
        if(len(a)==0):
            st.error("Please Enter Data")
        else:
            predDia = diabeties.predict(a)
        
        if(predDia[0]==1):
             
            dia = "Positive"
            st.warning((dia))
            diabetesSoltutions()
        else:
            dia = "Negative"
            st.success((dia))   
            healthyDia()
            
    
    
if(selected == 'Heart Disease'):
    st.title("Heart Disease Prediction")
    st.write("High blood pressure, high blood cholesterol, and smoking are key risk factors for heart disease. About half of people in the United States (47%) have at least one of these three risk factors.2 Several other medical conditions and lifestyle choices can also put people at a higher risk for heart disease, including")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age ",min_value=1, max_value=110, value=1)
    with col2:
        sex = st.number_input("Gender(Male =1, Female = 0)",min_value=0, max_value=1, value=0)
    with col3:
        cp = st.number_input("Chest Pain Type",min_value=0, max_value=3, value=0)
    with col1:
        trestbps = st.number_input("Resting Blood PRessure",min_value=1, max_value=500, value=1)
    with col2:
        chol = st.number_input("Serum Cholestoral in mg/dl",min_value=1, max_value=700, value=1)
    with col3:
        fbs = st.number_input("Fasting Blood Suger>120mg/dl(1=true,0=false) ",min_value=0, max_value=1, value=0)
    with col1:
        restecg = st.number_input("resting electrocardiographic results (values 0,1,2)",min_value=0, max_value=2, value=0)
    with col2:
        thalach = st.number_input("maximum heart rate achieved",min_value=1, max_value=250, value=1)
    with col3:
        exang = st.number_input("exercise induced angina(1=yes,0=no)",min_value=0, max_value=1, value=0)
    with col1:
        oldpeak = st.number_input(" ST depression induced by exercise relative to rest",min_value=0.0, max_value=10.0, value=0.0, step=0.1)
    with col2:
        slope = st.number_input("the slope of the peak exercise ST segmen",min_value=0, max_value=10, value=0)
    with col3:
        ca = st.number_input("number of major vessels (0-3) colored by flourosopy",min_value=0, max_value=10, value=0)
    with col1:
        thal = st.number_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect",min_value=0, max_value=3, value=0)
        
    heartRes = ""
    if(st.button("Result")):
        a = [[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
        a = np.array(a,dtype=float)
        heartPred = heart.predict(a)
        if(heartPred[0]==1):
            heartRes = "Positive"
        else:
            heartRes = "Negative"
    st.success(heartRes)
    
    
    
if(selected == 'ParkingSons'):
    st.title("ParkingSons Disease Prediction")
    

    

    
