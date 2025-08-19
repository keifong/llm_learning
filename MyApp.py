import streamlit as st
from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def create_study_plan(school, degree, year):
    response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
        "role": "system",
        "content": [    
            {
            "type": "text",
            "text": "# Identity\nYou are a senior academic coach for SIM undergraduates in Computer Science. Your\ngoal is to convert the actual SIM/UoL CS curriculum into effective study techniques,\ntime plans, resource stacks, and exam tactics that improve grades and mastery quickly.\n# Instruction\nRecommend effective study strategies for an undergraduate student pursuing a\nComputer Science degree at Singapore Institute of Management.\nPlan for each of the following:\n1.Effective study techniques\n2.Time management strategies\n3.Resource recommendations\n4.Tips for exam preparation\n# Context\n1. SIM delivers the UoL BSc (Hons) Computer Science in blended mode: Coursera/VLE +\nSIM teaching support, two semesters/year, up to 4 new modules/semester.\n2.Programme structure: 23 modules (8 L4 compulsory, 8 L5 compulsory, 6 L6 electives)\n+ final project.\n3.<more about your curriculum>"
            }
        ]
        },
        {
        "role": "user",
        "content": [    
            {
            "type": "text",
            "text": f"what are some effective study strategies for a {year} undergraduate {degree}  student in {school} at Singapore Institute of Management?"
            }
        ]
        }
    ],
    response_format={
        "type": "text"
    },
    temperature=1,
    max_completion_tokens=512,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response


st.title("SIM Study Planning App")
option_school = st.selectbox(
    "Your School: ",
    ("UOW", "RMIT", "UOL"),
    key="school"
)

option_degree = st.selectbox(
    "Your Degree: ",
    ("Finance", "Computer Science", "Business Management"),
    key="degree"
)

option_year = st.selectbox(
    "Your Year: ",
    ("Year 1", "Year 2", "Year 3", "Pre-U"),
    key="year"
)


if st.button("Generate Plan!"):
    res = create_study_plan(option_school, option_degree, option_year)
    st.markdown(res.choices[0].message.content)