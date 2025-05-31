# image extraction for inverse kine soal 2
import matplotlib
matplotlib.use('TkAgg')

from roboticstoolbox import ET, ETS
from spatialmath import SE3
from math import radians as rad
import numpy as np
import matplotlib.pyplot as plt
import os

# Create output directory
os.makedirs('ikine_solutions/ikine_sol_2', exist_ok=True)

# Define the SCARA-like robot using ETS
scara_ets = ETS(
    ET.tz(0.2) +
    ET.Rz() +                                   # q0
    ET.ty(-0.2) +
    ET.Ry(qlim=[rad(-90), rad(90)]) +           # q1
    ET.tz(0.6) +
    ET.Ry(qlim=[rad(-120), rad(180)]) +         # q2
    ET.tz(0.6) +
    ET.Ry() +                                   # q3
    ET.ty(-0.2) +
    ET.Rx(qlim=[rad(-120), rad(180)]) +         # q4
    ET.tx(0.2) +
    ET.Rz() +                                   # q5
    ET.tz(-0.2)
)

# Base initial joint values
q_init = [
    rad(0),     # q0
    rad(15),    # q1
    rad(120),   # q2
    rad(-135),  # q3
    rad(0),     # q4
    rad(0)      # q5
]

# Small gentle variation ranges +- 20 deg
q1_vals = [rad(-5), rad(15), rad(35)]     # Base joint rotation
q2_vals = [rad(100), rad(120), rad(140)]  # Arm vertical
q4_vals = [rad(-30), rad(0), rad(30)]     # Joint 4 swing
q5_vals = [rad(-45), rad(0), rad(45)]     # Final wrist rotation

qs = []

# Vary q1 slightly
for val in q1_vals:
    q = q_init.copy()
    q[1] = val
    qs.append(q)

# Vary q2 slightly
for val in q2_vals:
    q = q_init.copy()
    q[2] = val
    qs.append(q)

# Vary q4 more noticeably
for val in q4_vals:
    q = q_init.copy()
    q[4] = val
    qs.append(q)

# Vary q5 more noticeably
for val in q5_vals:
    q = q_init.copy()
    q[5] = val
    qs.append(q)

# If under 15, vary q1 + q4 combinations
if len(qs) < 15:
    for val1 in q1_vals:
        for val4 in q4_vals:
            if len(qs) >= 15:
                break
            q = q_init.copy()
            q[1] = val1
            q[4] = val4
            qs.append(q)

# IK solve and image dump
for i, q_try in enumerate(qs, 1):
    T_goal = scara_ets.fkine(q_try)
    sol = scara_ets.ikine_LM(T_goal, q0=q_try)

    if sol.success:
        q_sol = sol.q
        print(f"Solution #{i} success: {[round(np.degrees(x), 2) for x in q_sol]}")

        scara_ets.plot(q_sol, block=False)
        fig = plt.gcf()

        # Annotate joint values
        q_deg = [round(np.degrees(x), 1) for x in q_sol]
        textstr = '\n'.join([f'q{j}: {val}°' for j, val in enumerate(q_deg)])

        plt.figtext(
            0.02, 0.98, textstr,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        )

        # Save figure
        filename = f'ikine_solutions/ikine_sol_2/solution_{i}.png'
        fig.savefig(filename)
        plt.close(fig)
    else:
        print(f"Solution #{i} IK failed")

print("Done! Images and q results saved in ./ikine_solutions/ikine_sol_2/")
