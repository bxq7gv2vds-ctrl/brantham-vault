#!/bin/bash
# Dashboard de monitoring en temps réel

LOG_FILE="/tmp/terminal-monitor.log"
CONFIG_DIR="$HOME/.config/terminal-monitor"

echo "=== TERMINAL MONITOR DASHBOARD ==="
echo "Heure: $(date)"
echo ""

# Statut des processus
echo "📊 STATUT PROCESSUS:"
echo "-------------------"
processes=("npm run dev" "python manage.py runserver" "yarn dev" "go run main.go" "docker-compose up")
for process in "${processes[@]}"; do
    if pgrep -f "$process" > /dev/null; then
        echo "✅ $process"
    else
        echo "❌ $process"
    fi
done

echo ""
echo "🔧 STATUT SERVICES:"
echo "-------------------"
services=("docker" "redis" "postgres" "nginx")
for service in "${services[@]}"; do
    if systemctl is-active --quiet "$service"; then
        echo "✅ $service (actif)"
    else
        echo "❌ $service (arrêté)"
    fi
done

echo ""
echo "💾 RÉSSOURCES SYSTÈME:"
echo "---------------------"
echo "Mémoire: $(free -h | grep Mem | awk '{print $3 "/" $2 " (" $7 " disponible)"}')"
echo "CPU: $(top -l 1 | grep "CPU usage" | awk '{print $3}' | sed 's/%//')% usage"
echo "Disque: $(df -h | grep -E '/$|/home$' | awk '{print $5 " utilisé sur " $6}')"

echo ""
echo "📋 EXTENSIONS VSCode:"
echo "-------------------"
if [ -f "$CONFIG_DIR/extensions-list.txt" ]; then
    echo "Extensions installées: $(wc -l < "$CONFIG_DIR/extensions-list.txt")"
    echo "Dernière vérification: $(stat -f "%Sm" "$CONFIG_DIR/extensions-list.txt")"
else
    echo "Liste des extensions non disponible"
fi

echo ""
echo "📝 LOGS RÉCENTS:"
echo "---------------"
if [ -f "$LOG_FILE" ]; then
    echo "Derniers 10 événements:"
    tail -n 10 "$LOG_FILE"
else
    echo "Aucun log trouvé"
fi

echo ""
echo "🚀 ACTIONS:"
echo "-----------"
echo "1. Lancer le monitor: python3 advanced-monitor.py"
echo "2. Voir les processus: ps aux | grep -E '(npm|python|yarn|go)' | grep -v grep"
echo "3. Redémarrer un service: sudo systemctl restart [service]"
echo "4. Logs détaillés: tail -f $LOG_FILE"