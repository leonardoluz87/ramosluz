#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Constantes
massa_proton = 1.6726e-27  # kg
energia_colisao_protons = 6.86e-10  # J

# Funções de cálculo
def calcular_tempo(distancia, velocidade):
    return distancia / velocidade

def calcular_aceleracao(velocidade, tempo):
    return velocidade / tempo

def calcular_energia_cinetica(massa, velocidade):
    return 0.5 * massa * velocidade**2

def energia_por_massa(energia, massa):
    return energia / massa

# Interface do programa
st.title("Cálculo de Física: Colisão de Esferas e Comparação com Prótons")
st.write("Insira os dados abaixo para calcular as propriedades físicas antes da colisão.")

# Entradas do usuário (agora com unidades em g, m/s, cm, psi)
velocidade_A = st.number_input("Velocidade da esfera A (em m/s):", min_value=0.0, step=0.1)
velocidade_B = st.number_input("Velocidade da esfera B (em m/s):", min_value=0.0, step=0.1)
distancia_A = st.number_input("Distância percorrida pela esfera A (em cm):", min_value=0.0, step=0.1)
distancia_B = st.number_input("Distância percorrida pela esfera B (em cm):", min_value=0.0, step=0.1)
massa_A = st.number_input("Massa da esfera A (em g):", min_value=0.0, step=0.01)
massa_B = st.number_input("Massa da esfera B (em g):", min_value=0.0, step=0.01)
pressao = st.number_input("Pressão do gás no cilindro (em psi):", min_value=0.0, step=1.0)

# Botão para calcular
if st.button("Calcular"):
    if all(v > 0 for v in [velocidade_A, velocidade_B, distancia_A, distancia_B, massa_A, massa_B, pressao]):
        # Conversões de unidades
        distancia_A = distancia_A / 100  # cm para m
        distancia_B = distancia_B / 100  # cm para m
        massa_A = massa_A / 1000  # g para kg
        massa_B = massa_B / 1000  # g para kg
        pressao = pressao * 6894.76  # psi para Pascal (1 psi = 6894.76 Pa)

        # Cálculos
        tempo_A = calcular_tempo(distancia_A, velocidade_A)
        tempo_B = calcular_tempo(distancia_B, velocidade_B)

        aceleracao_A = calcular_aceleracao(velocidade_A, tempo_A)
        aceleracao_B = calcular_aceleracao(velocidade_B, tempo_B)

        energia_cinetica_A = calcular_energia_cinetica(massa_A, velocidade_A)
        energia_cinetica_B = calcular_energia_cinetica(massa_B, velocidade_B)
        energia_cinetica_total = energia_cinetica_A + energia_cinetica_B

        # Comparação com colisão de prótons
        energia_proton_por_massa = energia_por_massa(energia_colisao_protons, massa_proton * 2)  # energia por massa de 2 prótons
        energia_esferas_A_por_massa = energia_por_massa(energia_cinetica_A, massa_A)
        energia_esferas_B_por_massa = energia_por_massa(energia_cinetica_B, massa_B)

        # Exibição dos resultados
        st.subheader("Resultados:")
        st.write(f"Tempo percorrido pela esfera A: {tempo_A:.3f} s")
        st.write(f"Tempo percorrido pela esfera B: {tempo_B:.3f} s")
        st.write(f"Aceleração da esfera A: {aceleracao_A:.3f} m/s²")
        st.write(f"Aceleração da esfera B: {aceleracao_B:.3f} m/s²")
        st.write(f"Energia Cinética da esfera A: {energia_cinetica_A:.3e} J")
        st.write(f"Energia Cinética da esfera B: {energia_cinetica_B:.3e} J")
        st.write(f"Energia Cinética Total antes da colisão: {energia_cinetica_total:.3e} J")

        st.subheader("Comparação de Energia por Massa:")

        # Comparação
        st.write("**Prótons:**")
        st.write(f"Massa total dos prótons: 3,34e-27 kg")
        st.write(f"Energia total dos prótons: {energia_colisao_protons:.3e} J")
        st.write(f"Energia por unidade de massa (prótons): {energia_proton_por_massa:.3e} J/kg")

        st.write("**Esferas:**")
        st.write(f"Energia por unidade de massa da esfera A: {energia_esferas_A_por_massa:.3e} J/kg")
        st.write(f"Energia por unidade de massa da esfera B: {energia_esferas_B_por_massa:.3e} J/kg")

        st.write(
            """
            **Conclusão**:
            A comparação de energia por unidade de massa mostra como diferentes sistemas (prótons e esferas) possuem uma grande disparidade em termos de energia disponível para a mesma quantidade de massa. 
            Enquanto a energia por unidade de massa é muito maior para os prótons, as esferas ainda possuem uma energia cinética significativa devido à sua velocidade, mesmo com uma massa maior.
            """
        )
    else:
        st.error("Por favor, insira valores positivos para todos os campos.")

