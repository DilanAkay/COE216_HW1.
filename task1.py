import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1) Frequencies
# -----------------------------
f0 = 37
f1 = f0
f2 = f0 / 2
f3 = 10 * f0

# -----------------------------
# 2) Sampling frequency
# -----------------------------
fs = 5000  # Nyquist condition satisfied (fs > 2*f3)

# -----------------------------
# 3) Dynamic time windows (3 periods each)
# -----------------------------
T1 = 1 / f1
T2 = 1 / f2
T3 = 1 / f3

t1 = np.arange(0, 3*T1, 1/fs)
t2 = np.arange(0, 3*T2, 1/fs)
t3 = np.arange(0, 3*T3, 1/fs)

# -----------------------------
# 4) Signals
# -----------------------------
x1 = np.sin(2*np.pi*f1*t1)
x2 = np.sin(2*np.pi*f2*t2)
x3 = np.sin(2*np.pi*f3*t3)

# -----------------------------
# 5) Plot three signals (same window, 3 subplots)
# -----------------------------
plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.plot(t1, x1)
plt.title("f1 = 37 Hz (3 Periods)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3,1,2)
plt.plot(t2, x2)
plt.title("f2 = 18.5 Hz (3 Periods)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3,1,3)
plt.plot(t3, x3)
plt.title("f3 = 370 Hz (3 Periods)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

# -----------------------------
# 6) Sum of three signals (separate graph)
# -----------------------------
# For sum, use common time axis (shortest duration)
t_sum = np.arange(0, 3*T3, 1/fs)

x_sum = (np.sin(2*np.pi*f1*t_sum) +
         np.sin(2*np.pi*f2*t_sum) +
         np.sin(2*np.pi*f3*t_sum))

plt.figure()
plt.plot(t_sum, x_sum)
plt.title("Sum of Three Signals")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()