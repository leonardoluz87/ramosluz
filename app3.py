#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

def calcular_energia_cinetica(massa_g, velocidade_m_s):
    # Converte a massa de gramas para quilogramas
    massa_kg = massa_g / 1000
    # Calcula a energia cinética
    energia_cinetica = 0.5 * massa_kg * (velocidade_m_s ** 2)
    return energia_cinetica

# Título da aplicação
st.title("Cálculo da Energia Cinética de Partículas")

# Recebe os dados de entrada para a primeira esfera
massa_g1 = st.number_input("Digite a massa da primeira esfera em gramas:", min_value=0.0, step=0.1)
velocidade_m_s1 = st.number_input("Digite a velocidade da primeira esfera em metros por segundo:", min_value=0.0, step=0.1)

# Recebe os dados de entrada para a segunda esfera
massa_g2 = st.number_input("Digite a massa da segunda esfera em gramas:", min_value=0.0, step=0.1)
velocidade_m_s2 = st.number_input("Digite a velocidade da segunda esfera em metros por segundo:", min_value=0.0, step=0.1)

# Calcula a energia cinética de cada esfera
energia1 = calcular_energia_cinetica(massa_g1, velocidade_m_s1)
energia2 = calcular_energia_cinetica(massa_g2, velocidade_m_s2)

# Exibe os resultados das esferas
energia_total_esferas = energia1 + energia2
massa_total_esferas = massa_g1 + massa_g2  # Soma das massas das esferas em gramas

# Dados para a colisão de 2 prótons:
massa_proton = 1.67e-27  # massa de um próton em kg
velocidade_proton = 1e6  # velocidade dos prótons em m/s

# Calcula a energia cinética de dois prótons
energia_proton = calcular_energia_cinetica(massa_proton * 1000, velocidade_proton)  # multiplicando por 1000 para converter a massa para gramas

# Como são dois prótons, a energia total é o dobro de um
energia_total_protons = 2 * energia_proton
massa_total_protons = 2 * (massa_proton * 1000)  # Massa total dos dois prótons em gramas

# Exibe os resultados das esferas
st.subheader("Resultados para as Esferas:")
st.write(f"A energia cinética total das esferas antes da colisão é: {energia_total_esferas:.4e} Joules")
st.write(f"A massa total das esferas é: {massa_total_esferas} gramas")

# Exibe os resultados dos prótons
st.subheader("Resultados para os Prótons:")
st.write(f"A energia cinética total de dois prótons a {velocidade_proton} m/s é: {energia_total_protons:.4e} Joules")
st.write(f"A massa total dos prótons é: {massa_total_protons:.4e} gramas")

# Dividindo a energia total pela massa total para as esferas
energia_por_massa_esferas = energia_total_esferas / massa_total_esferas
energia_por_massa_protons = energia_total_protons / massa_total_protons

# Exibe o resultado
st.subheader("Energia Cinética por Unidade de Massa:")
st.write(f"A energia cinética por unidade de massa das esferas é: {energia_por_massa_esferas:.4e} Joules/grama")
st.write(f"A energia cinética por unidade de massa dos prótons é: {energia_por_massa_protons:.4e} Joules/grama")

