import streamlit as st
import pandas as pd

def app():
    df = pd.read_parquet('tax.parquet')

    entity = st.text_input("Type in the entity: ", value = "Machine learning")

    try:
        df.loc[entity]
        st.markdown("Entity Found!")
    
    except KeyError:
        st.markdown("Sorry Entity Not Present :(")

app()
