import streamlit as st


# importing the gen_recommendations function
from recommender import gen_recommendations

#importing the get_available_interests function
from recommender import get_available_interests

#Importing the AI function
from ai_explainer import generate_roadmap

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

    # Save Pathly's recommendations for the AI feature
    st.session_state["pathly_recommendations"] = {
        "courses": courses,
        "projects": projects,
        "careers": careers
    }

    # Remember which interests generated these results
    st.session_state["pathly_interests"] = interests.copy()

    # Clear an old AI roadmap when new recommendations are made
    st.session_state.pop("pathly_roadmap", None)

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


# AI Career Roadmap Section
st.divider()
st.subheader("✨ Generate Your AI Career Roadmap")

# Ask the student about their experience
experience_level = st.selectbox(
    "What is your experience level?",
    ["Beginner", "Intermediate", "Advanced"]
)

# Ask about their career goal
career_goal = st.text_input(
    "What is your career goal?",
    placeholder="e.g. Explore careers in AI and finance"
)


# Generate a personalized roadmap
if st.button("Generate AI Roadmap"):

    # Retrieve Pathly's saved recommendations
    saved_recs = st.session_state.get(
        "pathly_recommendations"
    )

    saved_interests = st.session_state.get(
        "pathly_interests"
    )

    # Validate the student's inputs
    if not career_goal.strip():
        st.warning("Please enter a career goal.")

    elif saved_recs is None:
        st.warning("Generate your Pathly recommendations first.")

    elif interests != saved_interests:
        st.warning(
            "Your interests have changed. "
            "Please generate your Pathly recommendations again."
        )

    else:
        try:
            with st.spinner("Generating your AI roadmap..."):

                roadmap = generate_roadmap(
                    interests=saved_interests,
                    experience_level=experience_level,
                    career_goal=career_goal.strip(),
                    courses=saved_recs["courses"],
                    projects=saved_recs["projects"],
                    careers=saved_recs["careers"],
                    api_key=st.secrets["GEMINI_API_KEY"]
                )

            # Remember the generated roadmap
            st.session_state["pathly_roadmap"] = roadmap

            # Remember which inputs created it
            st.session_state["pathly_roadmap_profile"] = {
                "interests": interests.copy(),
                "experience_level": experience_level,
                "career_goal": career_goal.strip()
            }

        except Exception as error:
            st.error(
                "Unable to generate the roadmap. "
                "Please try again."
            )
            print("Roadmap error:", type(error).__name__)



# Describe the currently selected inputs
current_profile = {
    "interests": interests.copy(),
    "experience_level": experience_level,
    "career_goal": career_goal.strip()
}

# Only show a roadmap matching the current inputs
if (
    st.session_state.get("pathly_roadmap")
    and st.session_state.get("pathly_roadmap_profile")
        == current_profile
    and st.session_state.get("pathly_interests")
        == interests
):
    st.success("Your personalized roadmap is ready!")

    st.markdown(
        st.session_state["pathly_roadmap"]
    )
