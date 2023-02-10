import streamlit as st 
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

@st.cache_data
def get_data():
     return pd.read_csv('SM_Survey_UPSA-2020_clean.csv'))

 
#configuration of the page
st.set_page_config(layout="wide")
#load dataframes

df = get_data()

#st.title('Interractive Information Visualization')
#st.title('Understanding Procrastivision among students')
st.title('Academic performance and social media usage')

st.markdown("""
## What is the **correlation/relationship** between social media usage and students’ academic performance ?

This visualisation shows the relationship between students academic performance expressed via `GPA` (grade point average) and 4 related `social media usage metrics`: 
- **Time** refers to average number of hours a student spends daily on social media,
- **Groups** represents to the number of social media groups a student belongs to,
- **Freinds** is the number of social media friends a student has,
- **Notifications** - the average number of times each student checks his phone notifications per day.

**WHAT** the visualizations show;
It is the result of an online survey where a random sample of 623 students was asked to self-reflect about
their usage of social media, so Mohammed Nurudeen and his team could measure the effect of social media on
academic performance. This application of social media may have some benefits for students’ academic performance.
Nonetheless, social media may have an addicting effect that could lead to several things including
poor health, poor concentration in class, poor time management, lack of appetite for learning, procrastination
and consequently poor academic performance.

**WHO** the visualization is for: parents, teachers and students.

**WHY** we the audience should care about it: while striving for performance one needs to decrease the potential non productive time.

**HOW** to read the visualization.

""")

st.subheader('View part of the data')
if st.checkbox("Preview dataframe"):
    st.dataframe(df.head())

st.subheader('Descriptive statistics')
if st.checkbox("Get statistics"):
    st.dataframe(df.describe())

st.subheader('Correlations')
if st.checkbox("View correlations"):
    correlation = df.corr()
    fig, ax = plt.subplots(figsize=(5,5)) 
    sns.heatmap(correlation,annot=True, cmap='spring', fmt=".2f", linewidth=.5, ax=ax)
    #st.write(correlation)
    st.pyplot(fig)

st.write(df.info())
st.metric(label="GPA",
            value=df.GPA.mean().round(2),
            delta="smth")

st.header("Academic performance, GPA, and 4 related social media usage metrics :tada:")
st.subheader("By Genders")

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(ncols=2,nrows=2, figsize=(10, 6)) #, figsize=(10, 10)
 
sns.lineplot(ax=ax1, data=df, x="Time", y="GPA", hue="Gender",style="Gender")
sns.lineplot(ax=ax2, data=df, x="Groups", y="GPA", hue="Gender",style="Gender")
ax1.set_title("Time vs GPA")
ax1.set_xlim(1,5)
ax1.set_ylim(1,4)
ax1.legend(loc=3, prop={'size': 6})
ax2.set_title("Groups vs GPA")
ax2.set_xlim(0,6)
ax2.set_ylim(1,4)
ax2.legend(loc=3, prop={'size': 6})

sns.lineplot(ax=ax3, data=df, x="Friends", y="GPA", hue="Gender",style="Gender")
sns.lineplot(ax=ax4, data=df, x="Notifications", y="GPA", hue="Gender",style="Gender")
ax3.set_title("Friends vs GPA")
ax3.set_xlim(1000,4000)
ax3.set_ylim(1,4)
ax3.legend(loc=3, prop={'size': 6})
ax4.set_xlim(5,50)
ax4.set_ylim(1,4)
ax4.legend(loc=3, prop={'size': 6})
ax4.set_title("Notifications vs GPA")

fig.set_tight_layout(True)
st.pyplot(fig)

st.header("Academic performance, GPA, and 4 related social media usage metrics :tada:")
st.subheader("By Age groups")

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(ncols=2,nrows=2, figsize=(10, 6)) #, figsize=(10, 10)
 
sns.lineplot(ax=ax1, data=df, x="Time", y="GPA", hue="Age Group", style="Age Group")
sns.lineplot(ax=ax2, data=df, x="Groups", y="GPA", hue="Age Group",style="Age Group")
ax1.set_title("Time vs GPA")
ax1.set_xlim(1,5)
ax1.set_ylim(1,4)
ax1.legend(loc=3, prop={'size': 6})
ax2.set_title("Groups vs GPA")
ax2.set_xlim(0,6)
ax2.set_ylim(1,4)
ax2.legend(loc=3, prop={'size': 6})

sns.lineplot(ax=ax3, data=df, x="Friends", y="GPA", hue="Age Group",style="Age Group")
sns.lineplot(ax=ax4, data=df, x="Notifications", y="GPA", hue="Age Group",style="Age Group")
ax3.set_title("Friends vs GPA")
ax3.set_xlim(1000,4000)
ax3.set_ylim(1,4)
ax3.legend(loc=3, prop={'size': 6})
ax4.set_xlim(5,50)
ax4.set_ylim(1,4)
ax4.legend(loc=3, prop={'size': 6})
ax4.set_title("Notifications vs GPA")

fig.set_tight_layout(True)
st.pyplot(fig)


st.caption('Stay calm and be productive :tada:')
