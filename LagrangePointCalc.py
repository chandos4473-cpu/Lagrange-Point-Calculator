import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(page_title="Relative Lagrange Point Location Calculator", layout = "wide")
st.title("Dynamic Lagrange Point Co-ord Calculator")
st.markdown("Adjust the configurations in the sidebar to edit the orbital system bountaries")

st.sidebar.header("System Parameters")

system_preset = st.sidebar.selectbox("Choose a system preset", ["Sun-Earth", "Sun-Jupiter", "Inverse", "Fully Manual Sliders"])

if system_preset == "Sun-Earth":
    M1 = 1.989e30
    M2 = 5.972e24
    R = 10.0
    st.sidebar.info("Loaded Sun-Earth Defaults")
elif system_preset == "Sun-Jupiter":
    M1 = 1.989e30
    M2 = 1.898e27
    R = 12.0
    st.sidebar.info("Loaded Sun-Jupiter Defaults")
elif system_preset == "Inverse":
    M1 = 5.972e24
    M2 = 1.989e30
    R = 10.0
    st.sidebar.warning("Inverse physics loaded!")
else:
    star_exp = st.sidebar.slider("Star Mass Factor (10^30 kg)", min_value=0.1, max_value=2000.0, value=5.972, step=1.0)
    M1 = star_exp * 1e30

    planet_exp = st.sidebar.slider("Planet Mass Factor (10^24 kg)", min_value=1.0, max_value=2000.0, value=10.0, step=1.0)
    M2 = planet_exp * 1e24

    R = st.sidebar.slider("Planet orbit radius (Units)", min_value=5.0, max_value=20.0, value=10.0, step=1.0)


mu = M2 / (M1 + M2)

    

xM1 = 0.0
xM2 = R

r_h = R * (mu / 3) ** (1/3)

x_L1 = xM2 - r_h
y_L1 = 0

x_L2 = xM2 + r_h
y_L2 = 0

x_L3 = xM1 - R * (1 + 5 * mu / 12)
y_L3 = 0

x_L4 = R * 0.5
y_L4 = R * (3**0.5 / 2)

x_L5 = R * 0.5
y_L5 = -R * (3**0.5 / 2)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor("#575757")
fig.patch.set_facecolor("#575757")

ax.scatter(xM1, 0, color="#f9d71c", s=400, label="Sun (M1)", edgecolors="orange", zorder=3)
ax.scatter(xM2, 0, color="#4ba3e3", s=150, label="Planet (M2)", zorder=3)

orbit_circle = plt.Circle((0, 0), R, color="#4ba3e3", fill=False, linestyle="--", alpha=0.4, label="Planet Orbit")
ax.add_artist(orbit_circle)

ax.scatter([x_L1, x_L2, x_L3], [y_L1, y_L2, y_L3], color="#ff4b4b", s=120, marker="x", linewidth=2.5, label="Unstable (L1,L2,L3)", zorder=4)
ax.scatter([x_L4, x_L5], [y_L4, y_L5], color="#00aa66", s=120, marker="^", label="Stable (L4,L5)", zorder=4)

offset = R * 0.05
ax.text(x_L1 - 0.3, y_L1 + offset, f"L1\n({x_L1:.4f}, 0)", fontsize=9, ha="right", fontweight="bold")
ax.text(x_L2 + 0.3, y_L2 + offset, f"L2\n({x_L2:.4f}, 0)", fontsize=9, ha="left", fontweight="bold")
ax.text(x_L3, y_L3 + offset, f"L3\n({x_L3:.4f}, 0)", fontsize=9, ha="center", fontweight="bold")
ax.text(x_L4, y_L4 + offset, f"L4\n({x_L4:.1f}, {y_L4:.1f})", fontsize=9, ha="center", fontweight="bold")
ax.text(x_L5, y_L5 - offset, f"L5\n({x_L5:.1f}, {y_L5:.1f})", fontsize=9, ha="center", va="top", fontweight="bold")

padding = R * 1.3
ax.set_xlim(-padding, padding)
ax.set_ylim(-padding, padding)
ax.set_aspect("equal")

ax.grid(True, linestyle=":", alpha=0.5, color="#888888")
ax.axhline(0, color="#888888", linewidth=1, alpha=0.3)
ax.axvline(0, color="#888888", linewidth=1, alpha=0.3)
ax.legend(loc="upper right")

col1, col2 = st.columns([1,2])

with col1:
    st.subheader("Calculated metrics")
    st.metric(label="System mass ratio (μ)", value=f"{mu:.4e}")
    st.metric(label="Hill radius boundary (Units)", value=f"{r_h:.3f}")
    st.markdown("L point coordinate positions")
    st.success(f"L1: ({x_L1:.3f}, 0.000)")
    st.success(f"L2: ({x_L2:.3f}, 0.000)")
    st.success(f"L3: ({x_L3:.3f}, 0.000)")
    st.info(f"L4: ({x_L4:.2f}, {y_L4:.2f})")
    st.info(f"L5: ({x_L5:.2f}, {y_L5:.2f})")

with col2:
    st.subheader("Interactive Orbital System")
    st.pyplot(fig)