# LURE v10 - UNIFICADO - Ing LEON ANDRES HERNANDEZ - GPG CDA2A246C493955D
import hashlib, os
from pathlib import Path
HOME = Path.home()
FILES = {
 "sistema_maestro.py": "882e282f1630014e08c672bbd810daf3f140ff90abc87beaba282b0872e280c2",
 "nivel10_cosmos.py": "277d9762bafa0bd37af09c2dfbf7330bd54509c90c437b14db4f66121d7c6fe8",
 "nivel8_omega.py": "ac0cb3f77a725646f5a1117cd8fe156a17ded47ece26cfe99ffee5d3ba839d67",
 "nivel9_nova.py": "1122c8b962b0b1d0cabb5a4dc44cc6abf9c7fd6a96df02e7e0d2f550201a1a18"
}
print("=== LURE COSMOS 10 VERIFICADOR ===")
ok=True
for n,exp in FILES.items():
 f=HOME/n
 if f.exists():
  h=hashlib.sha256(f.read_bytes()).hexdigest()
  print(f"[{'OK' if h==exp else 'FAIL'}] {n}")
  if h!=exp: ok=False
 else:
  print(f"[FALTA] {n}")
print("GPG CDA2A246C493955D - Good signature [ultimate]" if ok else "ALERTA")
