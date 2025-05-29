
import preprocess
import showenv

preprocess.main()
showenv.main()

print("early process completed")

import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH
import matplotlib.pyplot as plt

L1 = 0.5  
L2 = 0.5  
L3 = 0.4 
L4 = 0.3 

articulated = DHRobot([
    RevoluteDH(d=L1, a=0, alpha=np.pi/2),  # Axis 1
    RevoluteDH(d=0,   a=L2, alpha=0),      # Axis 2
    RevoluteDH(d=0,   a=L3, alpha=0),      # Axis 3
    RevoluteDH(d=0,   a=L4, alpha=0)       # Axis 4
], name='Latihan Articulated')
print(articulated)

theta1_vals = np.linspace(0, np.pi/2, 10)
theta2_vals = np.linspace(0, np.pi/2, 10)

print("\nForward Kinematics Results:")
for t1 in theta1_vals:
    for t2 in theta2_vals:
        q = [t1, t2, 0, 0]  
        T = articulated.fkine(q)
        print(f"Theta1: {np.degrees(t1):.0f}°, Theta2: {np.degrees(t2):.0f}° => Pose:\n{T}")

articulated.teach([0, 0, 0, 0])