#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Constantes
massa_proton = 1.6726e-27  # kg
energia_colisao_protons = 1.602e-13  # J (aproximadamente 1 MeV em colisões de baixa energia)

# Funções de cálculo
def calcular_tempo(distancia, velocidade):
    return distancia / velocidade

def calcular_aceleracao(velocidade, tempo):
    return velocidade / tempo

def calcular_energia_cinetica(massa, velocidade):
    return 0.5 * massa * velocidade**2

def relacao_energia_massa(energia, massa):
    return energia / massa

# Interface do programa
st.title("Cálculo de Física: Colisão de Esferas e Comparação com Prótons")
st.write("Insira os dados abaixo para calcular as propriedades físicas antes da colisão.")

# Entradas do usuário
velocidade_A = st.number_input("Velocidade da esfera A (em m/s):", min_value=0.0, step=0.1)
velocidade_B = st.number_input("Velocidade da esfera B (em m/s):", min_value=0.0, step=0.1)
distancia_A = st.number_input("Distância percorrida pela esfera A (em m):", min_value=0.0, step=0.1)
distancia_B = st.number_input("Distância percorrida pela esfera B (em m):", min_value=0.0, step=0.1)
massa_A = st.number_input("Massa da esfera A (em kg):", min_value=0.0, step=0.01)
massa_B = st.number_input("Massa da esfera B (em kg):", min_value=0.0, step=0.01)
pressao = st.number_input("Pressão do gás no cilindro (em Pascal):", min_value=0.0, step=100.0)

# Botão para calcular
if st.button("Calcular"):
    if all(v > 0 for v in [velocidade_A, velocidade_B, distancia_A, distancia_B, massa_A, massa_B, pressao]):
        # Cálculos
        tempo_A = calcular_tempo(distancia_A, velocidade_A)
        tempo_B = calcular_tempo(distancia_B, velocidade_B)

        aceleracao_A = calcular_aceleracao(velocidade_A, tempo_A)
        aceleracao_B = calcular_aceleracao(velocidade_B, tempo_B)

        energia_cinetica_A = calcular_energia_cinetica(massa_A, velocidade_A)
        energia_cinetica_B = calcular_energia_cinetica(massa_B, velocidade_B)
        energia_cinetica_total = energia_cinetica_A + energia_cinetica_B

        # Comparação com colisão de prótons
        relacao_protons = relacao_energia_massa(energia_cinetica_total, massa_proton)

        # Exibição dos resultados
        st.subheader("Resultados:")
        st.write(f"Tempo percorrido pela esfera A: {tempo_A:.3f} s")
        st.write(f"Tempo percorrido pela esfera B: {tempo_B:.3f} s")
        st.write(f"Aceleração da esfera A: {aceleracao_A:.3f} m/s²")
        st.write(f"Aceleração da esfera B: {aceleracao_B:.3f} m/s²")
        st.write(f"Energia Cinética da esfera A: {energia_cinetica_A:.3e} J")
        st.write(f"Energia Cinética da esfera B: {energia_cinetica_B:.3e} J")
        st.write(f"Energia Cinética Total antes da colisão: {energia_cinetica_total:.3e} J")

        st.subheader("Comparação com Prótons:")
        st.write(f"Energia em uma colisão de dois prótons: {energia_colisao_protons:.3e} J")
        st.write(f"Relação entre a energia total das esferas e a energia de um próton: {relacao_protons:.3e}")

        st.write(
            """
            **Relação entre Massa e Energia**:
            Segundo a equação de Einstein, \(E = mc^2\), a energia total está diretamente relacionada à massa.
            Neste caso, a energia cinética das esferas antes da colisão é muito maior que a de dois prótons, 
            demonstrando a diferença de escala entre as massas envolvidas.
            """
        )
    else:
        st.error("Por favor, insira valores positivos para todos os campos.")

