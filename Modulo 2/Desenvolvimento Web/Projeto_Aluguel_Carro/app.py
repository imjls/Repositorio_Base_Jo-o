import streamlit as st
import pandas as pd
# python -m streamlit run app.py

# ------------------------------------------------------ Sidebar

st.sidebar.image("logo.png")
st.sidebar.title('João Motors')


carros = ['Omega', 'Astra', 'Vectra', 'Etios', 'Corolla']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)



# ---------------------------------------------------------- Principal
st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

if opcao == 'Omega':
    diaria = 416

elif opcao == 'Astra':
    diaria = 97

elif opcao == 'Vectra':
    diaria = 120

elif opcao == 'Etios':
    diaria = 149

elif opcao == 'Corolla':
    diaria = 299

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')