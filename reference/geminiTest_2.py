import matplotlib
matplotlib.use('TkAgg')

from roboticstoolbox import ET, ETS
from spatialmath import SE3
from math import radians as rad
import numpy as np
import matplotlib.pyplot as plt
import os

# Create output directory
os.makedirs('ikine_solutions', exist_ok=True)

# Define your robot ETS chain (same as you gave)
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

# Base joint values q_init
q_init = [
    rad(0),     # q0
    rad(15),    # q1
    rad(120),   # q2
    rad(-135),  # q3
    rad(0),     # q4
    rad(0)      # q5
]

# Variation values for q2, q4, q5
q2_vals = [rad(110), rad(120), rad(130)]      # around 120 degrees
q4_vals = [rad(-30), rad(0), rad(30)]
q5_vals = [rad(-60), rad(0), rad(45)]

qs = []

# Vary q2 only (index 2)
for val in q2_vals:
    q = q_init.copy()
    q[2] = val
    qs.append(q)

# Vary q4 only (index 4)
for val in q4_vals:
    q = q_init.copy()
    q[4] = val
    qs.append(q)

# Vary q5 only (index 5)
for val in q5_vals:
    q = q_init.copy()
    q[5] = val
    qs.append(q)

# Add 6 combos varying q2 & q4 (first two vals of q2)
for val2 in q2_vals[:2]:
    for val4 in q4_vals[:3]:
        q = q_init.copy()
        q[2] = val2
        q[4] = val4
        qs.append(q)
        if len(qs) >= 15:
            break
    if len(qs) >= 15:
        break

# Run IK and save images + print q text on image
for i, q_try in enumerate(qs, 1):
    T_goal = scara_ets.fkine(q_try)
    
    # Use IK solver, initialize at q_try to help convergence
    sol = scara_ets.ikine_LM(T_goal, q0=q_try)

    if sol.success:
        q_sol = sol.q
        print(f"Solution #{i} success: {[round(x,4) for x in q_sol]}")

        # Plot robot pose
        scara_ets.plot(q_sol, block=False)
        fig = plt.gcf()
        
        # Add joint values as text on image
        q_deg = [round(np.degrees(x), 1) for x in q_sol]
        textstr = '\n'.join([f'q{i}: {val}°' for i, val in enumerate(q_deg)])
        
        # Place text box in upper left corner
        plt.figtext(
            0.02, 0.98, textstr,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        )

        
        # Save image
        filename = f'ikine_solutions/solution_{i}.png'
        fig.savefig(filename)
        plt.close(fig)
    else:
        print(f"Solution #{i} IK failed")

print("Done! Images and q results saved in ./ikine_solutions/")