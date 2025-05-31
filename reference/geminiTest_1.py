import matplotlib
matplotlib.use('TkAgg')

from roboticstoolbox import ET, ETS
from math import radians as rad, degrees as deg
import numpy as np
import matplotlib.pyplot as plt
import os
import random

# Create output folder
os.makedirs('ikine_solutions', exist_ok=True)

# Robot model as before
scara = ETS(
    ET.Rz() +                          # q1
    ET.tz(qlim=[0.3,0.5]) +           # q2
    ET.ty(qlim=[0.15,0.25]) +         # q3
    ET.Ry() +                         # q4
    ET.Rz(qlim=[rad(-100),rad(45)]) +# q5
    ET.ty(0.15) +                     # fixed offset after q5
    ET.Ry()                           # q6
)

# Base joint values
q_true = [
    rad(30),   # q1
    0.4,       # q2 (tz)
    0.2,       # q3 (ty)
    rad(15),   # q4
    rad(-45),  # q5
    rad(10)    # q6
]

# Limits from ET qlim for relevant joints
q2_lim = [0.3, 0.5]
q3_lim = [0.15, 0.25]
q4_lim = [-rad(20), rad(20)]  # small rotation range ±20°
q5_lim = [rad(-60), rad(0)]   # smaller than original for variation

qs = []

# Randomize 15 q vectors
for _ in range(15):
    q = q_true.copy()
    # Random q1 rotation full circle
    q[0] = random.uniform(-np.pi, np.pi)
    # Random translations within limits for q2, q3
    q[1] = random.uniform(*q2_lim)
    q[2] = random.uniform(*q3_lim)
    # Small rotations around q4, q5 limits
    q[3] = random.uniform(*q4_lim)
    q[4] = random.uniform(*q5_lim)
    # Keep q6 fixed for now
    q[5] = q_true[5]

    qs.append(q)

print(f"Generated {len(qs)} random test poses.")

# Run IK, plot, save results with joint values
for i, q_test in enumerate(qs, 1):
    T_goal = scara.fkine(q_test)
    sol = scara.ikine_LM(T_goal, q0=q_test)

    if sol.success:
        q_sol = sol.q
        print(f"Solution #{i} success: {[round(deg(x),2) for x in q_sol]}")

        scara.plot(q_sol, block=False)
        fig = plt.gcf()

        q_deg = [round(deg(x), 1) for x in q_sol]
        textstr = '\n'.join([f'q{i+1}: {val}°' for i, val in enumerate(q_deg)])

        plt.figtext(
            0.02, 0.98, textstr,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        )

        filename = f'ikine_solutions/solution_{i}.png'
        fig.savefig(filename)
        plt.close(fig)

    else:
        print(f"Solution #{i} IK failed")

print("Done! Check 'ikine_solutions' folder for images.")
