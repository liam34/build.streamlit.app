import streamlit as st

header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

with header:
    st.title('welcome')

with  dataset:
    st.header('sample')
    st.text('sample sentence')

with features:
    st.header('the features i created')

with modelTraining:
    st.header('time to train the model')


  