
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('DATA BREACH ANALYSIS')
st.subheader(" Crimnal Activity on the Internet is much broader that cybercrime as essentially all elements of human criminal activity have moved into cyberspace. Data breaches can be far more than a temporary terror — they may change the course of your life")
st.image('https://i.pcmag.com/imagery/articles/02mQkDMBiuzTBn1bq9ml1ZI-1..v1655219289.jpg')
st.write("This interactive application contains the analysis based on the **Data Breach** data collected over a few years")

#importing the dataset 
df = pd.read_csv("https://raw.githubusercontent.com/Jennifer-Elias/streamlit-project/main/Data%20Breaches.csv")
#df.head()
df.info()

# Data Cleaning
#checking for null values
df.isnull().sum()

#checking for duplicate values
df.duplicated().sum()
# Dropping NaN values and unnecessary columns
df=df.drop("Sources Link",axis=1)
st.subheader("DATAFRAME")
df

st.subheader("Data Breach count per year")
st.write('The following Graph Analysis the **DataBreach Count Per Year**.')# creating graph based on the data Breach count per year 
fig= plt.figure(figsize=(9,7)) # creating a new figure
 # projecting the plot on the created figure
sns.countplot(df['Year'])
st.pyplot(fig) # displaying the figure
st.write("According to the Analysis The highest Data breach was recorded during the year **2011**.The second observation that can be concluded is that there has been an increase in Data Breach from the year 2004 to 2011 , but it did reduce in the later years but  there not less than the the previous years   ")

st.subheader("Method of Leak per year")
st.write('The following Graph Analysis the Maximum frequency of Methods in which Data has been Breached.')
st.write(df['Method of Leak'].unique())
fig2= plt.figure(figsize=(9,7))
sns.set_theme(style="whitegrid")
sns.histplot(data=df,x= df['Year'],hue='Method of Leak',multiple="stack")
st.pyplot(fig2)
st.write("As seen in the graph that the most common method of data breach was **hacking** followed by **lost/stolen media**. Also It has been observed that their has been  an increase in  the frequency of the usage of hacking. The most common method used through the years are either by  stealing devices or hacking ")
st.write("According to the recent studies In 2020 report analyzed nearly 4000 confirmed data breaches,and over half of them i.e 52% were a result of hacking")

st.subheader("Most Targetted Firms ")
fig3= plt.figure(figsize=(9,7))
sns.histplot(y=df['Target Organization Type'])
st.pyplot(fig3)
st.write(""" According to the records the most common form of databreach has been detected via web activities
  people during web surfing accidently click on various popup adds hence resulting in providing the attacker an easy access to the users devices. Thus exposing your important data to the attackers followed by healthcare facilities, financial organisations and government organisation. Thus helping us to better understand the target organisations.
""")

st.subheader("Source Count")
st.write(" The following graph gives the count of the highest amount of updates are provided by which sites ")
fig4= plt.figure(figsize=(9,7))
sns.countplot(y=df['Sources name'])
st.pyplot(fig4)
st.subheader("Target Organizations")
st.write('**The following Organizationa have been the main targets of the Data Breach**')
st.write(df['Target Organization Type'].unique())
st.subheader("Most affected Target Organizations ")
fig5= plt.figure(figsize=(9,7))
sns.countplot(y=df['Target Organization Type'])
st.pyplot(fig5)

#Method of Leak
st.subheader("Method common method of Data Breach")
st.write('**The following methods the most common means of Data Breach**')
st.write(df['Method of Leak'].unique())
st.subheader("Most common Means of Data breach ")
fig6= plt.figure(figsize=(9,9))
sns.countplot(y=df['Method of Leak'])
st.pyplot(fig6)
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df["Data Sensitivity"]= le.fit_transform(df["Data Sensitivity"])
df["Target Organization Type"]= le.fit_transform(df["Target Organization Type"])
df["Sources name"]= le.fit_transform(df["Sources name"])
df["Method of Leak"]= le.fit_transform(df["Method of Leak"])
df["Entity"]= le.fit_transform(df["Entity"])

st.subheader("Correlation between Various Fields of the Dataset ")

st.write('In order to find the relation between Various Categorical Fiels we Have Used Label Encoding hence converting a few selective columns into a numerical format')
st.write("Label Encoding Code")
from PIL import Image
image = Image.open('C:/Users/ADMIN/Desktop/LE.jpg')
st.image(image)
st.write("The LabelEncoded Dataframe")
st.dataframe(df.head())

fig7= plt.figure(figsize=(9,9))
sns.heatmap(df.corr())
st.pyplot(fig7)
st.write(" the above mentioned heatmap defines the relation between various fields ")

st.subheader("Correlation between Data Sensitivity and Target Organization Type ")
import plotly.express as px
fig8= plt.figure(figsize=(9,9))
sns.scatterplot(data=df, x="Data Sensitivity", y="Target Organization Type",hue="Method of Leak",
    sizes=(20, 200), hue_norm=(0,9),legend="full")
st.pyplot(fig8)
