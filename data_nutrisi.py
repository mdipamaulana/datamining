import pickle
import streamlit as sl

model = pickle.load(open('data_nutrisi.sav', 'rb'))

sl.title('estimasi Jumlah Lemak')
sl.subheader('Jumlah Total Lemak makanan di restaurant bawah tanah')
sl.write('---')

Sugars = sl.number_input('Input Sugars (g)')
Protein= sl.number_input('Input Protein (g)')
Calories = sl.number_input('Input Calories')
Sodium = sl.number_input('Input Sodium (mg)')
Serving_Size = sl.number_input('Input Serving Size (g)')
Cholesterol = sl.number_input('Cholesterol (mg)')
Carbohydrate = sl.number_input('Carbohydrate')

predict = ''

if sl.button('Estimasi Lemak'):
    predict = model.predict(
        [[Sugars, Protein, Calories, Sodium, Serving_Size, Cholesterol, Carbohidrate]]
    )
    sl.write ('Estimasi jumlah lemak makanan di restaurant bawah tanah (g) :'.predict)