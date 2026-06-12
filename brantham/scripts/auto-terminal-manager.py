#!/usr/bin/env python3
"""
Auto Terminal Manager - Gestion automatique des terminaux et processus
Surveille et redémarre automatiquement les sessions déconnectées
"""

import os
import sys
import subprocess
import time
import json
import signal
import psutil
from pathlib import Path
from datetime import datetime
import argparse

class AutoTerminalManager:
    def __init__(self, config_file=None):
        self.config_file = config_file or "terminal_config.json"
        self.sessions = {}
        self.processes = {}
        self.running = False

        # Configuration par défaut
        self.default_config = {
            "check_interval": 30,  # secondes
            "max_restarts": 5,
            "auto_reconnect": True,
            "notification": True,
            "log_file": "terminal_manager.log",
            "sessions": {
                "dev-server": {
                    "command": "npm run dev",
                    "directory": "/Users/paul/Desktop/brantham-partners",
                    "type": "npm",
                    "auto_restart": True,
                    "max_restarts": 3
                },
                "api-server": {
                    "command": "uvicorn main:app --reload",
                    "directory": "/Users/paul/internal-tool/api",
                    "type": "python",
                    "auto_restart": True,
                    "max_restarts": 5
                },
                "database": {
                    "command": "docker-compose up postgres",
                    "directory": "/Users/paul/internal-tool",
                    "type": "docker",
                    "auto_restart": True,
                    "max_restart": 2
                }
            }
        }

        self.load_config()

    def load_config(self):
        """Charge la configuration depuis le fichier"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = self.default_config
            self.save_config()

    def save_config(self):
        """Sauvegarde la configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def log(self, message, level="INFO"):
        """Log les messages avec timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {level}: {message}"

        print(log_message)

        if self.config.get("log_file"):
            with open(self.config.get("log_file"), 'a') as f:
                f.write(log_message + "\n")

    def start_session(self, session_name):
        """Démarre une session de terminal"""
        if session_name not in self.config["sessions"]:
            self.log(f"Session {session_name} non trouvée dans la configuration", "ERROR")
            return False

        session = self.config["sessions"][session_name]

        # Vérifier si la session tourne déjà
        if session_name in self.processes and self.processes[session_name].is_running():
            self.log(f"Session {session_name} déjà en cours", "WARNING")
            return True

        try:
            # Créer le processus
            env = os.environ.copy()
            env["SESSION_NAME"] = session_name

            # Détacher le processus pour qu'il continue de tourner
            process = subprocess.Popen(
                session["command"],
                shell=True,
                cwd=session["directory"],
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid  # Crée un nouveau groupe de processus
            )

            self.processes[session_name] = process
            self.sessions[session_name] = {
                "start_time": datetime.now(),
                "restart_count": 0,
                "status": "running"
            }

            self.log(f"Session {session_name} démarrée avec PID {process.pid}")
            return True

        except Exception as e:
            self.log(f"Erreur lors du démarrage de {session_name}: {str(e)}", "ERROR")
            return False

    def stop_session(self, session_name):
        """Arrête une session"""
        if session_name in self.processes:
            try:
                # Envoyer SIGTERM d'abord
                os.killpg(os.getpgid(self.processes[session_name].pid), signal.SIGTERM)
                time.sleep(2)

                # Si toujours vivant, envoyer SIGKILL
                if self.processes[session_name].is_running():
                    os.killpg(os.getpgid(self.processes[session_name].pid), signal.SIGKILL)

                self.processes[session_name].terminate()
                self.log(f"Session {session_name} arrêtée")

            except Exception as e:
                self.log(f"Erreur lors de l'arrêt de {session_name}: {str(e)}", "ERROR")

            del self.processes[session_name]
            if session_name in self.sessions:
                self.sessions[session_name]["status"] = "stopped"

    def check_session(self, session_name):
        """Vérifie l'état d'une session"""
        if session_name not in self.processes:
            return False

        process = self.processes[session_name]

        if not process.is_running():
            self.log(f"Session {session_name} arrêtée inattendue", "WARNING")

            session = self.config["sessions"][session_name]
            restart_count = self.sessions[session_name]["restart_count"]

            if restart_count < session.get("max_restarts", 5):
                if session.get("auto_restart", True):
                    self.log(f"Redémarrage automatique de {session_name} ({restart_count + 1}/{session.get('max_restarts', 5)})", "INFO")
                    self.start_session(session_name)
                    self.sessions[session_name]["restart_count"] = restart_count + 1
                    return True
                else:
                    self.log(f"Auto-redémarrage désactivé pour {session_name}", "WARNING")
            else:
                self.log(f"Nombre maximal de redémarrages atteint pour {session_name}", "ERROR")

            return False

        return True

    def check_all_sessions(self):
        """Vérifie toutes les sessions"""
        for session_name in self.config["sessions"]:
            if session_name in self.processes:
                self.check_session(session_name)
            else:
                session = self.config["sessions"][session_name]
                if session.get("auto_start", False):
                    self.log(f"Démarrage automatique de {session_name}", "INFO")
                    self.start_session(session_name)

    def start_monitoring(self):
        """Démarre le monitoring"""
        self.running = True
        self.log("Démarrage du monitoring des terminaux", "INFO")

        try:
            while self.running:
                self.check_all_sessions()
                time.sleep(self.config.get("check_interval", 30))

        except KeyboardInterrupt:
            self.log("Arrêt du monitoring demandé par l'utilisateur", "INFO")
        finally:
            self.stop_all()

    def stop_all(self):
        """Arrête toutes les sessions"""
        self.log("Arrêt de toutes les sessions", "INFO")
        for session_name in list(self.processes.keys()):
            self.stop_session(session_name)

    def add_session(self, name, command, directory, session_type="custom", auto_restart=True, max_restarts=3):
        """Ajoute une nouvelle session"""
        self.config["sessions"][name] = {
            "command": command,
            "directory": directory,
            "type": session_type,
            "auto_restart": auto_restart,
            "max_restarts": max_restarts
        }
        self.save_config()
        self.log(f"Nouvelle session {name} ajoutée", "INFO")

    def list_sessions(self):
        """Liste toutes les sessions et leur statut"""
        print("\n=== Sessions Actives ===")
        for name, session in self.config["sessions"].items():
            status = "running" if name in self.processes and self.processes[name].is_running() else "stopped"
            restart_count = self.sessions[name]["restart_count"] if name in self.sessions else 0

            print(f"{name}: {status} | Redémarrages: {restart_count} | Commande: {session['command']}")

    def get_stats(self):
        """Retourne des statistiques sur les sessions"""
        running_count = sum(1 for p in self.processes.values() if p.is_running())
        total_count = len(self.config["sessions"])

        return {
            "total": total_count,
            "running": running_count,
            "stopped": total_count - running_count,
            "uptime": datetime.now() - self.sessions.get("start_time", datetime.now())
        }

def main():
    parser = argparse.ArgumentParser(description="Auto Terminal Manager - Gestion automatique des terminaux")
    parser.add_argument("--start", action="store_true", help="Démarrer le monitoring")
    parser.add_argument("--stop", action="store_true", help="Arrêter toutes les sessions")
    parser.add_argument("--add", nargs=4, metavar=('NAME', 'COMMAND', 'DIRECTORY', 'TYPE'),
                       help="Ajouter une nouvelle session: nom commande type directory")
    parser.add_argument("--list", action="store_true", help="Lister les sessions")
    parser.add_argument("--stats", action="store_true", help="Afficher les statistiques")
    parser.add_argument("--config", default="terminal_config.json", help="Fichier de configuration")

    args = parser.parse_args()

    manager = AutoTerminalManager(args.config)

    if args.add:
        name, command, directory, session_type = args.add
        manager.add_session(name, command, directory, session_type)

    elif args.list:
        manager.list_sessions()

    elif args.stats:
        stats = manager.get_stats()
        print(f"\n=== Statistiques ===")
        print(f"Total sessions: {stats['total']}")
        print(f"Running: {stats['running']}")
        print(f"Stopped: {stats['stopped']}")

    elif args.start:
        manager.start_monitoring()

    elif args.stop:
        manager.stop_all()

    else:
        print("Auto Terminal Manager")
        print("Utilisez --help pour voir les options disponibles")
        manager.list_sessions()

if __name__ == "__main__":
    main()