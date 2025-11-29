import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

import streamlit as st
from src.infer_pretrained import generate_sql
from pathlib import Path

'''st.set_page_config(page_title="Text-to-SQL (Groq)", layout="centered")
st.title("Text → SQL Demo (Groq Llama 3.1 – 8B Instant)")
'''
st.title("Text to SQL Generator")
st.header("Generate SQL query from natural language")

# DB existence check (only for future execution)
'''if not Path("data/company.db").exists():
    st.warning("Sample database not found. Run `python src/create_db.py` first.")
'''

question = st.text_input("Enter your question", "")
schema = st.text_input("Schema (optional)", "Users(Id, NAME, AGE)")

if st.button("Generate SQL"):
    if not question.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Generating SQL using Groq..."):    # st.spinner() used to display the temporary loading animation with a message while executing the bolck of code 
            result = generate_sql(question, schema)

        if result["error"]:
            st.error(f"Error: {result['error']}")
        else:
            st.subheader("Generated SQL")
            st.code(result["sql"])
            st.markdown("---")  #used for seperation line
            st.success("Query Generated!!")