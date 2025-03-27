import numpy as np
import pandas as pd
from scipy.stats import pearsonr,spearmanr
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from pandas import read_csv
from pandas.plotting import scatter_matrix
   


try:
    fichier="BeansDataSet.csv"
    col=['Channel','Region','Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']
    article=[f'article_{i}' for i in range(1,439)]  
    data=read_csv(fichier,names=col)
    data.index=article
    pd.set_option('display.width',100)
    pd.set_option('display.float_format','{:.2f}'.format)
except:
    st.markdown("<h1 style='text-align: center;'>Beans&Pods</h1>", unsafe_allow_html=True)


st.sidebar.title("Analyse de données BeansDataSet")
menu=st.sidebar.selectbox("Navigation",["Peek at the date","Statisques descriptives","Compte rendu"])

if menu=="Peek at the date":
    st.subheader("Description des données :")
    st.write(data)
    st.subheader("Affichage des 5 premiers :")
    peek=data.head(5)    
    st.write(peek)
    st.subheader("Affichage des 5 derniers :")
    peek=data.tail(5)
    st.write(peek)
    st.subheader("Dimension des données :")
    st.write(data.shape)
    st.write(data.shape[0])
    st.write(data.shape[0])
    st.subheader("Absence des valeurs :")
    x = data.isnull()
    st.write(x)
    st.subheader("Total des valeurs manquantes :")
    Total_val_manquante = data.isnull().sum()
    st.write(Total_val_manquante)
    st.subheader("Nombre de vente Online et Store :")
    Channel_count=data.groupby('Channel').size()
    st.write(Channel_count)
    st.subheader("Nombre de vente au Centre/North/South :")
    Channel_count1=data.groupby('Region').size()
    st.write(Channel_count1)


elif menu=="Statisques descriptives":
    st.header("Statisques descriptives")
    st.subheader("Description des données :")
    descr=data.describe().round(2)
    st.dataframe(descr, width=1000)
 
    st.subheader("Etude de correlation :")
    correlation=data.select_dtypes(include='number').corr().round(2)
    st.dataframe(correlation, width=1000)
  
    st.subheader("Carte de chaleur :")
    fig,ax=plt.subplots(figsize=(10,10))
    sns.heatmap(correlation,annot=True,cmap='coolwarm',fmt='.2f')
    plt.suptitle("Carte de chaleur", fontsize=16)
    st.pyplot(fig)
    
    st.subheader("Boite a moustache :")
    fig,ax=plt.subplots(figsize=(10,10))
    sns.boxplot(data=data,ax=ax)
    plt.suptitle("Boite a moustache", fontsize=16)
    st.pyplot(fig)
 
    st.subheader("Histogramme :")
    fig, ax = plt.subplots(2, 3, figsize=(10, 10))
    data.hist(bins=15, ax=ax, rwidth=0.8, color='skyblue', edgecolor='black')
    plt.suptitle("Histogramme", fontsize=16)
    st.pyplot(fig)

    st.subheader("Matrice de dispersion :")
    fig, ax = plt.subplots(figsize=(15, 10))
    scatter_matrix(data, ax=ax, color='g')
    plt.suptitle("Matrice de dispersion", fontsize=22)
    st.pyplot(fig)
  
    st.subheader("Matrice de dispersion par la variable channel :")
    fig = sns.pairplot(data, hue='Channel')
    fig.fig.suptitle("Matrice de dispersion", fontsize=26)
    fig.fig.tight_layout()
    fig.fig.subplots_adjust(top=0.95)
    st.pyplot(fig)
  
    st.subheader("Histogramme en cercle des sommes des corrélations :")
    data=read_csv(fichier,names=col)
    corr=data.select_dtypes(include='number').corr()
    sums = corr.sum()
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))
    colors = plt.cm.tab20c.colors
    wedges, texts, autotexts = ax.pie(sums, labels=sums.index,
    autopct='%1.1f%%', startangle=90, colors=colors)
    fig.suptitle("Histogramme en cercle", fontsize=16)
    st.pyplot(fig)


elif menu=="Compte rendu":    
   
    st.markdown("<h1 style='text-align: center;'>Compte rendu</h1>", unsafe_allow_html=True)


    st.markdown("""
    ### 1. Analyse de données
    ### Distribution Channel et Région
    - **Channel de vente** : 142 ventes proviennent de la plateforme Online, tandis que 298 proviennent de Store. Cela montre une préférence pour les ventes en magasin.
    - **Région** : La majorité des ventes proviennent de la région South (316), suivie de North (77) et Central (47). Cela pourrait indiquer une présence ou une popularité plus forte dans le Sud.

    ### Statistiques par Produit
    Voici les statistiques par type de café pour mieux comprendre leur popularité :
    - Les ventes moyennes et les écarts types pour chaque type de café.
    - Espresso et Robusta semblent être les produits les plus vendus, tandis que Latte et Cappuccino ont des ventes plus faibles.

    ### 2. Recherche de Modèles et Tendances
    #### Analyse par Channel
    En comparant les ventes moyennes de chaque produit pour les canaux Online et Store, nous pourrions observer des tendances telles que :
    - Espresso et Robusta sont populaires en magasin, probablement en raison de la préférence pour les produits prêts à emporter.
    - Lungo est davantage vendu en ligne, ce qui peut suggérer une préférence pour les produits plus spécifiques ou de niche dans ce canal.

    #### Corrélations Entre les Produits
    En examinant la matrice de corrélation, nous observons des corrélations notables entre certains types de café :
    - Espresso et Latte montrent une corrélation positive. Cela pourrait signifier que les clients qui achètent l'un sont également intéressés par l'autre, ce qui peut être exploité pour des offres combinées.

    ### 3. Recommandations pour la Nouvelle Campagne de Marketing
    1. **Campagnes de Vente Croisée** : Proposer des offres groupées avec Espresso et Latte, car ces produits montrent une forte corrélation de vente.
    2. **Promotions Ciblées par Canal** :
        - **Online** : Mettre en avant les produits comme le Lungo, qui semble être plus populaire en ligne. Offrir des promotions spécifiques pour attirer encore plus de clients en ligne.
        - **Store** : Promouvoir des produits comme Robusta et Espresso, qui sont déjà populaires, mais en augmentant la fréquence d'achat avec des programmes de fidélité.
    3. **Focus Régional** : Puisque la majorité des ventes proviennent de la région South, concentrer la campagne marketing et les promotions dans cette région. Des campagnes spécifiques peuvent être développées pour North et Central pour essayer d'augmenter la présence dans ces régions.

    ### 4. Suggestions de Données Supplémentaires à Collecter
    Pour affiner l'analyse et mieux cibler les clients, Beans & Pods devrait envisager de collecter les données suivantes à l'avenir :
    - **Données démographiques des clients** : Informations telles que l'âge, le sexe, et les niveaux de revenus pour cibler les offres.
    - **Fréquence d'achat et historique des clients** : Avoir un aperçu des comportements d'achat permettrait de proposer des campagnes de fidélisation.
    - **Périodes de vente (saisonnalité)** : Collecter des données temporelles pourrait aider à identifier des pics de vente saisonniers et à planifier les promotions en conséquence.
    - **Retour clients et avis** : Savoir pourquoi les clients achètent certains produits pourrait éclairer les décisions d'inventaire et les campagnes marketing.
    """, unsafe_allow_html=True)

