# Use this file to import policy tables (once per version)
import pandas as pd
import numpy as np
from datetime import datetime
from components import create_connection, insert_data
from models import PolicyTables
import time
import sys
import os


def main():
    database = 'test.db'
    policy_tables_folder = 'data/policy-tables/'
    
    # create database connection
    conn = create_connection(database)

    # read in tables
    start = time.time()
    print('reading policy tables at ' + policy_tables_folder)
    for table in os.listdir(policy_tables_folder):
        # read in table
        table_path = os.path.join(policy_tables_folder, table)
        df = pd.read_csv(table_path)
        
        # read in sql file
        sql_file_name = 'insert_' + table[:-4].replace('-', '_') + '.sql'
        sql_file_path = os.path.join('sql/', sql_file_name)
        
        # insert data into database
        with conn:
            print('inserting ' + table[:-4].replace('-', '_'))
            for _, row in df.iterrows():
                data = tuple(row)
                insert_data(conn, sql_file_path, data)
    
    conn.close()
        
    print(f'{round((time.time() - start), 2)} seconds elapsed')

if __name__ == '__main__':
    main()