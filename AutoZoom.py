#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install fpdf')


# In[ ]:


from fpdf import FPDF
import tkinter as tk
from tkinter import filedialog, messagebox

class PDFOrcamento(FPDF):
    def header(self):
        if hasattr(self, 'logomarca') and self.logomarca:
            self.image(self.logomarca, 10, 8, 33)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'ORCAMENTO', border=0, ln=1, align='C')
        self.ln(20)

def gerar_orcamento(cliente, fornecedor, itens, imposto, logomarca):
    pdf = PDFOrcamento()
    pdf.logomarca = logomarca
    pdf.add_page()

    # Informações do cliente e fornecedor
    pdf.set_font('Arial', '', 10)
    pdf.cell(100, 10, f'CLIENTE: {cliente}', ln=False)
    pdf.cell(0, 10, f'FORNECEDOR: {fornecedor}', ln=True)
    pdf.ln(5)

    # Tabela de itens
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(80, 10, 'DESCRICAO', border=1)
    pdf.cell(30, 10, 'QTD', border=1, align='C')
    pdf.cell(30, 10, 'PRECO', border=1, align='C')
    pdf.cell(30, 10, 'TOTAL', border=1, align='C')
    pdf.ln()

    pdf.set_font('Arial', '', 10)
    subtotal = 0
    for item in itens:
        descricao, qtd, preco = item
        total = qtd * preco
        subtotal += total
        pdf.cell(80, 10, descricao, border=1)
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
    quantidade = quantidade_entry.get()
    preco = preco_entry.get()

    if not descricao or not quantidade or not preco:
        messagebox.showerror("Erro", "Preencha todos os campos do item.")
        return

    itens.append((descricao, int(quantidade), float(preco)))
    itens_list.insert(tk.END, f"{descricao} - QTD: {quantidade} - R$ {preco}")
    descricao_entry.delete(0, tk.END)
    quantidade_entry.delete(0, tk.END)
    preco_entry.delete(0, tk.END)

def gerar():
    cliente = cliente_entry.get()
    fornecedor = fornecedor_entry.get()
    imposto = imposto_entry.get()
    logomarca = logomarca_entry.get()

    if not cliente or not fornecedor or not imposto:
        messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
        return

    if not itens:
        messagebox.showerror("Erro", "Adicione pelo menos um item.")
        return

    gerar_orcamento(cliente, fornecedor, itens, float(imposto), logomarca)
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

tk.Label(janela, text="Taxa de Imposto (%):").grid(row=2, column=0)
imposto_entry = tk.Entry(janela)
imposto_entry.grid(row=2, column=1)

tk.Label(janela, text="Logomarca:").grid(row=3, column=0)
logomarca_entry = tk.Entry(janela)
logomarca_entry.grid(row=3, column=1)
tk.Button(janela, text="Selecionar", command=selecionar_logomarca).grid(row=3, column=2)

# Adicionar itens
tk.Label(janela, text="Descrição do Item:").grid(row=4, column=0)
descricao_entry = tk.Entry(janela)
descricao_entry.grid(row=4, column=1)

tk.Label(janela, text="Quantidade:").grid(row=5, column=0)
quantidade_entry = tk.Entry(janela)
quantidade_entry.grid(row=5, column=1)

tk.Label(janela, text="Preço Unitário (R$):").grid(row=6, column=0)
preco_entry = tk.Entry(janela)
preco_entry.grid(row=6, column=1)

tk.Button(janela, text="Adicionar Item", command=adicionar_item).grid(row=7, column=1)

# Lista de itens
itens_list = tk.Listbox(janela, height=10, width=50)
itens_list.grid(row=8, column=0, columnspan=3)

# Botão para gerar orçamento
tk.Button(janela, text="Gerar Orçamento", command=gerar).grid(row=9, column=1)

janela.mainloop()

