import streamlit as st  # Import the library after installation

# Créer deux colonnes
col1, col2 = st.columns(2)

# Première colonne
with col1:
    option1 = st.selectbox(
        "Catégories",
        ("Email", "Home phone", "Mobile phone"),
        index=0,
        placeholder="Sélectionner la catégorie du livre..."
    )

# Deuxième colonne
with col2:
    option2 = st.selectbox(
        "TEST TEST",
        ("Email", "Home phone", "Mobile phone")
    )

# Afficher le résultat sélectionné dans les deux colonnes
st.write("You selected in column 1:", option1)
st.write("You selected in column 2:", option2)
