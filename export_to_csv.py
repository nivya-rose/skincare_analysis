import sqlite3
import pandas as pd

#connect to sqlite db
conn=sqlite3.connect("D:/SkinCareAnalysys/skincare_dashboard/db.sqlite3")

#list of django tables
tables=["products_product", "products_ingredient", "products_review"]

# export each table to csv

for table in tables:
    df= pd.read_sql_query(f"SELECT * FROM {table}", conn)
    df.to_csv(f"{table}.csv",index=False, encoding='utf-8')
    print(f"Exported {table} to {table}.csv")

conn.close()
print("All tables exported successfully.")