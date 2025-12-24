def calculate_kpis(contracts, customers, services):
    """Calculate key performance indicators."""
    # Total de clientes
    total_customers = contracts['customerID'].nunique()

    # Taxa de churn
    churn_rate = contracts['Churn'].value_counts(normalize=True).get('Yes', 0)

    # Receita mensal total
    total_revenue = contracts['MonthlyCharges'].sum()

    # Distribuição por tipo de contrato
    contract_distribution = contracts['Contract'].value_counts()

    kpis = {
        "Total Customers": total_customers,
        "Churn Rate": churn_rate,
        "Total Revenue": total_revenue,
        "Contract Distribution": contract_distribution,
    }
    return kpis
