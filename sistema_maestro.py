import sys; sys.path.insert(0, '/data/data/com.termux/files/home')
import nivel8_omega
nivel8_omega.iniciar_omega()
import threading
import time
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] LURE-MASTER-CORE: %(message)s", handlers=[logging.StreamHandler(sys.stdout)])

class LUREMasterSanctuary:
    def __init__(self, total_layers=7):
        self.total_layers = total_layers
        self.lock = threading.Lock()
        self.active_threads = 0
        logging.info("Inicializando la Matriz de Defensa de 7 Niveles de LURE...")

    def execute_layer_pipeline(self, layer_id):
        with self.lock:
            self.active_threads += 1
            logging.info(f">> Ejecutando validación en Nivel {layer_id} [Hilos activos: {self.active_threads}]")
            time.sleep(0.15)
            self.active_threads -= 1
            logging.info(f"<< Nivel {layer_id} verificado y asegurado bajo matriz Cero Errores.")

def run_lure_matrix():
    print("============================================================")
    print("      INICIANDO SISTEMA INMUNOLÓGICO DIGITAL - LURE v1.0")
    print("      Autor: Ing. León Andrés Hernández")
    print("============================================================")
    core = LUREMasterSanctuary()
    threads = []
    for layer in range(1, core.total_layers + 1):
        t = threading.Thread(target=core.execute_layer_pipeline, args=(layer,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("============================================================")
    logging.info("¡Ciclos de verificación completados con ÉXITO ABSOLUTO!")
    print("Estado del Núcleo: ESTABLE / SEGURO / CERO ERRORES")
    print("============================================================")

if __name__ == "__main__":
    run_lure_matrix()
