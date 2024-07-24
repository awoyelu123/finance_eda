import yaml
from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path  

class RDSDatabaseConnector:

    def __init__(self,):
        self.credentials = {}

    def load_credentials(self):
        with open('credentials.yaml', 'r') as file:
            self.credentials = yaml.safe_load(file)
        return(self.credentials)

    def connect_to_database(self):
        engine = create_engine(f"{self.credentials['DATABASE_TYPE']}+{self.credentials['DBAPI']}://{self.credentials['USER']}:{self.credentials['PASSWORD']}@{self.credentials['HOST']}:{self.credentials['PORT']}/{self.credentials['DATABASE']}")
        engine.execution_options(isolation_level='AUTOCOMMIT').connect()
        engine.connect()
        self.data = pd.read_sql_table('loan_payments',con = engine)
        print("Connection Successful")


    def create_dataframe(self):
        self.df = pd.DataFrame(self.data)

    def save_data_as_csv(self):
        filepath = Path("C:\\Users\\awoye\OneDrive\\Documents\\GitHub\\finance_eda\\data.csv'")  
        filepath.parent.mkdir(parents=True, exist_ok=True)  
        self.df.to_csv(filepath) 

    def shape(self):
        local_data = pd.read_csv("C:\\Users\\awoye\OneDrive\\Documents\\GitHub\\finance_eda\\data.csv'")
        local_df = pd.DataFrame(local_data)

p = RDSDatabaseConnector()
p.shape()

