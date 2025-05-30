# Khusus windows ya bang, block aja kalo pakai linux (gwe tuch)
# import preprocess
# import showenv
# preprocess.main()
# showenv.main()

# The fun part (pls banh aku nak tido)
from roboticstoolbox import ET
from math import radians as rad

scara = (
    ET.tz(0.2) *
    ET.Rz() * 
    ET.ty(-0.2) *
    ET.Ry(qlim=[rad(-90), rad(90)]) *
    ET.tz(0.6) *
    ET.Rz() *
    ET.ty(0.2) *
    ET.Ry(qlim=[rad(-90), rad(180)]) *
    ET.tz(0.6) *
    ET.Ry() *
    ET.ty(-0.2) *
    ET.Rx(qlim=[rad(-90), rad(180)]) *
    ET.tx(0.2) *
    ET.Rz() *
    ET.tz(-0.2)
    )

q = [
    rad(0),     # q0
    rad(15),    # q1
    rad(0),     # q2
    rad(90),   # q3
    rad(-120),  # q4
    rad(0),     # q5
    rad(0)      # q6
    ] 

scara.fkine(q).printline()
scara.teach(q)
