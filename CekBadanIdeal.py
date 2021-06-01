from tkinter import *
from tkinter import messagebox


def reset_entry():
    nama_tf.delete(0, 'end')
    berat_tf.delete(0, 'end')
    tinggi_tf.delete(0, 'end')


def hitung_bmi():
    kg = int(berat_tf.get())
    m = int(tinggi_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)


def ucapan():
    n = 0
    for n in range(6):
        print("Terimakasih", (n))
    n += 1


def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('Hasil Perhitungan',
                            f'Hallo! BMI = {bmi} Anda Tergolong Kurus')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('Hasil Perhitungan',
                            f'Hallo! BMI = {bmi} Anda Tergolong Normal/Ideal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('Hasil Perhitungan',
                            f'Hallo! BMI = {bmi} Anda Tergolong Gemuk')
    elif (bmi > 29.9):
        messagebox.showinfo('Hasil Perhitungan',
                            f'Hallo! BMI = {bmi} Anda Tergolong Obesitas')


app = Tk()
app.geometry('350x300')
app.title('Program Cek Badan Ideal')
app.config(bg='#a1eafb')

var = IntVar()
frame = Frame(app, padx=10, pady=10, bg='#a1eafb')
frame.pack(expand=True)

# Gender
gen_lb = Label(frame, text='Gender : ', bg='#a1eafb')
gen_lb.grid(row=1, column=1)
frame2 = Frame(frame)
frame2.grid(row=1, column=2, pady=5)

pria_rb = Radiobutton(frame2, text='Pria', variable=var, value=1, bg='#a1eafb')
pria_rb.pack(side=LEFT)

wanita_rb = Radiobutton(frame2, text='Wanita',
                        variable=var, value=2, bg='#a1eafb')
wanita_rb.pack(side=RIGHT)

# Nama
nama_lb = Label(frame, text="Nama : ", bg='#a1eafb')
nama_lb.grid(row=2, column=1)
nama_tf = Entry(frame, bg='#fdfdfd')
nama_tf.grid(row=2, column=2, pady=5)

# Berat
berat_lb = Label(frame, text="Berat Badan (kg) : ", bg='#a1eafb')
berat_lb.grid(row=3, column=1)
berat_tf = Entry(frame, bg='#fdfdfd')
berat_tf.grid(row=3, column=2, pady=5)

# Tinggi
tinggi_lb = Label(frame, text="Tinggi Badan (cm) : ", bg='#a1eafb')
tinggi_lb.grid(row=4, column=1)
tinggi_tf = Entry(frame, bg='#fdfdfd')
tinggi_tf.grid(row=4, column=2, pady=5)

# Button Hitung, Reset, Exit, Terimakasih
frame3 = Frame(frame)
frame3.grid(row=5, columnspan=3, pady=10)

hitung_btn = Button(frame3, text='Hitung', command=hitung_bmi,
                    bg='#4ecca3')
hitung_btn.pack(side=RIGHT)

keluar_btn = Button(frame3, text='Keluar',
                    command=lambda: app.destroy(), bg='#cf0000', fg='white')
keluar_btn.pack(side=LEFT)

reset_btn = Button(frame3, text='Reset', command=reset_entry,
                   bg='#3d6cb9', fg='white')
reset_btn.pack(side=LEFT)

trim_btn = Button(frame, text='Terimakasih',
                  command=ucapan, bg='#3d6cb9', fg='white')
trim_btn.grid(row=6, columnspan=3, pady=10)

app.mainloop()
