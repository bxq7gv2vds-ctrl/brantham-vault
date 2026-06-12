---
name: terminal-monitor
description: Système de surveillance automatique terminaux et extensions VSCode
type: pattern
---

# Terminal & Extension Monitor

## Système de surveillance automatique terminaux et extensions VSCode

Ce pattern fournit un système de surveillance automatique pour:
- Extensions VSCode se déconnectant
- Terminaux qui se ferment
- Processus critiques arrêtés
- Reconnexion automatique

## Features

### 1. Terminal Health Check
```bash
# Script de surveillance terminaux
while true; do
    # Vérifier si le terminal est actif
    if [ -z "$(ps aux | grep '[t]erminal')" ]; then
        echo "Terminal fermé - redémarrage..."
        code .
    fi
    sleep 30
done
```

### 2. Extension Auto-Reconnect
```json
{
    "extensions.autoUpdate": true,
    "extensions.autoCheckUpdates": true,
    "extensions.showRecommendationsOnlyOnDemand": false
}
```

### 3. Process Monitor
```python
#!/usr/bin/env python3
import subprocess
import time
import logging

def monitor_processes():
    processes_to_watch = ['npm run dev', 'python manage.py runserver', 'yarn dev']
    
    while True:
        for process in processes_to_watch:
            try:
                result = subprocess.run(['pgrep', '-f', process], capture_output=True)
                if result.returncode != 0:
                    logging.warning(f"Processus {process} arrêté - redémarrage...")
                    subprocess.Popen(['zsh', '-c', process])
            except Exception as e:
                logging.error(f"Erreur monitoring: {e}")
        
        time.sleep(60)

if __name__ == "__main__":
    monitor_processes()
```

## Configuration VSCode

### Settings.json
```json
{
    "terminal.integrated.shell.osx": "/bin/zsh",
    "terminal.integrated.autoReveal": true,
    "terminal.integrated.copyOnSelection": true,
    "extensions.autoUpdate": true,
    "workbench.startupEditor": "terminal",
    
    // Configuration de la surveillance
    "terminal-monitor.enabled": true,
    "terminal-monitor.interval": 30,
    "terminal-monitor.processes": [
        "npm run dev",
        "python manage.py runserver",
        "yarn dev",
        "go run main.go"
    ]
}
```

### Installation extension vscode-terminal-auto-restart
```
# Code CLI
code --install-extension shd101wyy.markdown-preview-enhanced
code --install-extension ms-vscode.vscode-json
```

## Scripts de surveillance

### Script de base - monitor.sh
```bash
#!/bin/bash
# Monitor script pour terminaux et processus

LOG_FILE="/tmp/terminal-monitor.log"
INTERVAL=30

while true; do
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # Vérifier les terminaux actifs
    if [ -z "$(ps aux | grep '[t]erminal')" ]; then
        echo "[$timestamp] Terminal fermé, redémarrage..." >> $LOG_FILE
        code .
    fi
    
    # Vérifier processus Node
    if ! pgrep -f "npm run dev" > /dev/null; then
        echo "[$timestamp] Serveur Node.js arrêté" >> $LOG_FILE
    fi
    
    # Vérifier processus Python
    if ! pgrep -f "python manage.py" > /dev/null; then
        echo "[$timestamp] Serveur Django arrêté" >> $LOG_FILE
    fi
    
    sleep $INTERVAL
done
```

### Script avancé - advanced-monitor.py
```python
#!/usr/bin/env python3
import subprocess
import time
import json
import logging
from datetime import datetime

class TerminalMonitor:
    def __init__(self, config_file="terminal-monitor.json"):
        self.config = self.load_config(config_file)
        self.setup_logging()
        
    def load_config(self, config_file):
        try:
            with open(config_file) as f:
                return json.load(f)
        except FileNotFoundError:
            return self.get_default_config()
    
    def get_default_config(self):
        return {
            "interval": 30,
            "processes": [
                "npm run dev",
                "python manage.py runserver",
                "yarn dev"
            ],
            "services": ["redis", "postgres", "nginx"],
            "auto_restart": True
        }
    
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('/tmp/terminal-monitor.log'),
                logging.StreamHandler()
            ]
        )
    
    def is_process_running(self, process_name):
        try:
            result = subprocess.run(['pgrep', '-f', process_name], capture_output=True)
            return result.returncode == 0
        except:
            return False
    
    def restart_process(self, process_name):
        try:
            subprocess.Popen(['zsh', '-c', process_name])
            logging.info(f"Redémarrage du processus: {process_name}")
        except Exception as e:
            logging.error(f"Échec redémarrage {process_name}: {e}")
    
    def monitor_services(self):
        for service in self.config.get("services", []):
            try:
                result = subprocess.run(['systemctl', 'is-active', service], capture_output=True)
                if result.returncode != 0:
                    logging.warning(f"Service {service} arrêté")
                    if self.config.get("auto_restart", False):
                        subprocess.run(['systemctl', 'restart', service])
            except:
                pass
    
    def run(self):
        logging.info("Démarrage du monitor terminal")
        
        while True:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Monitoring processus
            for process in self.config.get("processes", []):
                if not self.is_process_running(process):
                    logging.warning(f"Processus arrêté: {process}")
                    if self.config.get("auto_restart", True):
                        self.restart_process(process)
            
            # Monitoring services système
            self.monitor_services()
            
            # Attente avant prochaine vérification
            time.sleep(self.config.get("interval", 30))

if __name__ == "__main__":
    monitor = TerminalMonitor()
    monitor.run()
```

## Installation et utilisation

### 1. Créer le fichier de configuration
```bash
mkdir -p ~/.config/terminal-monitor
cat > ~/.config/terminal-monitor/terminal-monitor.json << 'EOF'
{
    "interval": 30,
    "processes": [
        "npm run dev",
        "python manage.py runserver",
        "yarn dev",
        "go run main.go"
    ],
    "services": ["redis", "postgres", "nginx"],
    "auto_restart": true
}
EOF
```

### 2. Lancer le monitor
```bash
# Option 1: Lancer en arrière-plan
python advanced-monitor.py &

# Option 2: Avec systemd (pour démarrage automatique)
sudo systemctl --user enable terminal-monitor
sudo systemctl --user start terminal-monitor
```

### 3. Configuration VSCode
Ajouter à `.vscode/settings.json`:
```json
{
    "tasks": {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "Start Terminal Monitor",
                "type": "shell",
                "command": "python ~/.config/terminal-monitor/advanced-monitor.py",
                "isBackground": true,
                "problemMatcher": []
            }
        ]
    }
}
```

## Best Practices

1. **Logging**: Garder un log des événements
2. **Alertes**: Configurer des alertes pour les pannes critiques
3. **Redondance**: Avoir un script de backup
4. **Tests**: Vérifier régulièrement que le monitor fonctionne
5. **Documentation**: Documenter la configuration

## Monitoring en temps réel

### Créer un dashboard simple
```bash
# Dashboard de monitoring
echo "=== Terminal Monitor Status ==="
echo "Heure: $(date)"
echo "Processus actifs:"
ps aux | grep -E "(npm|python|yarn|go)" | grep -v grep
echo ""
echo "Services système:"
systemctl is-active redis postgres nginx
echo ""
echo "Logs récents:"
tail -n 20 /tmp/terminal-monitor.log
```

Ce système assure que vos terminaux et processus critiques restent actifs en cas de déconnexion ou crash, réduisant le temps d'arrêt et améliorant la productivité.

## Related
- [[dashboard-kpis-m-a]]
- [[workflow-deal-flow]]
- [[analyse-concurrentielle-m-a]]
- [[_system/MOC-patterns]]