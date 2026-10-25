# Pathly

Pathly is a career exploration application built with Python and Streamlit. It helps students discover relevant courses, project ideas, and potential career paths based on their interests.

## Features
- Select from multiple interest areas
- View recommended courses
- Explore project ideas
- See related career options
- Access course links directly

## Tech Stack
- Python
- Streamlit

## Project Structure
- `app.py` — user interface
- `recommender.py` — recommendation logic
- `data/rules.py` — recommendation data
- `requirements.txt` — dependencies


### New: Personalized AI Roadmaps

I extended Pathly's original rule-based recommendation engine with Google's Gemini API to generate personalized three-step learning roadmaps.

Students can:
- Select their interests, experience level, and career goal.
- Explore course, project, and career recommendations from Pathly's existing dataset.
- Generate a personalized AI roadmap explaining which skills to develop, what to build, and why each step matters.

### How It Works

1. **Student inputs:** Streamlit collects interests, experience level, and career goals.
2. **Recommendation engine:** `recommender.py` retrieves relevant courses, projects, and careers from `data/rules.py`.
3. **AI integration:** `ai_explainer.py` sends the student profile and recommendations to Gemini.
4. **Roadmap generation:** Gemini produces a three-step learning plan grounded in Pathly's recommendation data.

### Tech Stack

- **Python:** Application logic and recommendation engine
- **Streamlit:** Interactive web application
- **Google Gemini API:** Personalized roadmap generation
- **Git/GitHub:** Version control

### AI Evaluation and Limitations

During initial testing, I evaluated roadmaps for beginner students interested in finance and machine learning.

The first prompt produced relevant recommendations but included external resource links that required verification. I revised the prompt to improve learning progression, reduce unnecessary detail, and avoid generating external URLs.

The revised output followed a clearer three-step progression and contained no URLs. Further testing is planned to assess resource grounding and consistency across different student profiles.

### Future Improvements

- Automated evaluation of AI-generated recommendations
- User feedback collection
- Structured output validation
- MCP-based integration with external learning resources

## How to Run
```bash
source venv/bin/activate
streamlit run app.py