#!/bin/bash
"""
Tmux Session Manager - Gestion automatique des sessions tmux
Redémarre automatiquement les sessions déconnectées et sauvegarde l'état
"""

# Configuration
SESSIONS_DIR="$HOME/.tmux-sessions"
BACKUP_DIR="$SESSIONS_DIR/backups"
LOG_FILE="$SESSIONS_DIR/session-manager.log"

# Créer les répertoires nécessaires
mkdir -p "$BACKUP_DIR"
mkdir -p "$(dirname "$LOG_FILE")"

# Fonction de logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Fonction pour vérifier si une session tmux existe
session_exists() {
    tmux has-session -t "$1" 2>/dev/null
}

# Fonction pour sauvegarder l'état d'une session
backup_session() {
    local session_name="$1"
    local backup_file="$BACKUP_DIR/${session_name}_$(date +%Y%m%d_%H%M%S).state"

    if session_exists "$session_name"; then
        # Lister les fenêtres et panes
        tmux list-windows -t "$session_name" -F "#{window_index}:#{window_name}" > "$backup_file"
        tmux list-panes -t "$session_name" -F "#{pane_current_path}" >> "$backup_file"

        log "Sauvegarde de la session $session_name dans $backup_file"
    fi
}

# Fonction pour restaurer une session
restore_session() {
    local session_name="$1"
    local backup_file="$BACKUP_DIR/${session_name}_latest.state"

    if [ -f "$backup_file" ]; then
        log "Restauration de la session $session_name depuis $backup_file"

        # Restaurer les fenêtres et commandes
        while IFS=: read -r window_index window_name; do
            if [[ -n "$window_index" && -n "$window_name" ]]; then
                tmux new-window -t "$session_name" -n "$window_name" -d
                tmux send-keys -t "$session_name:$window_index" "cd $window_name" Enter
            fi
        done < <(grep -E "^[0-9]+:" "$backup_file")

        # Restaurer les chemins des panes
        while read -r pane_path; do
            if [[ -n "$pane_path" && -d "$pane_path" ]]; then
                tmux send-keys -t "$session_name:0.0" "cd $pane_path" Enter
            fi
        done < <(grep -vE "^[0-9]+:" "$backup_file")

        return 0
    fi
    return 1
}

# Fonction pour créer une session avec configuration
create_session() {
    local session_name="$1"
    local session_config="$2"

    if ! session_exists "$session_name"; then
        log "Création de la session tmux: $session_name"

        # Créer la session
        tmux new-session -d -s "$session_name" -c "${session_config:-$HOME}"

        # Appliquer la configuration
        if [ -f "$SESSIONS_DIR/${session_name}.config" ]; then
            source "$SESSIONS_DIR/${session_name}.config"
        fi

        # Sauvegarder l'état initial
        backup_session "$session_name"

        return 0
    else
        log "La session $session_name existe déjà"
        return 1
    fi
}

# Fonction pour redémarrer une session
restart_session() {
    local session_name="$1"
    local max_attempts=3
    local attempt=1

    log "Redémarrage de la session $session_name"

    while [ $attempt -le $max_attempts ]; do
        # Sauvegarder l'état actuel
        backup_session "$session_name"

        # Tuer la session existante
        if session_exists "$session_name"; then
            tmux kill-session -t "$session_name"
            sleep 2
        fi

        # Essayer de restaurer
        if restore_session "$session_name"; then
            log "Session $session_name redémarrée avec succès"
            return 0
        fi

        # Essayer de créer une nouvelle session
        if [ -f "$SESSIONS_DIR/${session_name}.config" ]; then
            source "$SESSIONS_DIR/${session_name}.config"
            create_session "$session_name" "$SESSION_DIR"
        else
            create_session "$session_name"
        fi

        attempt=$((attempt + 1))
        sleep 1
    done

    log "Échec du redémarrage de la session $session_name après $max_attempts tentatives"
    return 1
}

# Fonction pour surveiller toutes les sessions
monitor_sessions() {
    log "Démarrage du monitoring des sessions tmux"

    while true; do
        # Lister toutes les sessions tmux
        for session_name in $(tmux list-sessions -F "#{session_name}" 2>/dev/null); do
            # Vérifier si la session est active
            if ! tmux has-session -t "$session_name" -v 2>/dev/null; then
                log "Session $session_name déconnectée, redémarrage..."
                restart_session "$session_name"
            fi
        done

        sleep 30  # Vérifier toutes les 30 secondes
    done
}

# Fonction pour créer des sessions prédéfinies
create_default_sessions() {
    # Configuration pour le développement web
    cat > "$SESSIONS_DIR/web-dev.config" << 'EOF'
# Session de développement web
tmux new-window -n "frontend" -c "/Users/paul/Desktop/brantham-partners"
tmux send-keys -t "web-dev:frontend" "npm install" Enter
tmux send-keys -t "web-dev:frontend" "npm run dev" Enter

tmux new-window -n "backend" -c "/Users/paul/internal-tool/api"
tmux send-keys -t "web-dev:backend" "uvicorn main:app --reload --host 0.0.0.0 --port 8000" Enter

tmux new-window -n "database" -c "/Users/paul/internal-tool"
tmux send-keys -t "web-dev:database" "docker-compose up -d" Enter

tmux select-window -t "web-dev:frontend"
EOF

    # Configuration pour le data science
    cat > "$SESSIONS_DIR/data-science.config" << 'EOF'
# Session data science
tmux new-window -n "jupyter" -c "/Users/paul/data/projects"
tmux send-keys -t "data-science:jupyter" "jupyter lab --no-browser --port=8888" Enter

tmux new-window -n "ml-training" -c "/Users/paul/data/ml"
tmux send-keys -t "data-science:ml-training" "python train_model.py" Enter

tmux select-window -t "data-science:jupyter"
EOF

    log "Sessions par défaut créées"
}

# Interface utilisateur principale
case "$1" in
    start)
        monitor_sessions
        ;;

    create)
        create_session "$2" "$3"
        ;;

    restart)
        restart_session "$2"
        ;;

    stop)
        if [ -n "$2" ]; then
            tmux kill-session -t "$2"
            log "Session $2 arrêtée"
        else
            tmux kill-server
            log "Toutes les sessions tmux arrêtées"
        fi
        ;;

    list)
        echo "=== Sessions tmux actives ==="
        tmux list-sessions -F "#{session_name}: #{session_windows} windows (created #{session_created})"
        ;;

    backup)
        backup_session "$2"
        ;;

    restore)
        restore_session "$2"
        ;;

    init)
        create_default_sessions
        ;;

    *)
        echo "Usage: $0 {start|create|restart|stop|list|backup|restore|init} [session_name] [directory]"
        echo ""
        echo "  start          - Démarrer le monitoring permanent"
        echo "  create <name>  - Créer une nouvelle session"
        echo "  restart <name> - Redémarrer une session"
        echo "  stop [name]    - Arrêter une session ou toutes"
        echo "  list           - Lister les sessions actives"
        echo "  backup <name>  - Sauvegarder l'état d'une session"
        echo "  restore <name> - Restaurer une session depuis la sauvegarde"
        echo "  init           - Créer les sessions par défaut"
        exit 1
        ;;
esac