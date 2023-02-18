import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache
def get_data():
     return pd.read_csv('SM_Survey_UPSA-2020_clean.csv')

 
def aleksandra_plot():
    df = pd.read_csv('SM_Survey_UPSA-2020_clean.csv')
    st.header("Academic performance, GPA, and 4 related social media usage metrics :tada:")
    #st.markdown("These two blocks of graphs help to see clearly the relationship between students academic performance and the four metrics of social media usage as Time, Groups, Friends, Notifications. We have GPA on the y axis and the aforementioned metrics on the x axis, the lines reflect the mean and 95\% confidence interval ("blurred" areas). So, from the first graph it is clear that the more time a student spends on social media, the lower is his GPA. Plus, in the first block we can see the differences between genders. From this particular dataset, we can say that there is not much difference between males in females, except for 2 particular tails: for example, people with 4000 friends tend to have better GPA than those with 3000. Same for the notifications. \n \t Finally, there is the second block which shows difference for age groups. One can see that students below 30 y.o. having 4000 friends are performing better than elder students. So there is some positive relationship between media usage and academic performance.")
    st.markdown("- How the user can see the comparison of GPA and 4 related social media usage metrics: Time, Groups, Friends, Notifications by Gender and different Age groups. \n \t For example, one can see that the more students spend time browsing media - the smaller GPA they have.\n \t In addition, in the first part we can observe the differences for males and females, and below we can see the differences for the three age groups.")
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
    return fig

def main():
    # Set the background color to a light gray
    st.set_page_config(page_title="Procrasti-vision",
                  page_icon=":guardsman:",
                  layout="wide")
    selected_tab = st.sidebar.radio("Menu", ["Description", "Statistics", "Plots"])
   
    if selected_tab == 'Plots':
        f = aleksandra_plot()
        st.pyplot(f)

    elif selected_tab == 'Description':

        st.title('Procrastination through the lenses of the social media usage and students’ academic performance')

        st.markdown("""

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

        """)

    elif selected_tab == 'Statistics':
        df = get_data()

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
        

        
if __name__ == '__main__':
    main()
    st.caption('Stay calm and be productive :tada:')



