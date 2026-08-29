import streamlit as st
import clickhouse_connect
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Visiontech Insider Control", layout="wide")

# Настройки подключения к ClickHouse (подтягиваем из нашего Docker)
def load_data():
    try:
        client = clickhouse_connect.get_client(
            host='clickhouse', port=8123,
            username='auditor', password='SecureCH_1787649352_Auth!'
        )
        # Читаем реальные логи из базы
        df = client.query_df("SELECT timestamp, employee_name, event_type, payload_size_mb, risk_score_ai, ai_verdict FROM audit_logs.activity_stream ORDER BY timestamp DESC LIMIT 100")
        return df
    except Exception as e:
        st.error(f"Ошибка подключения к БД: {e}")
        return pd.DataFrame()

df = load_data()

st.title("🛡️ Visiontech Insider Control")
st.subheader("Автономный комплекс поведенческого анализа ИБ (152-ФЗ РФ)")

if not df.empty:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Зафиксировано аномалий", len(df))
    with col2:
        st.metric("Критические риски (AI > 80)", len(df[df['risk_score_ai'] > 80]))

    st.write("---")
    # Красивый scatter-график рисков
    fig = px.scatter(df, x="timestamp", y="risk_score_ai", size="payload_size_mb", 
                     color="event_type", hover_name="employee_name", title="Оперативная лента угроз")
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("### Журнал инцидентов")
    st.dataframe(df, use_container_width=True)
else:
    st.info("База данных пуста. Ожидание логов...")
