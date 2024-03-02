import pandas as pd
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine("mysql+pymysql://root:24Zorg42@localhost/recipes")

# Create a connection and perform a query
with engine.connect() as conn:
    df = pd.read_sql("SELECT * FROM recipes", conn)

# Print all column names
print(df.columns.tolist())
