import sys
import os
import plotly.express as px


# Adiciona o diretório raiz do projeto ao sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Agora faça os imports
from scripts.data_loading import load_data
from scripts.data_cleaning import clean_contracts, clean_customers, clean_services
from scripts.kpi_calculations import calculate_kpis
import streamlit as st

# Load and clean the data
contracts, customers, services = load_data()
contracts = clean_contracts(contracts)
customers = clean_customers(customers)
services = clean_services(services)

# Calculate KPIs
kpis = calculate_kpis(contracts, customers, services)



# Streamlit App
st.title("Telecom Churn Analysis Dashboard")

# KPIs
st.write("### Key Performance Indicators (KPIs)")
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", kpis["Total Customers"])
col2.metric("Churn Rate", f"{kpis['Churn Rate']:.2%}")
col3.metric("Total Revenue", f"${kpis['Total Revenue']:.2f}")

# Divider
st.markdown("---")

# Gráfico de distribuição por tipo de contrato
st.write("### Contract Distribution")
if not kpis["Contract Distribution"].empty:
    st.bar_chart(kpis["Contract Distribution"])
else:
    st.write("No data available to display.")



# Chatgpt crie este grafico aqui :
  # Um grafico de pizza que mostre clientes cancelados e os não cancelados

# Gráfico de Pizza: Clientes Cancelados vs Não Cancelados
st.write("### Churn Analysis: Canceled vs. Not Canceled")

churn_distribution = contracts['Churn'].value_counts()

if not churn_distribution.empty:
    churn_pie_chart = px.pie(
        values=churn_distribution.values,
        names=churn_distribution.index,
        title="Churn Analysis: Percentage of Canceled and Active Customers",
        labels={"label": "Churn Status", "value": "Count"}
    )
    st.plotly_chart(churn_pie_chart)
else:
    st.write("No churn data available to display.")