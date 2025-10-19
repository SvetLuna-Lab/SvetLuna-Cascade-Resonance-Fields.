import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

Path("outputs/figures").mkdir(parents=True, exist_ok=True)

# Synthetic 3D field visualization
x = np.linspace(0, 10, 200)
y = np.linspace(0, 10, 200)
X, Y = np.meshgrid(x, y)
Z = np.sin(2*np.pi*X/3) * np.cos(2*np.pi*Y/5) + np.sin(2*np.pi*(X+Y)/7)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=60, cmap="plasma")
plt.colorbar(label="Resonance Intensity")
plt.title("Cascade Resonance — Interlayer Coupling Map")
plt.xlabel("Layer X")
plt.ylabel("Layer Y")
plt.tight_layout()
plt.savefig("outputs/figures/cascade_layers_map.png", dpi=300)
plt.close()

print("✅ Visualization complete — map saved to outputs/figures/cascade_layers_map.png")
