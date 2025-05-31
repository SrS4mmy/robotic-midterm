import matplotlib
matplotlib.use('TkAgg')

from roboticstoolbox import ET, ETS
from math import radians as rad

# ikine use ETS
scara = ETS(
    ET.Rz() +                          # q1
    ET.tz(qlim=[0.3,0.5]) +            # q2
    ET.ty(qlim=[0.15,0.25]) +          # q3
    ET.Ry() +                          # q4
    ET.Rz(qlim=[rad(-100),rad(45)]) + # q5
    ET.ty(0.15) +                      # add length q5
    ET.Ry()                            # q6
)

# ke geminiAI, copy all code, set all q ke 0. "Give me a q combination that might works with my code"
q_true = [
    rad(30),   # q1: Rz (base rotation)
    0.4,       # q2: tz (between 0.3 - 0.5)
    0.2,       # q3: ty (between 0.15 - 0.25)
    rad(15),   # q4: Ry
    rad(-45),  # q5: Rz (within -100° to +45°)
    rad(10)    # q6: Ry
]

T_goal = scara.fkine(q_true)

# DOCnya aneh but ok. why? atleast it works
# aturlah bang peter, abang kan panitia
sol = scara.ikine_LM(T_goal, q0=q_true)

if sol.success:
    scara.fkine(sol.q).printline()
    scara.teach(sol.q)
else:
    print("Ikine goal not reached")
