# image extraction for inverse kine soal 1
import matplotlib
matplotlib.use('TkAgg')

from roboticstoolbox import ET, ETS
from math import radians as rad, degrees as deg
import numpy as np
import matplotlib.pyplot as plt
import os
import random

# Output folder
os.makedirs('ikine_solutions/ikine_sol_final', exist_ok=True)

# Define robot using ETS
scara = ETS(
    ET.Rz() +                          # q1
    ET.tz(qlim=[0.3, 0.5]) +           # q2
    ET.ty(qlim=[0.15, 0.25]) +         # q3
    ET.Ry() +                          # q4
    ET.Rz(qlim=[rad(-100), rad(45)]) +# q5
    ET.ty(0.15) +                      # fixed offset
    ET.Ry()                            # q6
)

# Base joint config
q_base = [
    rad(90),   # q1
    0.4,       # q2
    0.2,       # q3
    rad(15),   # q4
    rad(-45),  # q5
    rad(10)    # q6
]

# Variation bounds
variation_degrees = {
    0: -40,     # q1: base rotation ±15°
    1: 0.05,   # q2: tz ±5cm
    2: 0.03,   # q3: ty ±3cm
    3: 60,     # q4: Ry ±60°
    4: 10,     # q5: Rz ±10°
    5: 5       # q6: Ry ±5°
}

# Generate 15 small varied q combinations
qs = []
for _ in range(15):
    q = q_base.copy()

    # Small deltas for each joint
    q[0] += rad(random.uniform(-variation_degrees[0], variation_degrees[0]))  # q1
    q[1] += random.uniform(-variation_degrees[1], variation_degrees[1])       # q2
    q[2] += random.uniform(-variation_degrees[2], variation_degrees[2])       # q3
    q[3] += rad(random.uniform(-variation_degrees[3], variation_degrees[3]))  # q4
    q[4] += rad(random.uniform(-variation_degrees[4], variation_degrees[4]))  # q5
    q[5] += rad(random.uniform(-variation_degrees[5], variation_degrees[5]))  # q6

    qs.append(q)

print(f"Generated {len(qs)} small-variation q vectors.")

# IK, Plotting and Saving
for i, q_test in enumerate(qs, 1):
    T_goal = scara.fkine(q_test)
    sol = scara.ikine_LM(T_goal, q0=q_test)

    if sol.success:
        q_sol = sol.q
        print(f"Solution #{i} success: {[round(deg(x), 2) for x in q_sol]}")

        # Plot and annotate
        scara.plot(q_sol, block=False)
        fig = plt.gcf()

        # Degrees output
        q_deg = [round(deg(x), 1) if i in [0,3,4,5] else round(x, 3) for i, x in enumerate(q_sol)]
        text_lines = [f'q{i+1}: {val}°' if i in [0,3,4,5] else f'q{i+1}: {val} m' for i, val in enumerate(q_deg)]
        text = '\n'.join(text_lines)

        plt.figtext(
            0.02, 0.98, text,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        )

        filename = f'ikine_solutions/ikine_sol_1/solution_{i}.png'
        fig.savefig(filename)
        plt.close(fig)
    else:
        print(f"Solution #{i} IK failed")

print("✅ All poses saved to 'ikine_solutions/ikine_sol_1'")
