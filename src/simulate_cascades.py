import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

Path("outputs/figures").mkdir(parents=True, exist_ok=True)

def generate_layer(freq_shift, phase_shift, amplitude=1.0):
    x = np.linspace(0, 10, 2000)
    wave = amplitude * np.sin(2 * np.pi * (x * freq_shift) + phase_shift)
    noise = np.random.normal(0, 0.2, len(x))
    return wave + noise

# Generate 5 resonance layers
layers = []
for i in range(1, 6):
    layers.append(generate_layer(i * 0.25, i * np.pi / 6, amplitude=1 / i))

# Combine into cascade field
cascade = np.sum(layers, axis=0)

plt.figure(figsize=(12, 5))
plt.plot(cascade, color='deepskyblue')
plt.title("Cascade Resonance Field — Simulated Dark Energy Flow")
plt.xlabel("Spatial coordinate (normalized)")
plt.ylabel("Resonance amplitude")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/figures/cascade_field.png", dpi=300)
plt.close()

print("✅ Cascade field simulation completed — output saved to outputs/figures/cascade_field.png")
