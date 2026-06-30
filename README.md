# API d'Analyse de Sentiments (SocialMetrics AI)

Cette API permet d'évaluer le sentiment (positif ou négatif) d'une liste de tweets en utilisant un modèle de Machine Learning (Régression Logistique).

## Prérequis
- Docker et Docker Compose
- Python 3.8+
- Git

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone <url-du-repo>
   cd <dossier-du-repo>
   ```

2. **Démarrer la base de données MySQL via Docker** :
   ```bash
   docker-compose up -d
   ```
   *Note : Cela va initialiser la base de données `sentiment_db` et la table `tweets` avec quelques données initiales grâce au fichier `init.sql`.*

3. **Installer les dépendances Python** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Entraîner le modèle initialement** :
   Assurez-vous que la base de données est lancée, puis exécutez le script d'entraînement pour générer `sentiment_model.pkl`.
   ```bash
   python train_model.py
   ```

5. **Lancer l'API Flask** :
   ```bash
   python app.py
   ```
   L'API sera disponible sur `http://localhost:5000`.

## Utilisation de l'API

L'API expose un endpoint `POST /analyze`.

**Requête :**
Vous devez envoyer un tableau de chaînes de caractères au format JSON.

```bash
curl -X POST http://localhost:5000/analyze \
     -H "Content-Type: application/json" \
     -d '["Ce produit est génial !", "Je déteste cette application."]'
```

**Réponse :**
Retourne un JSON avec les scores de sentiment (entre -1 et 1). Un score proche de 1 indique un sentiment très positif, et un score proche de -1 indique un sentiment très négatif.

```json
{
  "tweet1": 0.8543,
  "tweet2": -0.7210
}
```

## Réentraînement du modèle

Le modèle peut être réentraîné avec les nouvelles données ajoutées à la base de données. 

### Sur Linux / macOS :
Un script `setup_cron.sh` est fourni. Il configure un cronjob pour exécuter `retrain.py` tous les dimanches à minuit.
```bash
./setup_cron.sh
```

### Sur Windows :
Un script `setup_task.bat` est fourni. Exécutez-le en tant qu'administrateur pour créer une tâche planifiée Windows.
```cmd
setup_task.bat
```

## Évaluation du modèle
Le script `evaluate_model.py` permet de générer les matrices de confusion (sous forme d'images PNG) et d'afficher le rapport de classification. Un rapport détaillé est disponible dans le fichier `rapport_evaluation.md` (qui peut être exporté en PDF).
```bash
python evaluate_model.py
```
