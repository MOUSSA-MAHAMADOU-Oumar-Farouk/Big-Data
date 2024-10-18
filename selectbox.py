import streamlit as st
import pandas as pd
import random
import altair as alt

# Define categories, ratings, stock status, editions, and tax rates
categories = ['Fiction', 'Science', 'Nature', 'History', 'Technology', 'Art']
titles = ['The Stars', 'Science and You', 'Nature\'s Beauty', 'History Unfolds', 'Tech Revolution', 'Art of Life']
ratings = ['3 étoiles', '4 étoiles', '5 étoiles']
stock_status = ['En stock', 'Indisponible']
editions = ['Edition 1', 'Edition 2', 'Edition 3', 'Edition Deluxe']
tax_rate = 0.2

# Generate the fictive dataset
data = []

for i in range(300):
    category = random.choice(categories)
    title = random.choice(titles)
    rating = random.choice(ratings)
    stock = random.choice(stock_status)
    quantity = random.randint(0, 50) if stock == 'En stock' else 0
    price_ht = round(random.uniform(5, 50), 2)
    price_ttc = round(price_ht * (1 + tax_rate), 2)
    edition = random.choice(editions)
    
    data.append([category, title, rating, stock, quantity, price_ht, price_ttc, edition])

# Create a DataFrame
df_books = pd.DataFrame(data, columns=['categorie_livre', 'titre_livre', 'notation_clients', 'disponibilité', 
                                       'nombre_de_livre_disponible', 'prix_hors_taxe', 'prix_avec_taxe', 'edition'])

# Extraire les catégories uniques
categories = df_books['categorie_livre'].unique()

# Créer deux colonnes
col1, col2 = st.columns(2)

# Première colonne avec le selectbox pour les catégories de livres
with col1:
    categorie_selectionnee = st.selectbox(
        "Catégories des livres",
        categories,
        placeholder="Sélectionner la catégorie du livre..."
    )

# Deuxième colonne
with col2:
    option2 = st.selectbox(
        "TEST TEST",
        ("Email", "Home phone", "Mobile phone")
    )
    # Définition des couleurs selon la catégorie
scale = alt.Scale(
    domain=categories,  # Utiliser les catégories réelles
    range=["#e7ba52", "#a7a7a7", "#aec7e8", "#a7a7a7", "#aec7e8", "#e7ba52"]
)
color = alt.Color("categorie_livre:N", scale=scale)

# Sélection par clic multiple
click = alt.selection_multi(encodings=["color"])

# Création du diagramme à barres
bars = (
    alt.Chart(df_books)  # Utiliser df_books comme source de données
    .mark_bar()
    .encode(
        x="count()",
        y="categorie_livre:N",  # Utiliser la colonne 'categorie_livre' de votre DataFrame
        color=alt.condition(click, color, alt.value("lightgray")),
    )
    .properties(
        width=550,
    )
    .add_selection(click)
)

# Afficher le graphique dans Streamlit
st.altair_chart(bars, use_container_width=True)

# Afficher le résultat sélectionné dans les deux colonnes
st.write("You selected in column 1:", categorie_selectionnee)


