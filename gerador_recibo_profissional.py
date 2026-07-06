import streamlit as st
from datetime import date
import base64

# Configuração da página
st.set_page_config(page_title="Gerador de Recibos Profissional", layout="centered")

# CSS para o estilo profissional (Verde Oliva, Dourado, Branco)
st.markdown("""
    <style>
        .recibo-box {
            font-family: 'Arial', sans-serif;
            background-color: #ffffff;
            border: 3px solid #556B2F; /* Verde Oliva */
            padding: 40px;
            max-width: 600px;
            margin: auto;
            color: #333;
        }
        .header-recibo {
            text-align: center;
            color: #556B2F;
            border-bottom: 3px solid #DAA520; /* Dourado */
            margin-bottom: 20px;
        }
        .info-row {
            margin-bottom: 10px;
            font-size: 16px;
        }
        .footer-recibo {
            margin-top: 60px;
            text-align: center;
            border-top: 1px solid #DAA520;
            padding-top: 20px;
            color: #556B2F;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📄 Gerador de Recibos")

# Formulario
with st.form("recibo_form"):
    st.subheader("Configurações do Recibo")
    logo_url = st.text_input("Link do logotipo (Opcional):")
    
    col1, col2 = st.columns(2)
    with col1:
        valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
    with col2:
        data = st.date_input("Data", date.today())
    
    recebido_de = st.text_input("Recebido de:")
    referente_a = st.text_area("Referente a:")
    forma_pagamento = st.selectbox("Forma de Pagamento:", ["Dinheiro", "PIX", "Cheque"])
    
    st.divider()
    st.subheader("Dados do Recebedor")
    nome_empresa = st.text_input("Nome da Empresa / Recebedor:")
    telefone = st.text_input("Telefone (Opcional):")
    cpf_cnpj = st.text_input("CPF/CNPJ (Opcional):")
    
    btn_gerar = st.form_submit_button("Gerar Recibo Profissional")

# Geração do HTML
if btn_gerar:
    html_content = f"""
    <div class="recibo-box">
        <div class="header-recibo">
            <h1>RECIBO</h1>
        </div>
        <p>Recebi(emos) de <b>{recebido_de}</b> a importância de <b>R$ {valor:,.2f}</b>.</p>
        <div class="info-row"><b>Referente a:</b> {referente_a}</div>
        <div class="info-row"><b>Forma de Pagamento:</b> {forma_pagamento}</div>
        <div class="info-row"><b>Data:</b> {data.strftime('%d/%m/%Y')}</div>
        
        <br>
        <div style="text-align: right;">
            <p>__________________________________________<br>
            <b>{nome_empresa}</b><br>
            {telefone}<br>
            {cpf_cnpj}</p>
        </div>
        <div class="footer-recibo">
            Documento emitido com finalidade comprobatória.
        </div>
    </div>
    """
    
    # Exibe o HTML renderizado
    st.markdown(html_content, unsafe_allow_html=True)
    
    # Botão para download do HTML
    st.download_button(
        label="Download como HTML",
        data=html_content,
        file_name="recibo.html",
        mime="text/html"
    )
    
    st.info("Dica: Use o botão de download ou imprima a tela (Ctrl+P).")
