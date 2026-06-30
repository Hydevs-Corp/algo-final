#!/bin/bash

# Rendre le script Python exécutable
chmod +x retrain.py

# Chemin absolu vers le script
SCRIPT_PATH=$(realpath retrain.py)
PYTHON_PATH=$(which python3)

# Ajouter la tâche cron pour s'exécuter tous les dimanches à minuit
CRON_JOB="0 0 * * 0 $PYTHON_PATH $SCRIPT_PATH >> /var/log/sentiment_retrain.log 2>&1"

(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
echo "Cronjob ajouté : $CRON_JOB"
