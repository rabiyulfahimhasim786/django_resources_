import pandas as pd
import sqlite3
from sqlite3 import Error
db_file = 'db.sqlite3'
conn = sqlite3.connect(db_file, isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
db_df = pd.read_sql_query("SELECT * FROM polls_person", conn)
db_df.to_csv('database.csv', index=False)
# Python program to explain os.mkdir() method