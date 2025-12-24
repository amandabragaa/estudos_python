import pandas as pd

# Acessar a base de dados
def load_data():
    contracts = pd.read_csv("data/churn_contracts.csv")
    customers = pd.read_csv("data/churn_customers.csv")
    services = pd.read_csv("data/churn_services.csv")
    return contracts, customers, services
