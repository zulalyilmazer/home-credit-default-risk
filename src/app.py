import streamlit as st
from google.cloud import bigquery

st.title("Home Credit Finansal Analiz Paneli")

st.write("BigQuery bağlantısı test ediliyor...")

client = bigquery.Client.from_service_account_json("dbt-zulalyilmazer.json")

query = """
SELECT *
FROM `event-test-487817.dbt_zulal.mart_finance_summary`
LIMIT 5
"""

try:
    df = client.query(query).to_dataframe()
    st.success("Bağlantı başarılı! İşte ilk 5 satır:")
    st.dataframe(df)

except Exception as e:
    st.error(f"Bağlantı hatası: {e}")

df = client.query(query).to_dataframe()

st.success("Bağlantı başarılı! İlk 5 satır:")

st.dataframe(df)

