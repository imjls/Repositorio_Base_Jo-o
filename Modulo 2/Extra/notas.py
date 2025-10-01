import streamlit as st

st.title("📘 Sistema de Notas")


nota1 = st.number_input("Informe a primeira nota:", min_value=0.0, max_value=10.0, step=0.1)
nota2 = st.number_input("Informe a segunda nota:", min_value=0.0, max_value=10.0, step=0.1)
nota3 = st.number_input("Informe a terceira nota:", min_value=0.0, max_value=10.0, step=0.1)

if st.button("Calcular Média"):
    media = (nota1 + nota2 + nota3) / 3

    st.write(f"📊 Sua média foi: **{media:.2f}**")

    if media <= 4.9:
        st.error("❌ Reprovado")
    elif media <= 6.9:
        st.warning("⚠️ Recuperação")
    else:
        st.success("✅ Aprovado")
