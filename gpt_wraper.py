from openai import OpenAI
import streamlit as st

openai_key = st.secrets["OPENAI_KEY"]

client = OpenAI(api_key=openai_key)

def gpt_wraper_message(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(completion.choices[0].message.content)