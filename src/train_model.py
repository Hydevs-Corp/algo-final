# pyrefly: ignore [missing-import]
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from db import fetch_all_tweets

def train_and_save_model():
    records = fetch_all_tweets()
    if not records:
        print("Aucune donnée disponible pour l'entraînement.")
        return

    df = pd.DataFrame(records)
    
    # Construction de la cible (y) : 1 pour positif, -1 pour négatif
    # On suppose que si positive=1, alors c'est 1, si negative=1, alors c'est -1.
    def get_label(row):
        if row['positive'] == 1:
            return 1
        elif row['negative'] == 1:
            return -1
        else:
            return 0 # Neutre par défaut
            
    df['label'] = df.apply(get_label, axis=1)
    
    # On filtre les tweets neutres s'il y en a pour cet exercice binaire
    df = df[df['label'] != 0]

    if len(df) == 0:
        print("Aucune donnée labellisée disponible pour l'entraînement.")
        return

    X = df['text']
    y = df['label']

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # Création d'un pipeline: Vectorisation + Régression Logistique
    model = make_pipeline(
        TfidfVectorizer(max_features=1000),
        LogisticRegression()
    )

    model.fit(X_train, y_train)

    import os
    model_path = os.path.join(os.path.dirname(__file__), 'sentiment_model.pkl')
    # Sauvegarde du modèle entraîné
    joblib.dump(model, model_path)
    print("Modèle entraîné et sauvegardé avec succès dans 'sentiment_model.pkl'.")

if __name__ == '__main__':
    train_and_save_model()
