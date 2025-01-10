#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from fpdf import FPDF

class PDFOrcamento(FPDF):
    def header(self):
        if hasattr(self, 'logomarca') and self.logomarca:
            self.image(self.logomarca, 10, 8, 50)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'ORCAMENTO', border=0, ln=1, align='C')
        self.ln(20)

def gerar_orcamento(cliente, fornecedor, cnpj, endereco, cep, cidade, frete, itens, imposto, logomarca):
    pdf = PDFOrcamento()
    pdf.logomarca = logomarca
    pdf.add_page()

    # Informações do cliente e fornecedor
    pdf.set_font('Arial', '', 10)
    pdf.cell(100, 10, f'CLIENTE: {cliente}', ln=False)
    pdf.cell(0, 10, f'FORNECEDOR: {fornecedor}', ln=True)
    pdf.ln(5)
    
    if cnpj:
        pdf.cell(0, 10, f'CNPJ: {cnpj}', ln=True)
    if endereco:
        pdf.cell(0, 10, f'ENDEREÇO: {endereco}', ln=True)
    if cep:
        pdf.cell(0, 10, f'CEP: {cep}', ln=True)
    if cidade:
        pdf.cell(0, 10, f'CIDADE: {cidade}', ln=True)
    pdf.ln(5)

    # Frete
    if frete:
        pdf.cell(0, 10, f'FRETE: {frete}', ln=True)
    pdf.ln(5)

    # Tabela de itens
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(70, 10, 'DESCRICAO', border=1)
    pdf.cell(40, 10, 'MARCA', border=1)
    pdf.cell(30, 10, 'QTD', border=1, align='C')
    pdf.cell(30, 10, 'PRECO', border=1, align='C')
    pdf.cell(30, 10, 'TOTAL', border=1, align='C')
    pdf.ln()

    pdf.set_font('Arial', '', 10)
    subtotal = 0
    for item in itens:
        descricao, marca, qtd, preco = item
        total = qtd * preco
        subtotal += total
        pdf.cell(70, 10, descricao, border=1)
        pdf.cell(40, 10, marca, border=1)
        pdf.cell(30, 10, str(qtd), border=1, align='C')
        pdf.cell(30, 10, f'R$ {preco:.2f}', border=1, align='C')
        pdf.cell(30, 10, f'R$ {total:.2f}', border=1, align='C')
        pdf.ln()

    # Resumo
    pdf.ln(5)
    pdf.cell(140, 10, 'SUBTOTAL:', align='R')
    pdf.cell(30, 10, f'R$ {subtotal:.2f}', ln=True, align='C')

    valor_imposto = subtotal * (imposto / 100)
    total_final = subtotal + valor_imposto

    pdf.cell(140, 10, f'TAX ({imposto}%):', align='R')
    pdf.cell(30, 10, f'R$ {valor_imposto:.2f}', ln=True, align='C')

    if frete:
        total_final += float(frete)

    pdf.cell(140, 10, 'TOTAL:', align='R')
    pdf.cell(30, 10, f'R$ {total_final:.2f}', ln=True, align='C')

    pdf.output('orcamento.pdf')

# Interface gráfica com Streamlit
st.title("Gerador de Orçamentos")

itens = []

# Campos de entrada
cliente = st.text_input("Cliente:")
fornecedor = st.text_input("Fornecedor:")
cnpj = st.text_input("CNPJ:")
endereco = st.text_input("Endereço:")
cep = st.text_input("CEP:")
cidade = st.text_input("Cidade:")
frete = st.text_input("Frete:")
imposto = st.text_input("Taxa de Imposto (%):")
logomarca = st.text_input("Logomarca (caminho do arquivo):")

# Adicionar itens
descricao = st.text_input("Descrição do Item:")
marca = st.text_input("Marca:")
quantidade = st.number_input("Quantidade:", min_value=1, step=1)
preco = st.number_input("Preço:", min_value=0.01, step=0.01)

if st.button("Adicionar Item"):
    if descricao and marca and quantidade and preco:
        itens.append((descricao, marca, int(quantidade), float(preco)))
        st.success(f"Item adicionado: {descricao} - {marca} - QTD: {quantidade} - R$ {preco:.2f}")
    else:
        st.warning("Por favor, preencha todos os campos para adicionar um item.")

# Mostrar os itens adicionados
st.write("Itens adicionados:")
for item in itens:
    st.write(f"{item[0]} - {item[1]} - QTD: {item[2]} - R$ {item[3]:.2f}")

# Botão para gerar o orçamento
if st.button("Gerar Orçamento"):
    if cliente and fornecedor:
        gerar_orcamento(cliente, fornecedor, cnpj, endereco, cep, cidade, frete, itens, float(imposto or 0), logomarca)
        st.success("Orçamento gerado com sucesso!")
        with open("orcamento.pdf", "rb") as f:
            st.download_button("Baixar Orçamento", f, "orcamento.pdf")
    else:
        st.warning("Por favor, preencha os campos obrigatórios.")

