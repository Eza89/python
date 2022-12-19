import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("My first Streamlit App")
st.write(pd.DataFrame({
    'Intplan': ['yes', 'yes', 'yes', 'no'],
    'Churn Status': [0, 0, 0, 1]
}))

iris = sns.load_dataset('iris')
fig = plt.figure(figsize=(10, 4))
sns.boxplot(data=iris)
st.pyplot(fig)
