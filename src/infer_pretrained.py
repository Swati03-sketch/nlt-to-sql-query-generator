from groq import Groq
from src.utils import clean_sql_query
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("GROQ_API_Key")  
MODEL_NAME = "llama-3.1-8b-instant"

client = Groq(api_key=API_KEY)

def generate_sql(question, schema):
    """
    Generate SQL query from a Natural Language Text using Groq API.
    Returns a dict : {"sql":..., "error":...}
    """
    prompt = f"""
    As you are an expert to generate the SQL query from Natural language, 
    so please generate the SQL query based on the following database schema and question.

    Schema : 
    {schema}

    Question : 
    {question}

    Return ONLY a valid SQL query with all necessary clauses.
    """

    try:
        response = client.chat.completions.create(
            model = MODEL_NAME,
            messages = [{"role":"user", "content":prompt}],
            temperature = 0
        )
        sql_raw = response.choices[0].message.content
        try:
            sql_clean = clean_sql_query(sql_raw)
        except ValueError:
            # For DDL commands
            sql_clean = sql_raw.strip().rstrip(";") + ";"

        return {"sql" : sql_clean, "error" : None}
    except Exception as e:
        return {"sql" : None, "error" : str(e)}

'''if __name__ == "__main__":
    question = "Add a column 'email' of type TEXT to the Users table"
    schema = "Users(Id, NAME, AGE)"
    
    result = generate_sql(question, schema)
    
    if result["error"]:
        print("Error generating SQL:", result["error"])
    else:
        print("Generated SQL:", result["sql"]) 
'''