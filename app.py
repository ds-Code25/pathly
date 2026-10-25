import streamlit as st


# importing the gen_recommendations function
from recommender import gen_recommendations

#importing the get_available_interests function
from recommender import get_available_interests

#UI parts
st.title("Pathly")

#Short explenation for the user to show how and why to use the program
st.caption("Do you struggle with finding relevant courses to grow your interests? Creating side project ideas? Or searching for potential career paths? Then wait no more! Select a topic, and we'll help you find a path forward!")

#Getting a list of interests from RULES
interest_list = get_available_interests()

#The different topic options a user can choose from: corispoding to rules.py
interests = st.multiselect("Choose your interests:", interest_list)
#"Machine Learning", "Data Science","Finance", "Backend Development", "Business Analysis"

#button to generate and show the recommended courses, projects, and careers
if st.button("Generate My Path →"):

    courses, projects, careers = gen_recommendations(interests)

    #Starting with courses
    st.markdown("## Courses")
    st.divider()

    for c in courses:
        st.info(f"{c['name']} ({c['platform']})")
        st.markdown(f"[➤ Go to course]({c['link']})")

    #projects
    st.markdown("## Projects")
    st.divider()

    for p in projects:
        st.info(p)

    #careers
    st.markdown("## Careers")
    st.divider()

    for ca in careers:
        st.info(ca)
