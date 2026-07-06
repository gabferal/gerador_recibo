# Para atender à solicitação:
# 1. Layout mais elaborado e profissional.
# 2. Logotipo local (usando base64 para incluir a imagem diretamente no HTML).
# 3. Logotipo posicionado no canto superior esquerdo com tamanho controlado.
# 4. Gerar o código Python (Streamlit) que faz isso.

# Vamos assumir que a imagem será carregada no Streamlit e processada.

streamlit_code_v3 = """
import streamlit as st
import base64
from datetime import date
from io import BytesIO

st.set_page_config(page_title="Gerador de Recibos Premium", layout="centered")

# Função para converter imagem para base64
def get_image_base64(uploaded_file):
    image_data = uploaded_file.getvalue()
    return base64.b64encode(image_data).decode()

# Estilo CSS Profissional
st.markdown(\"\"\"
    <style>
        .recibo-wrapper {
            background-color: #f9f9f9;
            padding: 50px;
            border: 1px solid #ddd;
        }
        .recibo-card {
            background-color: #ffffff;
            padding: 40px;
            border-left: 10px solid #556B2F; /* Verde Oliva */
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        .header-section {
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 2px solid #DAA520; /* Dourado */
            padding-bottom: 20px;
            margin-bottom: 30px;
        }
        .logo-container {
            width: 120px;
        }
        .title-text {
            color: #556B2F;
            font-size: 32px;
            font-weight: bold;
            text-transform: uppercase;
        }
        .content-body {
            line-height: 1.6;
            color: #444;
            font-size: 18px;
        }
        .footer-sign {
            margin-top: 60px;
            text-align: center;
            border-top: 1px solid #556B2F;
            padding-top: 10px;
        }
    </style>
\"\"\", unsafe_allow_html=True)

st.title("💼 Gerador de Recibos Premium")

with st.form("recibo_form"):
    uploaded_logo = st.file_uploader("Carregue o logotipo da empresa", type=['png', 'jpg', 'jpeg'])
    
    col1, col2 = st.columns(2)
    with col1:
        valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
    with col2:
        data = st.date_input("Data", date.today())
    
    recebido_de = st.text_input("Recebido de:")
    referente_a = st.text_area("Referente a:")
    forma_pagamento = st.selectbox("Forma de Pagamento:", ["Dinheiro", "PIX", "Cheque"])
    
    nome_empresa = st.text_input("Nome da sua Empresa:")
    telefone_empresa = st.text_input("Telefone:")
    doc_empresa = st.text_input("CPF/CNPJ:")
    
    btn_gerar = st.form_submit_button("Gerar Recibo Profissional")

if btn_gerar:
    logo_html = ""
    if uploaded_logo:
        b64 = get_image_base64(uploaded_logo)
        logo_html = f'<div class="logo-container"><img src="data:image/png;base64,{b64}" style="width:100%"></div>'

    html_content = f\"\"\"
    <div class="recibo-wrapper">
        <div class="recibo-card">
            <div class="header-section">
                {logo_html}
                <div class="title-text">Recibo</div>
            </div>
            <div class="content-body">
                <p>Recebi(emos) de <b>{recebido_de}</b> a importância de <b>R$ {valor:,.2f}</b>.</p>
                <p><b>Referente a:</b> {referente_a}</p>
                <p><b>Forma de Pagamento:</b> {forma_pagamento}</p>
                <p><b>Data:</b> {data.strftime('%d/%m/%Y')}</p>
            </div>
            <div class="footer-sign">
                <p><b>{nome_empresa}</b><br>
                {telefone_empresa} | {doc_empresa}</p>
            </div>
        </div>
    </div>
    \"\"\"
    st.markdown(html_content, unsafe_allow_html=True)
    st.download_button("Download HTML", data=html_content, file_name="recibo_profissional.html", mime="text/html")
"""

with open("gerador_recibo_premium.py", "w", encoding="utf-8") as f:
    f.write(streamlit_code_v3)
