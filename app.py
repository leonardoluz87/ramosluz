#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

# Funções para cálculos
def calcular_quantidade_de_movimento(massa, velocidade):
    return massa * velocidade

def calcular_energia_cinetica(massa, velocidade):
    return 0.5 * massa * velocidade**2

# Título do aplicativo
st.title("Cálculo de Física: Quantidade de Movimento e Energia Cinética")
st.write("Insira os dados abaixo para calcular os valores antes da colisão.")

# Entradas do usuário
distancia = st.number_input("Distância medida na régua (em cm):", min_value=0.0, step=0.1)
peso_gramas = st.number_input("Peso da bola (em gramas):", min_value=0.0, step=0.1)
velocidade = st.number_input("Velocidade da bola (em m/s):", min_value=0.0, step=0.1)

# Botão para calcular
if st.button("Calcular"):
    if peso_gramas > 0 and velocidade > 0:
        # Convertendo peso para kg
        massa_kg = peso_gramas / 1000
        
        # Realizando os cálculos
        quantidade_de_movimento = calcular_quantidade_de_movimento(massa_kg, velocidade)
        energia_cinetica = calcular_energia_cinetica(massa_kg, velocidade)

        # Exibindo os resultados
        st.subheader("Resultados:")
        st.write(f"Massa: {massa_kg:.3f} kg")
        st.write(f"Quantidade de Movimento: {quantidade_de_movimento:.2f} kg·m/s")
        st.write(f"Energia Cinética: {energia_cinetica:.2f} J")
    else:
        st.error("Por favor, insira valores positivos para peso e velocidade.")


# In[ ]:




