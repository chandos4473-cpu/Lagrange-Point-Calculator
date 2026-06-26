# Dynamic Lagrange Point Coordinate Visualizer

An interactive orbital mechanics simulator and visualization dashboard built using **Python 3.9**, **Streamlit**, and **Matplotlib**. This application dynamically computes and vectors the 2D coordinate positions ($L_1$ through $L_5$) for multi-body celestial systems using dimensionless, normalized spatial rules.

Built as an official software entry for the **Hack Club Stardance Challenge** under handle `@chandos4473`.

---

## How It Works (The Engineering Logic)

Calculating orbital mechanics using raw SI units (meters and kilograms) introduces massive scaling distortions. For example, the Sun is $10^{30}\text{ kg}$ while the Earth is $10^{24}\text{ kg}$, separated by 150 billion meters. Attempting to render these raw coordinates causes text labels to smash together and planet graphics to compress into invisible sub-pixels.

To solve this, this simulator treats the workspace as a **Dimensionless System**. 
* The primary star is permanently anchored at the spatial origin `(0, 0)`.
* The secondary planet is positioned on the horizontal axis at exactly `(R, 0)`, where $R$ is a variable scaling unit (defaulting to 10).
* All five Lagrange equilibrium points are dynamically mapped as algebraic ratios relative to this coordinate backbone.

### The Mathematical Engine

The background script automatically parses the selected body masses to derive the system mass ratio ($\mu$):

$$\mu = \frac{M_2}{M_1 + M_2}$$

1. **Collinear Points ($L_1, L_2, L_3$):** Pinned directly to the horizontal $X$-axis. $L_1$ and $L_2$ sit inside the planet's gravitational boundary, determined by the **Hill Radius ($r_h$)** equation translated into normalized grid space:
   $$r_h = R \times \sqrt[3]{\frac{\mu}{3}}$$
   * **$L_1$ (Inner Node):** Sit exactly $r_h$ units inside the planet's path: $x = R - r_h$
   * **$L_2$ (Outer Node):** Sit exactly $r_h$ units outside the planet's path: $x = R + r_h$
   * **$L_3$ (Counter Node):** Positioned on the exact opposite side of the star, slightly perturbed by the planetary pull: $x = 0 - R \times (1 + \frac{5}{12}\mu)$

2. **Triangular Points ($L_4, L_5$):** These stable locations form perfect equilateral triangles with the star and planet. Because an equilateral triangle has interior angles of $60^\circ$, we apply standard trigonometric constants ($\cos(60^\circ) = 0.5$ and $\sin(60^\circ) = \frac{\sqrt{3}}{2}$) to map them into 2D space:
   * **$L_4$ (Leading Node):** Hovering $60^\circ$ ahead of the planet: $(R \times 0.5, \ R \times \frac{\sqrt{3}}{2})$
   * **$L_5$ (Trailing Node):** Hovering $60^\circ$ behind the planet: $(R \times 0.5, \ -R \times \frac{\sqrt{3}}{2})$

---

## Code Architecture Breakdown

The program is organized into 5 modular execution nodes:
* **Block 1: Framework Setup:** Initializes the Streamlit wide-screen browser viewport and imports `numpy` and `matplotlib`.
* **Block 2: Preset Selection Layer:** Runs a Python 3.9 compatible `if-elif-else` conditional array to toggle between real-world balances (Sun-Earth, Sun-Jupiter), a physics-breaking "Inverse" model where the planet out-masses the star, and manual slider inputs.
* **Block 3: Spatial Matrix Calculations:** Executes the dynamic math operations outlined above instantly upon adjusting a parameter.
* **Block 4: Matplotlib Graphic Compilation:** Generates a vector chart featuring a deep space-black layout canvas (`#000000`), custom circular orbital path tracks, distinct marker crosshairs, and white staggered coordinate flag annotations.
* **Block 5: Streamlit Web UI Split:** Divides the user viewport into a metric logging table column on the left and a live-rendering plot graphic container on the right.

---

## Local Installation & Execution

1. Clone this repository to your machine.
2. Open a terminal inside the project directory and install the background module dependencies:
   ```bash
   pip install numpy matplotlib streamlit
   ```
3. Boot up the local interactive web host application:
   ```bash
   python -m streamlit run LagrangePointCalc.py
   ```
4. Open your web browser to `http://localhost:8501`.

---

## Build Status & Project Checklist

- [x] Simple Lagrange point calculation code using raw 1D physics constants

- [x] Implement 2D vector coordinate mapping arrays ($L_1$ through $L_5$)
      
- [x] Fix system scale distortions by designing a clean 10-unit dimensionless coordinate system
      
- [x] Creating simple single systems (Sun-Earth hardcoded parameters)
      
- [x] Build smooth non-overlapping staggered text annotation strings inside Matplotlib graphics
      
- [x] Creating multiple systems and fully customizable systems using multi-variable slider panels
      
- [x] Inject custom automated system presets (Sun-Jupiter real-world mass ratio calculations)
      
- [x] Create an extreme theoretical "Inverse Scenario" toggle where the planet out-masses the star
      
- [x] Refactor background syntax arrays to support Python 3.9 environments using conditional logic
      
- [x] Migrate full backend physics engine into an interactive browser dashboard using Streamlit
      
- [x] Deploy finalized code scripts and development documentation checklist to GitHub cloud
