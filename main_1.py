# Khusus windows ya bang, block aja kalo pakai linux (gwe tuch)
# import preprocess
# import showenv
# preprocess.main()
# showenv.main()
import matplotlib
matplotlib.use('TkAgg')

# The fun part (pls banh aku nak tido ZZZZzzzzz)
from roboticstoolbox import ET
from math import pi, radians as rad

# bikin robot 
scara = (
    ET.Rz()* # 360deg
    ET.tz(qlim=[0.3,0.5])*ET.ty(qlim=[0.15,0.25])*
    ET.Ry()*
    ET.Rz(qlim=[rad(-100),rad(45)])* # tapi berputar putar (180 derajat)
    ET.ty(0.15)*ET.Ry()
)

# init pos
q = [
    0,
    0.3,
    0,
    0.15,
    rad(45),  # 90 derajat
    0
    ]

# plot
scara.fkine(q).printline()
scara.teach(q)