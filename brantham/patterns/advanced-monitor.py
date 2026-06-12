#!/usr/bin/env python3
import subprocess
import time
import json
import logging
import os
import sys
import signal
from datetime import datetime
from pathlib import Path

class TerminalMonitor:
    def __init__(self, config_file=None):
        # Configuration par défaut
        self.config_dir = Path.home() / ".config" / "terminal-monitor"
        self.config_file = config_file or (self.config_dir / "terminal-monitor.json")
        self.log_file = Path("/tmp") / "terminal-monitor.log"

        # Charger configuration
        self.config = self.load_config()
        self.setup_logging()

        # Gestion du signal pour arrêter proprement
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

        self.running = True

    def signal_handler(self, signum, frame):
        logging.info(f"Signal {signum} reçu - arrêt du monitor...")
        self.running = False

    def load_config(self):
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return self.get_default_config()
        except Exception as e:
            logging.error(f"Erreur chargement config: {e}")
            return self.get_default_config()

    def get_default_config(self):
        return {
            "interval": 30,
            "processes": [
                "npm run dev",
                "python manage.py runserver",
                "yarn dev",
                "go run main.go"
            ],
            "services": ["docker", "redis", "postgres", "nginx"],
            "auto_restart": True,
            "extensions": {
                "vscode": [],
                "check_interval": 300,
                "auto_update": True
            },
            "notifications": {
                "enabled": True,
                "desktop": True
            }
        }

    def setup_logging(self):
        # Créer le répertoire de logs si nécessaire
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file, encoding='utf-8'),
                logging.StreamHandler(sys.stdout)
            ]
        )

        # Afficher la configuration chargée
        logging.info(f"Configuration chargée depuis: {self.config_file}")
        logging.info(f"Intervalle de surveillance: {self.config['interval']}s")

    def run_command(self, command, capture_output=False):
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", "Command timeout"
        except Exception as e:
            return False, "", str(e)

    def is_process_running(self, process_name):
        cmd = f"pgrep -f '{process_name}'"
        success, stdout, stderr = self.run_command(cmd)
        return success and stdout.strip() != ""

    def restart_process(self, process_name):
        logging.info(f"Redémarrage du processus: {process_name}")

        # Sauvegarder le processus dans nohup pour qu'il continue si le monitor s'arrête
        cmd = f"nohup zsh -c '{process_name}' > /tmp/process-{self.sanitize_name(process_name)}.log 2>&1 &"
        success, stdout, stderr = self.run_command(cmd)

        if success:
            logging.info(f"Processus {process_name} redémarré avec succès")
            self.send_notification(f"Processus redémarré: {process_name}")
        else:
            logging.error(f"Échec redémarrage {process_name}: {stderr}")

    def sanitize_name(self, name):
        # Remplacer les caractères problématiques
        return name.replace(' ', '-').replace('/', '-').replace('\\', '-')

    def monitor_services(self):
        for service in self.config.get("services", []):
            # Vérifier si le service existe
            cmd = f"systemctl list-units --type=service | grep {service}"
            success, stdout, stderr = self.run_command(cmd)

            if success:
                # Vérifier le statut
                cmd = f"systemctl is-active {service}"
                success, _, stderr = self.run_command(cmd)

                if success:
                    logging.debug(f"Service OK: {service}")
                else:
                    logging.warning(f"Service arrêté: {service}")
                    if self.config.get("auto_restart", False):
                        logging.info(f"Redémarrage du service: {service}")
                        cmd = f"sudo systemctl restart {service}"
                        self.run_command(cmd)
            else:
                logging.debug(f"Service non trouvé ou non géré par systemd: {service}")

    def monitor_extensions(self):
        extensions_config = self.config.get("extensions", {})
        check_interval = extensions_config.get("check_interval", 300)

        # Vérifier si c'est le moment de vérifier les extensions
        current_time = datetime.now().timestamp()
        if not hasattr(self, 'last_extension_check'):
            self.last_extension_check = 0

        if current_time - self.last_extension_check < check_interval:
            return

        self.last_extension_check = current_time

        if extensions_config.get("auto_update", False):
            logging.info("Vérification des mises à jour d'extensions VSCode...")

            # Lister les extensions installées
            success, stdout, stderr = self.run_command("code --list-extensions --show-version")
            if success:
                # Sauvegarder la liste
                extensions_file = self.config_dir / "extensions-list.txt"
                with open(extensions_file, 'w', encoding='utf-8') as f:
                    f.write(stdout)

                logging.debug(f"Liste des extensions sauvegardée: {extensions_file}")

    def send_notification(self, message):
        if self.config.get("notifications", {}).get("enabled", False):
            # Notification desktop
            if self.config["notifications"].get("desktop", True):
                cmd = f'osascript -e \'display notification "{message}" with title "Terminal Monitor"\''
                self.run_command(cmd, capture_output=True)

            # Log
            logging.info(f"NOTIFICATION: {message}")

    def monitor_system_health(self):
        # Vérifier la mémoire disponible
        success, stdout, stderr = self.run_command("free -h | grep Mem | awk '{print $7}'")
        if success:
            available_mem = stdout.strip()
            logging.info(f"Mémoire disponible: {available_mem}")

            # Si moins de 1GB de mémoire disponible
            if "M" in available_mem and float(available_mem.replace("M", "")) < 1000:
                logging.warning("Mémoire disponible faible - considérer redémarrage")
                self.send_notification("Mémoire disponible faible")

        # Vérifier l'espace disque
        success, stdout, stderr = self.run_command("df -h | grep -E '/$|/home$' | awk '{print $5}'")
        if success:
            usage = stdout.strip().replace("%", "")
            if int(usage) > 90:
                logging.warning(f"Espace disque à {usage}% - considérer nettoyage")
                self.send_notification(f"Espace disque critique: {usage}%")

    def run(self):
        logging.info("=== DÉMARRAGE DU TERMINAL MONITOR ===")
        logging.info(f"Configuration: {self.config_file}")
        logging.info(f"Intervalle: {self.config['interval']}s")

        # Créer le répertoire de configuration
        self.config_dir.mkdir(parents=True, exist_ok=True)

        while self.running:
            try:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # 1. Monitoring processus
                for process in self.config.get("processes", []):
                    if not self.is_process_running(process):
                        logging.warning(f"Processus arrêté: {process}")
                        if self.config.get("auto_restart", True):
                            self.restart_process(process)

                # 2. Monitoring services système
                self.monitor_services()

                # 3. Monitoring extensions VSCode
                self.monitor_extensions()

                # 4. Santé système
                self.monitor_system_health()

                # Attente
                time.sleep(self.config.get("interval", 30))

            except KeyboardInterrupt:
                logging.info("Interruption clavier - arrêt du monitor...")
                break
            except Exception as e:
                logging.error(f"Erreur dans la boucle principale: {e}")
                time.sleep(5)  # Attendre avant de réessayer

        logging.info("=== ARRÊT DU TERMINAL MONITOR ===")

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Terminal Monitor - Surveillance automatique terminaux et extensions')
    parser.add_argument('--config', help='Chemin du fichier de configuration')
    parser.add_argument('--daemon', action='store_true', help='Lancer en arrière-plan')
    parser.add_argument('--install-service', action='store_true', help='Installer en service systemd')

    args = parser.parse_args()

    monitor = TerminalMonitor(args.config)

    if args.install_service:
        # Installer en service systemd
        service_content = f"""[Unit]
Description=Terminal Monitor Service
After=network.target

[Service]
Type=simple
User={os.getlogin()}
WorkingDirectory={os.getcwd()}
ExecStart={sys.executable} {sys.argv[0]}
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
"""
        service_file = Path("/tmp/terminal-monitor.service")
        with open(service_file, 'w') as f:
            f.write(service_content)

        print(f"Service créé: {service_file}")
        print("Pour l'installer: sudo cp /tmp/terminal-monitor.service /etc/systemd/system/")
        print("Puis: sudo systemctl daemon-reload && sudo systemctl enable terminal-monitor")
        return

    if args.daemon:
        # Lancer en arrière-plan
        import os
        pid = os.fork()
        if pid > 0:
            sys.exit(0)  # Parent process exits
        else:
            monitor.run()
    else:
        monitor.run()

if __name__ == "__main__":
    main()