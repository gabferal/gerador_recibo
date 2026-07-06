
import streamlit as st
from datetime import date

# Configuração da página e estilo
st.set_page_config(page_title="Gerador de Recibos Profissional", layout="centered")

# CSS para o estilo profissional (Verde Oliva, Dourado, Branco)
st.markdown("""
    <style>
        .recibo-container {
            background-color: #ffffff;
            border: 2px solid #556B2F; /* Verde Oliva */
            padding: 30px;
            border-radius: 10px;
            color: #333;
        }
        .header {
            color: #556B2F;
            border-bottom: 2px solid #DAA520; /* Dourado */
            padding-bottom: 10px;
            margin-bottom: 20px;
            text-align: center;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            border-top: 1px solid #DAA520;
            padding-top: 10px;
        }
        .highlight {
            color: #556B2F;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📄 Gerador de Recibos")

# Formulario
with st.form("recibo_form"):
    st.subheader("Informações do Recibo")
    logo_url = st.text_input("Link da imagem do logotipo (URL):")
    
    col1, col2 = st.columns(2)
    with col1:
        valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
    with col2:
        data = st.date_input("Data", date.today())
    
    st.divider()
    st.subheader("Dados do Pagador")
    recebido_de = st.text_input("Recebido de:")
    
    st.subheader("Dados do Recebedor (Empresa)")
    nome_empresa = st.text_input("Nome da sua Empresa:")
    telefone_empresa = st.text_input("Telefone (Opcional):")
    doc_empresa = st.text_input("CPF/CNPJ (Opcional):")
    
    referente_a = st.text_area("Referente a:")
    forma_pagamento = st.radio("Forma de Pagamento:", ["Dinheiro", "PIX", "Cheque"])
    
    btn_gerar = st.form_submit_button("Gerar Recibo")

# Exibição do Recibo
if btn_gerar:
    st.markdown("""
    <div class="recibo-container">
        <div class="header">
            <h1>RECIBO</h1>
        </div>
    """, unsafe_allow_html=True)
    
    if logo_url:
        st.image(logo_url, width=150)
    
    st.write(f"**Valor:** R$ {valor:,.2f}")
    st.write(f"**Data:** {data.strftime('%d/%m/%Y')}")
    st.write(f"**Recebido de:** {recebido_de}")
    st.write(f"**Referente a:** {referente_a}")
    st.write(f"**Forma de Pagamento:** {forma_pagamento}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.write(f"---")
    st.write(f"**Recebido por:** {nome_empresa}")
    if telefone_empresa: st.write(f"**Contato:** {telefone_empresa}")
    if doc_empresa: st.write(f"**Documento:** {doc_empresa}")
    
    st.markdown("""
        <div class="footer">
            <br><br>__________________________________________<br>Assinatura do Recebedor
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("Para imprimir: Pressione Ctrl+P (ou Cmd+P no Mac) e salve como PDF.")
