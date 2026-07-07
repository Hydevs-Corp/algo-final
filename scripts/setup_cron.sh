#!/bin/bash

# Chemin du répertoire parent
PROJECT_DIR=$(dirname "$(realpath "$0")")/..

# Rendre le script Python exécutable
chmod +x "$PROJECT_DIR/src/retrain.py"

# Chemin absolu vers le script
SCRIPT_PATH=$(realpath "$PROJECT_DIR/src/retrain.py")
PYTHON_PATH=$(which python3)

# Ajouter la tâche cron pour s'exécuter tous les dimanches à minuit
CRON_JOB="0 0 * * 0 $PYTHON_PATH $SCRIPT_PATH >> /var/log/sentiment_retrain.log 2>&1"

(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
echo "Cronjob ajouté : $CRON_JOB"
