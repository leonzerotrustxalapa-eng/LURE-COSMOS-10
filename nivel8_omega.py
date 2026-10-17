import os, time, threading, hashlib
from datetime import datetime

def log(m):
    print(f"{datetime.now().strftime('%H:%M:%S')} [OMEGA-8] {m}")

def modulo_espejo_negro():
    while True:
        time.sleep(15)

def modulo_fantasma():
    archivo = "sistema_maestro.py"
    last = ""
    while True:
        try:
            h = hashlib.sha256(open(archivo,"rb").read()).hexdigest()
            if last and h != last:
                log("8B: Cambio detectado")
            last = h
        except: pass
        time.sleep(10)

def modulo_colmena():
    while True:
        try:
            os.makedirs("colmena_backup", exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            os.system(f"tar -czf colmena_backup/LURE_{ts}.tar.gz sistema_maestro.py 2>/dev/null")
            log(f"8C: Respaldo {ts} OK")
            files = sorted(os.listdir("colmena_backup"))
            if len(files) > 10:
                os.remove(f"colmena_backup/{files[0]}")
        except Exception as e:
            log(f"8C Error {e}")
        time.sleep(600)

def iniciar_omega():
    log("=== INICIANDO NIVEL 8 OMEGA ===")
    threading.Thread(target=modulo_espejo_negro, daemon=True).start()
    threading.Thread(target=modulo_fantasma, daemon=True).start()
    threading.Thread(target=modulo_colmena, daemon=True).start()
    log("NIVEL 8 OMEGA: 8A+8B+8C ACTIVOS")
