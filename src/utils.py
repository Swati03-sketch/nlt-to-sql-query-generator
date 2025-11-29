import re

keywords = ["select", "from", "where", "join", "on", "group by", "order by", "having", "limit", "and", "or", "count", "sum", "avg", "min", "max"]
def clean_sql_query(sql_text):
    s = sql_text.strip().rstrip(";")
    s = re.sub(r"\s+", " ", s)
    s = s.strip()
    if not s.lower().startswith("select"):
        raise ValueError("SQL query must starts with SELECT!")
    return s + ";"

