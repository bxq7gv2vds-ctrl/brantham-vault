#!/bin/bash
# Terminal Monitor Script - Surveillance automatique terminaux et extensions

LOG_FILE="/tmp/terminal-monitor.log"
CONFIG_DIR="$HOME/.config/terminal-monitor"
CONFIG_FILE="$CONFIG_DIR/terminal-monitor.json"

# Créer le répertoire de configuration si nécessaire
mkdir -p "$CONFIG_DIR"

# Charger la configuration
if [ -f "$CONFIG_FILE" ]; then
    INTERVAL=$(jq -r '.interval // 30' "$CONFIG_FILE")
else
    INTERVAL=30
fi

echo "Démarrage du terminal monitor - Intervalle: ${INTERVAL}s"
echo "Logs: $LOG_FILE"

# Boucle de surveillance
while true; do
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')

    # 1. Vérifier les terminaux VSCode actifs
    if ! pgrep -f "code.*--wait" > /dev/null; then
        echo "[$timestamp] VSCode non détecté - vérification terminaux..." >> "$LOG_FILE"

        # Vérifier si des processus de développement sont actifs
        dev_processes=$(pgrep -f "npm|yarn|python|go|rails")
        if [ -z "$dev_processes" ]; then
            echo "[$timestamp] Aucun processus de développement actif" >> "$LOG_FILE"
        fi
    fi

    # 2. Vérifier les processus de développement
    processes_to_check=("npm run dev" "python manage.py runserver" "yarn dev" "go run main.go")

    for process in "${processes_to_check[@]}"; do
        if ! pgrep -f "$process" > /dev/null; then
            echo "[$timestamp] Processus arrêté: $process" >> "$LOG_FILE"

            # Optionnel: redémarrer automatiquement
            if [ "$(jq -r '.auto_restart // true' "$CONFIG_FILE" 2>/dev/null)" = "true" ]; then
                echo "[$timestamp] Redémarrage du processus: $process" >> "$LOG_FILE"
                nohup zsh -c "$process" > /tmp/process-$(echo $process | tr ' ' '-').log 2>&1 &
            fi
        fi
    done

    # 3. Vérifier les services système
    services_to_check=("docker" "redis" "postgres" "nginx")
    for service in "${services_to_check[@]}"; do
        if systemctl is-active --quiet "$service"; then
            echo "[$timestamp] Service OK: $service" >> "$LOG_FILE"
        else
            echo "[$timestamp] Service arrêté: $service" >> "$LOG_FILE"
            if [ "$(jq -r '.auto_restart // true' "$CONFIG_FILE" 2>/dev/null)" = "true" ]; then
                echo "[$timestamp] Redémarrage du service: $service" >> "$LOG_FILE"
                sudo systemctl restart "$service" 2>/dev/null || true
            fi
        fi
    done

    # 4. Vérifier les mises à jour d'extensions VSCode (toutes les 5 vérifications)
    if [ $((timestamp % 150)) -eq 0 ]; then  # 5 * 30s = 150s
        echo "[$timestamp] Vérification mises à jour extensions VSCode..." >> "$LOG_FILE"
        code --list-extensions --show-version > "$CONFIG_DIR/extensions-list.txt" 2>/dev/null || true
    fi

    sleep $INTERVAL
done