import keyboard
import time
import threading
from datetime import datetime

def auto_refresh():
    """Boucle qui envoie la commande toutes les 5 minutes."""
    while True:
        time.sleep(300)  # 5 minutes
        now = datetime.now().strftime("%H:%M:%S")
        keyboard.send("ctrl+shift+windows+b")
        print(f"[{now}] | Rafraîchissement automatique envoyé (Ctrl+Shift+Win+B)")

def manual_test():
    """Déclenchement manuel via Ctrl+T"""
    now = datetime.now().strftime("%H:%M:%S")
    keyboard.send("ctrl+shift+windows+b")
    print(f"[{now}] | Test manuel déclenché (Ctrl+Shift+Win+B)")

print("=== GPU Refresh Utility ===")
print("Appuie sur CTRL+T pour tester manuellement.")
print("Rafraîchissement auto toutes les 5 minutes.")
print("Appuie sur CTRL+C pour quitter.\n")

# Lancer la boucle automatique dans un thread
threading.Thread(target=auto_refresh, daemon=True).start()

# Écoute permanente du raccourci CTRL+T
keyboard.add_hotkey("ctrl+t", manual_test)

# Boucle principale
try:
    keyboard.wait()  # attend indéfiniment
except KeyboardInterrupt:
    print("\nProgramme arrêté par l'utilisateur.")
