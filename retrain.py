import datetime
from train_model import train_and_save_model

def retrain_model():
    print(f"[{datetime.datetime.now()}] Début du réentraînement hebdomadaire du modèle...")
    try:
        train_and_save_model()
        print(f"[{datetime.datetime.now()}] Réentraînement terminé avec succès.")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] Erreur lors du réentraînement : {e}")

if __name__ == '__main__':
    retrain_model()
