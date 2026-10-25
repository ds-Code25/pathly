
import streamlit as st

from recommender import gen_recommendations
from ai_explainer import generate_roadmap

# Step 1: Create a fictional student profile
interests = ["Finance", "Machine Learning"]
experience_level = "Beginner"
career_goal = "Explore careers combining AI and finance"

# Step 2: Get Pathly's existing recommendations
courses, projects, careers = gen_recommendations(interests)

# Step 3: Generate an AI roadmap
roadmap = generate_roadmap(
    interests=interests,
    experience_level=experience_level,
    career_goal=career_goal,
    courses=courses,
    projects=projects,
    careers=careers,
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Step 4: Display the result
print(roadmap)
