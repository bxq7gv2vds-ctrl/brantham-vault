#!/usr/bin/env python3
"""
Process Watcher - Surveillance et redémarrage automatique des processus
Surveille les processus critiques et les redémarre s'ils s'arrêtent
"""

import os
import sys
import time
import json
import signal
import psutil
import subprocess
from pathlib import Path
from datetime import datetime
import argparse
import logging
from typing import Dict, List, Optional

class ProcessWatcher:
    def __init__(self, config_file="process_watcher.json"):
        self.config_file = config_file
        self.processes: Dict[str, psutil.Process] = {}
        self.config = self.load_config()
        self.setup_logging()
        self.start_time = datetime.now()

    def setup_logging(self):
        """Configure le logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('process_watcher.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def load_config(self) -> dict:
        """Charge la configuration depuis le fichier JSON"""
        default_config = {
            "check_interval": 10,
            "max_restarts": 3,
            "auto_restart": True,
            "notifications": True,
            "processes": {
                "nginx": {
                    "command": "nginx",
                    "args": ["-g", "daemon off;"],
                    "working_dir": "/usr/sbin",
                    "expected_exit_code": 0,
                    "restart_delay": 5
                },
                "postgres": {
                    "command": "postgres",
                    "args": ["-D", "/var/lib/postgresql/data"],
                    "working_dir": "/usr/bin",
                    "expected_exit_code": 0,
                    "restart_delay": 10
                },
                "redis": {
                    "command": "redis-server",
                    "args": ["/etc/redis/redis.conf"],
                    "working_dir": "/usr/bin",
                    "expected_exit_code": 0,
                    "restart_delay": 3
                },
                "node-app": {
                    "command": "node",
                    "args": ["app.js"],
                    "working_dir": "/Users/paul/Desktop/brantham-partners",
                    "expected_exit_code": 0,
                    "restart_delay": 2
                }
            }
        }

        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    # Fusionner avec la config par défaut
                    for key, value in default_config.items():
                        if key not in config:
                            config[key] = value
                    return config
            except Exception as e:
                self.logger.error(f"Erreur lors du chargement de la config: {e}")
                return default_config
        else:
            with open(self.config_file, 'w') as f:
                json.dump(default_config, f, indent=2)
            return default_config

    def save_config(self):
        """Sauvegarde la configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def start_process(self, process_name: str) -> bool:
        """Démarre un processus"""
        if process_name not in self.config["processes"]:
            self.logger.error(f"Process {process_name} non trouvé dans la configuration")
            return False

        process_config = self.config["processes"][process_name]

        try:
            # Vérifier si le processus tourne déjà
            if process_name in self.processes:
                try:
                    self.processes[process_name].pid
                    self.logger.info(f"Process {process_name} déjà en cours d'exécution")
                    return True
                except psutil.NoSuchProcess:
                    pass

            # Démarrer le processus
            env = os.environ.copy()
            env["PROCESS_NAME"] = process_name

            process = subprocess.Popen(
                [process_config["command"]] + process_config["args"],
                cwd=process_config.get("working_dir", "."),
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                start_new_session=True
            )

            # Vérifier que le processus a démarré
            time.sleep(1)
            if process.poll() is None:
                self.processes[process_name] = psutil.Process(process.pid)
                self.logger.info(f"Process {process_name} démarré avec PID {process.pid}")
                return True
            else:
                self.logger.error(f"Process {process_name} a échoué de démarrer")
                return False

        except Exception as e:
            self.logger.error(f"Erreur lors du démarrage de {process_name}: {e}")
            return False

    def stop_process(self, process_name: str) -> bool:
        """Arrête un processus"""
        if process_name in self.processes:
            try:
                process = self.processes[process_name]

                # Envoyer SIGTERM d'abord
                process.terminate()

                # Attendre 5 secondes
                try:
                    process.wait(timeout=5)
                except psutil.TimeoutExpired:
                    # Envoyer SIGKILL si le processus ne répond pas
                    process.kill()
                    process.wait()

                del self.processes[process_name]
                self.logger.info(f"Process {process_name} arrêté")
                return True

            except psutil.NoSuchProcess:
                del self.processes[process_name]
                return True
            except Exception as e:
                self.logger.error(f"Erreur lors de l'arrêt de {process_name}: {e}")
                return False
        return True

    def check_process(self, process_name: str) -> bool:
        """Vérifie l'état d'un processus"""
        process_config = self.config["processes"][process_name]

        if process_name not in self.processes:
            self.logger.warning(f"Process {process_name} n'est pas en cours d'exécution")
            return False

        try:
            process = self.processes[process_name]

            # Vérifier si le processus tourne
            if not process.is_running():
                self.logger.warning(f"Process {process_name} s'est arrêté")
                return False

            # Vérifier le code de sortie s'il a terminé
            if process.poll() is not None:
                exit_code = process.returncode
                if exit_code != process_config["expected_exit_code"]:
                    self.logger.warning(f"Process {process_name} a quitté avec code {exit_code}")
                    return False

            # Vérifier si le processus consomme trop de ressources
            cpu_percent = process.cpu_percent()
            memory_percent = process.memory_percent()

            if cpu_percent > 90:
                self.logger.warning(f"Process {process_name} consomme trop de CPU: {cpu_percent}%")

            if memory_percent > 80:
                self.logger.warning(f"Process {process_name} consomme trop de mémoire: {memory_percent}%")

            return True

        except psutil.NoSuchProcess:
            self.logger.warning(f"Process {process_name} n'existe plus")
            return False
        except Exception as e:
            self.logger.error(f"Erreur lors de la vérification de {process_name}: {e}")
            return False

    def restart_process(self, process_name: str) -> bool:
        """Redémarre un processus"""
        process_config = self.config["processes"][process_name]

        # Arrêter le processus
        self.stop_process(process_name)

        # Attendre le délai configuré
        time.sleep(process_config.get("restart_delay", 5))

        # Redémarrer le processus
        return self.start_process(process_name)

    def check_all_processes(self):
        """Vérifie tous les processus configurés"""
        for process_name in self.config["processes"]:
            if not self.check_process(process_name):
                if self.config.get("auto_restart", True):
                    self.logger.info(f"Tentative de redémarrage de {process_name}")
                    self.restart_process(process_name)

    def add_process(self, name: str, command: str, args: List[str] = None,
                   working_dir: str = None, expected_exit_code: int = 0):
        """Ajoute un nouveau processus à surveiller"""
        self.config["processes"][name] = {
            "command": command,
            "args": args or [],
            "working_dir": working_dir,
            "expected_exit_code": expected_exit_code,
            "restart_delay": 5
        }
        self.save_config()
        self.logger.info(f"Nouveau processus {name} ajouté à la surveillance")

    def remove_process(self, name: str):
        """Supprime un processus de la surveillance"""
        if name in self.config["processes"]:
            self.stop_process(name)
            del self.config["processes"][name]
            self.save_config()
            self.logger.info(f"Processus {name} supprimé de la surveillance")

    def get_stats(self) -> dict:
        """Retourne les statistiques de surveillance"""
        running_count = len(self.processes)
        total_count = len(self.config["processes"])
        uptime = datetime.now() - self.start_time

        return {
            "total_processes": total_count,
            "running_processes": running_count,
            "uptime": str(uptime).split('.')[0],
            "processes": {
                name: {
                    "running": name in self.processes,
                    "pid": self.processes[name].pid if name in self.processes else None,
                    "cpu": self.processes[name].cpu_percent() if name in self.processes else 0,
                    "memory": self.processes[name].memory_percent() if name in self.processes else 0
                }
                for name in self.config["processes"]
            }
        }

    def start_monitoring(self):
        """Démarre le monitoring continu"""
        self.logger.info("Démarrage du monitoring des processus")

        try:
            while True:
                self.check_all_processes()
                time.sleep(self.config.get("check_interval", 10))

        except KeyboardInterrupt:
            self.logger.info("Arrêt du monitoring demandé par l'utilisateur")
        finally:
            self.stop_all()

    def stop_all(self):
        """Arrête tous les processus"""
        self.logger.info("Arrêt de tous les processus")
        for process_name in list(self.processes.keys()):
            self.stop_process(process_name)

def main():
    parser = argparse.ArgumentParser(description="Process Watcher - Surveillance des processus")
    parser.add_argument("--start", action="store_true", help="Démarrer le monitoring")
    parser.add_argument("--stop", action="store_true", help="Arrêter tous les processus")
    parser.add_argument("--status", action="store_true", help="Afficher le statut")
    parser.add_argument("--list", action="store_true", help="Lister les processus")
    parser.add_argument("--add", nargs='+', metavar=('NAME', 'COMMAND', 'ARGS...'),
                       help="Ajouter un processus: nom commande args...")
    parser.add_argument("--remove", metavar="NAME", help="Supprimer un processus")
    parser.add_argument("--config", default="process_watcher.json", help="Fichier de configuration")

    args = parser.parse_args()

    watcher = ProcessWatcher(args.config)

    if args.add:
        name, command = args.add[0], args.add[1]
        args_list = args.add[2:] if len(args.add) > 2 else []
        watcher.add_process(name, command, args_list)

    elif args.remove:
        watcher.remove_process(args.remove)

    elif args.status:
        stats = watcher.get_stats()
        print("\n=== Statistiques Process Watcher ===")
        print(f"Total processus: {stats['total_processes']}")
        print(f"En cours d'exécution: {stats['running_processes']}")
        print(f"Uptime: {stats['uptime']}")

        for name, info in stats['processes'].items():
            status = "RUNNING" if info['running'] else "STOPPED"
            print(f"{name}: {status} | PID: {info['pid']} | CPU: {info['cpu']:.1f}% | Mem: {info['memory']:.1f}%")

    elif args.list:
        print("\n=== Processus Surveillance ===")
        for name in watcher.config["processes"]:
            status = "RUNNING" if name in watcher.processes else "STOPPED"
            print(f"{name}: {status}")

    elif args.start:
        watcher.start_monitoring()

    elif args.stop:
        watcher.stop_all()

    else:
        print("Process Watcher")
        print("Utilisez --help pour voir les options disponibles")
        watcher.get_stats()

if __name__ == "__main__":
    main()