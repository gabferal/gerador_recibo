import streamlit as st
import base64
from datetime import date

# Configuração essencial da página (deve ser o primeiro comando)
st.set_page_config(page_title="Gerador de Recibos", layout="centered")

# Função segura para processar imagem em base64
def get_image_base64(uploaded_file):
    return base64.b64encode(uploaded_file.getvalue()).decode()

# Título
st.title("📄 Gerador de Recibos")

# Formulário
with st.form("recibo_form"):
    st.subheader("Configurações")
    uploaded_logo = st.file_uploader("Logotipo (Opcional)", type=['png', 'jpg', 'jpeg'])
    
    col1, col2 = st.columns(2)
    with col1:
        valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
    with col2:
        data = st.date_input("Data", date.today())
    
    recebido_de = st.text_input("Recebido de:")
    referente_a = st.text_area("Referente a:")
    forma_pagamento = st.selectbox("Forma de Pagamento:", ["Dinheiro", "PIX", "Cheque"])
    
    st.subheader("Dados do Recebedor")
    nome_empresa = st.text_input("Nome da Empresa / Recebedor:")
    telefone = st.text_input("Telefone:")
    cpf_cnpj = st.text_input("CPF/CNPJ:")
    
    btn_gerar = st.form_submit_button("Gerar Recibo")

# Lógica de processamento
if btn_gerar:
    # Preparação da imagem
    logo_html = ""
    if uploaded_logo:
        b64 = get_image_base64(uploaded_logo)
        logo_html = f'<div style="width: 120px;"><img src="data:image/png;base64,{b64}" style="width:100%"></div>'

    # Estrutura HTML consolidada para evitar conflitos de renderização
    html_content = f"""
    <div style="font-family: sans-serif; border: 2px solid #556B2F; padding: 30px; border-radius: 10px; max-width: 600px; margin: auto;">
        <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #DAA520; margin-bottom: 20px;">
            {logo_html}
            <h1 style="color: #556B2F;">RECIBO</h1>
        </div>
        <p>Recebi de <b>{recebido_de}</b> a importância de <b>R$ {valor:,.2f}</b>.</p>
        <p><b>Referente a:</b> {referente_a}</p>
        <p><b>Forma de Pagamento:</b> {forma_pagamento}</p>
        <p><b>Data:</b> {data.strftime('%d/%m/%Y')}</p>
        <div style="margin-top: 40px; text-align: right;">
            __________________________________________<br>
            <b>{nome_empresa}</b><br>{telefone}<br>{cpf_cnpj}
        </div>
    </div>
    """
    
    # Renderização segura
    st.markdown(html_content, unsafe_allow_html=True)
    st.download_button("Download HTML", data=html_content, file_name="recibo.html", mime="text/html")
