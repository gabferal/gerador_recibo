import streamlit as st
from datetime import date

# Configuração da página
st.set_page_config(page_title="Gerador de Recibos", layout="centered")

st.title("📄 Gerador de Recibos")

# Formulario
with st.form("recibo_form"):
    logo_url = st.text_input("Link da imagem do logotipo (URL):")
    col1, col2 = st.columns(2)
    with col1:
        valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
    with col2:
        data = st.date_input("Data", date.today())
    
    recebido_de = st.text_input("Recebido de:")
    referente_a = st.text_area("Referente a:")
    
    forma_pagamento = st.radio("Forma de Pagamento:", ["Dinheiro", "PIX", "Cheque"])
    
    btn_gerar = st.form_submit_button("Gerar Recibo")

# Exibição do Recibo
if btn_gerar:
    st.markdown("---")
    if logo_url:
        st.image(logo_url, width=150)
    
    st.header("RECIBO")
    st.write(f"**Valor:** R$ {valor:,.2f}")
    st.write(f"**Data:** {data.strftime('%d/%m/%Y')}")
    st.write(f"**Recebido de:** {recebido_de}")
    st.write(f"**Referente a:** {referente_a}")
    st.write(f"**Forma de Pagamento:** {forma_pagamento}")
    
    st.markdown("<br><br>__________________________________________<br>Assinatura", unsafe_allow_html=True)
    
    st.info("Para imprimir: Pressione Ctrl+P (ou Cmd+P no Mac) e salve como PDF.")