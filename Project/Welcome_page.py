import streamlit as st

st.set_page_config(
    page_title="Resume Screening",
    page_icon="👋",
)
html_str = f"""<html><body>
                <p> Welcome to Resume Screening App! 👋 </p>
                <p> In today's industry its difficult to go through each resume and select that particular candidates who are associated to a Job Description .</p>
                <p> So we designed this app, Where you will give the input of JD file and a set of resumes and it will return the top 5 resumes whose score matches to the given Job Description. </p>
                <p> Click on the left arrow to register, login and then upload the files of Job Description and multiple resume files.</p>
                </html></body>"""

st.markdown(html_str, unsafe_allow_html=True)

