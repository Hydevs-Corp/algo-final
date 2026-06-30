import joblib
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from db import fetch_all_tweets
from sklearn.model_selection import train_test_split

def evaluate_model():
    records = fetch_all_tweets()
    if not records:
        print("Aucune donnée disponible pour l'évaluation.")
        return

    df = pd.DataFrame(records)
    
    # Construction des cibles (y) : 1 pour positif, -1 pour négatif
    def get_label(row):
        if row['positive'] == 1:
            return 1
        elif row['negative'] == 1:
            return -1
        else:
            return 0
            
    df['label'] = df.apply(get_label, axis=1)
    df = df[df['label'] != 0]

    if len(df) == 0:
        print("Aucune donnée labellisée disponible pour l'évaluation.")
        return

    # Pour avoir un jeu de validation, on split les données
    # (En pratique, on ferait ça lors de l'entraînement, mais ici on évalue le modèle globalement
    # ou on s'assure que le modèle s'en sort bien)
    X = df['text']
    y_true = df['label']

    try:
        model = joblib.load('sentiment_model.pkl')
    except Exception as e:
        print(f"Erreur de chargement du modèle : {e}")
        return

    y_pred = model.predict(X)

    print("Rapport de classification général :")
    print(classification_report(y_true, y_pred))

    # Matrice de confusion pour la classe Positive (1)
    # On binarise : Positif (1) vs Non-Positif (!= 1)
    y_true_pos = (y_true == 1).astype(int)
    y_pred_pos = (y_pred == 1).astype(int)
    cm_pos = confusion_matrix(y_true_pos, y_pred_pos)
    
    # Matrice de confusion pour la classe Négative (-1)
    # On binarise : Négatif (-1) vs Non-Négatif (!= -1)
    y_true_neg = (y_true == -1).astype(int)
    y_pred_neg = (y_pred == -1).astype(int)
    cm_neg = confusion_matrix(y_true_neg, y_pred_neg)

    # Sauvegarde des matrices de confusion en images
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm_pos, annot=True, fmt='d', cmap='Blues', xticklabels=['Non-Positif', 'Positif'], yticklabels=['Non-Positif', 'Positif'])
    plt.title('Matrice de Confusion - Prédictions Positives')
    plt.ylabel('Vrai')
    plt.xlabel('Prédit')
    plt.tight_layout()
    plt.savefig('confusion_matrix_positive.png')
    plt.close()

    plt.figure(figsize=(6, 4))
    sns.heatmap(cm_neg, annot=True, fmt='d', cmap='Reds', xticklabels=['Non-Négatif', 'Négatif'], yticklabels=['Non-Négatif', 'Négatif'])
    plt.title('Matrice de Confusion - Prédictions Négatives')
    plt.ylabel('Vrai')
    plt.xlabel('Prédit')
    plt.tight_layout()
    plt.savefig('confusion_matrix_negative.png')
    plt.close()

    print("Matrices de confusion générées et sauvegardées en tant qu'images png.")

if __name__ == '__main__':
    evaluate_model()
