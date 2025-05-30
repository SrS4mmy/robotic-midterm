# Khusus windows ya bang, block aja kalo pakai linux (gwe tuch)
# import preprocess
# import showenv
# preprocess.main()
# showenv.main()

# The fun part (pls banh aku nak tido)
from roboticstoolbox import ET
from math import pi

scara = (
    ET.Rz()* # 360deg
    ET.tz(qlim=[0.3,0.5])*ET.ty(qlim=[0.15,0.25])*
    ET.Ry()*
    ET.Rz(qlim=[-2*pi/3,2*pi/3])* #putar naik turun 180deg max +90 - 90
    ET.ty(0.15)*ET.Ry()
)

q = [
    0,
    0.3,
    0,
    0.15,
    pi/2,
    0
    ]

scara.fkine(q).printline()
scara.teach(q)