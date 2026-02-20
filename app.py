import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title('Titanic Dashboard')

df = pd.read_csv('titanic_data.csv')
# st.write(df)

# print(df.info())
df['Embarked'] = df['Embarked'].fillna('Unknown')

# get unique values for embarked port
embarked_port = list(df['Embarked'].unique())
gender = list(df['Sex'].unique())

col1,col2 = st.columns([1,1])
selected_port = col1.selectbox(options=embarked_port,
                               label='Select a port')
selected_gender = col2.selectbox(options=gender,
                                 label='Select a gender')

# Filter dataframe based on the widget values
df_plot = df[df['Embarked'] == selected_port]
df_plot = df_plot[df_plot['Sex'] == selected_gender]