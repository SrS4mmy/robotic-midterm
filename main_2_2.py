# on geminiAI, "[Code main_2.py] From this code, modify this code to works like main_1_2.py"

import matplotlib
matplotlib.use('TkAgg')

from roboticstoolbox import ET, ETS
from math import radians as rad

scara_ets = ETS(
    ET.tz(0.2) +
    ET.Rz() +                                    # q0
    ET.ty(-0.2) +
    ET.Ry(qlim=[rad(-90), rad(90)]) +            # q1
    ET.tz(0.6) +
    ET.Ry(qlim=[rad(-120), rad(180)]) +          # q2
    ET.tz(0.6) +
    ET.Ry() +                                    # q3
    ET.ty(-0.2) +
    ET.Rx(qlim=[rad(-120), rad(180)]) +          # q4
    ET.tx(0.2) +
    ET.Rz() +                                    # q5
    ET.tz(-0.2)
)

# on geminiAI, "[Code main_2_2.py] from this code with all q = 0. make me a possible "
q_true = [
    rad(0),     # q0: Rz
    rad(15),    # q1: Ry
    rad(120),   # q2: Ry
    rad(-135),  # q3: Ry
    rad(0),     # q4: Rx
    rad(0)      # q5: Rz
]

T_goal = scara_ets.fkine(q_true)

sol = scara_ets.ikine_LM(T_goal, q0=q_true)

if sol.success:
    scara_ets.fkine(sol.q).printline()
    scara_ets.teach(sol.q)
else:
    print("IK not reahed")
