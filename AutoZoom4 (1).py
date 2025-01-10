#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fpdf import FPDF
import tkinter as tk
from tkinter import filedialog, messagebox

class PDFOrcamento(FPDF):
    def header(self):
        if hasattr(self, 'logomarca') and self.logomarca:
            self.image(self.logomarca, 10, 8, 50)  # Aumentando o tamanho da logomarca
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
    pdf.cell(70, 10, 'DESCRICAO', border=1)  # Aumentando largura de DESCRICAO
    pdf.cell(40, 10, 'MARCA', border=1)  # Diminuindo largura de MARCA
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
        pdf.cell(70, 10, descricao, border=1)  # Aumentando largura de DESCRICAO
        pdf.cell(40, 10, marca, border=1)  # Diminuindo largura de MARCA
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

    # Soma do valor do frete
    if frete:
        total_final += float(frete)

    pdf.cell(140, 10, 'TOTAL:', align='R')
    pdf.cell(30, 10, f'R$ {total_final:.2f}', ln=True, align='C')

    # Salvar PDF
    pdf.output('orcamento.pdf')

def selecionar_logomarca():
    caminho = filedialog.askopenfilename(title="Selecione a logomarca", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
    if caminho:
        logomarca_entry.delete(0, tk.END)
        logomarca_entry.insert(0, caminho)

def adicionar_item():
    descricao = descricao_entry.get()
    marca = marca_entry.get()
    quantidade = quantidade_entry.get()
    preco = preco_entry.get()

    # Verifica se todos os campos estão preenchidos
    if descricao and marca and quantidade and preco:  
        try:
            # Convertendo quantidade e preço para os tipos corretos
            quantidade = int(quantidade)
            preco = float(preco)
            
            # Adiciona o item à lista
            itens.append((descricao, marca, quantidade, preco))
            itens_list.insert(tk.END, f"{descricao} - {marca} - QTD: {quantidade} - R$ {preco:.2f}")

            # Limpa os campos de entrada
            descricao_entry.delete(0, tk.END)
            marca_entry.delete(0, tk.END)
            quantidade_entry.delete(0, tk.END)
            preco_entry.delete(0, tk.END)
        
        except ValueError:
            # Exibe mensagem de erro caso quantidade ou preço não sejam numéricos
            messagebox.showerror("Erro", "Quantidade e Preço devem ser numéricos!")
    else:
        messagebox.showinfo("Informação", "Todos os campos do item devem ser preenchidos corretamente.")

def gerar():
    cliente = cliente_entry.get()
    fornecedor = fornecedor_entry.get()
    cnpj = cnpj_entry.get()
    endereco = endereco_entry.get()
    cep = cep_entry.get()
    cidade = cidade_entry.get()
    frete = frete_entry.get()
    imposto = imposto_entry.get()
    logomarca = logomarca_entry.get()

    gerar_orcamento(cliente, fornecedor, cnpj, endereco, cep, cidade, frete, itens, float(imposto or 0), logomarca)  # Se imposto não for fornecido, usa 0
    messagebox.showinfo("Sucesso", "Orçamento gerado com sucesso!")

# Interface gráfica
janela = tk.Tk()
janela.title("Gerador de Orçamentos")

itens = []

# Campos
tk.Label(janela, text="Cliente:").grid(row=0, column=0)
cliente_entry = tk.Entry(janela)
cliente_entry.grid(row=0, column=1)

tk.Label(janela, text="Fornecedor:").grid(row=1, column=0)
fornecedor_entry = tk.Entry(janela)
fornecedor_entry.grid(row=1, column=1)

tk.Label(janela, text="CNPJ:").grid(row=2, column=0)
cnpj_entry = tk.Entry(janela)
cnpj_entry.grid(row=2, column=1)

tk.Label(janela, text="Endereço:").grid(row=3, column=0)
endereco_entry = tk.Entry(janela)
endereco_entry.grid(row=3, column=1)

tk.Label(janela, text="CEP:").grid(row=4, column=0)
cep_entry = tk.Entry(janela)
cep_entry.grid(row=4, column=1)

tk.Label(janela, text="Cidade:").grid(row=5, column=0)
cidade_entry = tk.Entry(janela)
cidade_entry.grid(row=5, column=1)

tk.Label(janela, text="Frete:").grid(row=6, column=0)
frete_entry = tk.Entry(janela)
frete_entry.grid(row=6, column=1)

tk.Label(janela, text="Taxa de Imposto (%):").grid(row=7, column=0)
imposto_entry = tk.Entry(janela)
imposto_entry.grid(row=7, column=1)

tk.Label(janela, text="Logomarca:").grid(row=8, column=0)
logomarca_entry = tk.Entry(janela)
logomarca_entry.grid(row=8, column=1)
tk.Button(janela, text="Selecionar", command=selecionar_logomarca).grid(row=8, column=2)

# Adicionar itens
tk.Label(janela, text="Descrição do Item:").grid(row=9, column=0)
descricao_entry = tk.Entry(janela)
descricao_entry.grid(row=9, column=1)

tk.Label(janela, text="Marca:").grid(row=10, column=0)
marca_entry = tk.Entry(janela)
marca_entry.grid(row=10, column=1)

tk.Label(janela, text="Quantidade:").grid(row=11, column=0)
quantidade_entry = tk.Entry(janela)
quantidade_entry.grid(row=11, column=1)

tk.Label(janela, text="Preço:").grid(row=12, column=0)
preco_entry = tk.Entry(janela)
preco_entry.grid(row=12, column=1)

tk.Button(janela, text="Adicionar Item", command=adicionar_item).grid(row=13, column=0, columnspan=2)

# Listbox para mostrar itens
itens_list = tk.Listbox(janela, height=10, width=50)
itens_list.grid(row=14, column=0, columnspan=3)

tk.Button(janela, text="Gerar Orçamento", command=gerar).grid(row=15, column=0, columnspan=3)

janela.mainloop()

