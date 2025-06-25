import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Logging config
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Database engine
engine = create_engine('sqlite:///inventory.db')

# Ingest function
def ingest_db(df, table_name, engine):
    '''This function ingests the DataFrame into the database'''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    logging.info(f"Ingested table: {table_name}")

# Load CSVs and ingest
def load_raw_data():
    '''This function loads CSVs as DataFrames and ingests them into DB'''
    start = time.time()
    for file in os.listdir('../data'):
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join('../data', file))
            logging.info(f'Ingesting {file} into db...')
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start) / 60
    logging.info('----------Ingestion Complete-----------')
    logging.info(f'Total Time Taken: {total_time:.2f} minutes')

# Run only if executed directly
if __name__ == '__main__':
    load_raw_data()  # ✅ Call the function with parentheses
