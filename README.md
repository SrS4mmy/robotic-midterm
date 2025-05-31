# Repo UTS Robotika dan Aplikasi

Sebuah repository tugas uts matkul robotika dan aplikasi UII.

Tutorial pakai:
    soal nomor 1 fkine = main_1
    soal nomor 2 fkine = main_2
    soal nomor 1 ikine = main_1_2
    soal nomor 2 ikine = main_2_2

FOR WINDOWS:
- silahkan blok (ctrl + /) pada bagian preprocess dan showenv agar skip check library
- silahkan menambahkan untuk menampilkan backend matplotlib dari pyqt ke tkinter
import matplotlib
matplotlib.use('TkAgg')

FOR LINUX:
- silahkan gunakan preprocess dan showenv untuk memastikan anda menggunakan venv yang benar
- tidak perlu menambahkan atribut TkAgg pada untuk matplotlib, namun gunakan backend pyqt6 dengan cara
pip install pyqt6

Update 31/5/2025:
- Adds Tool for Export image di ./reference/, made with GeminiAI with prompt "Make me 15 q combination that might works, export the image and show the result too in terminal"