import pandas as pd

def clean_contracts(contracts):
    """Clean the contracts dataset."""
    # Verifica valores ausentes
    contracts.dropna(subset=['customerID'], inplace=True)

    # Remove duplicatas
    contracts.drop_duplicates(inplace=True)

    # Converte a coluna TotalCharges para numérico (tratando valores não numéricos)
    contracts['TotalCharges'] = pd.to_numeric(contracts['TotalCharges'], errors='coerce')
    contracts['TotalCharges'].fillna(0, inplace=True)

    return contracts

def clean_customers(customers):
    """Clean the customers dataset."""
    customers.drop_duplicates(inplace=True)
    return customers

def clean_services(services):
    """Clean the services dataset."""
    services.drop_duplicates(inplace=True)
    return services


