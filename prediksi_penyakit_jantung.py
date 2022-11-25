import pickle
import streamlit as st

predik = pickle.load(open('heart-disease.sav', 'rb'))

st.title ('Prediksi Penyakit Jantung Menggunakan SVM')

Age= st.text_input('Age')
Sex= st.text_input(' Male = 1/ famale = 0')
ChestPainType= st.text_input('Chest Pain Type')
BP= st.text_input ('BP')
Cholestrol= st.text_input('Colestrol')
FBSOper= st.text_input('gula darah')
EKGResult= st.text_input('EKG')
MaxHR= st.text_input('Max HR')
ExerciseAngina= st.text_input('Exercise angina')
Depression= st.text_input('Depression')
SlopeOfSt= st.text_input('Slope of St')
NumberOFVesselsFluro= st.text_input('Number of Vessels Fluro')
Thallium= st.text_input('Thalium')


Heart_Diag = ''

if st.button('Test Heart Disease'):
    heart_predi = predik.predict([[Age, Sex, ChestPainType, BP, Cholestrol, FBSOper, EKGResult, MaxHR, ExerciseAngina, Depression, SlopeOfSt, NumberOFVesselsFluro, Thallium]])

    if(heart_predi[0] == 1):
        Heart_Diag = 'Have Heart Disease'
    else : 
        Heart_Diag = 'Have No Heart Disease'
    st.success(Heart_Diag)