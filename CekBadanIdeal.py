from tkinter import *
from tkinter import messagebox


def reset_entry():
    nama_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')


def ucapan_kata():
    n = 0
    for n in range(6):
        print("Terimakasih", (n))
    n += 1


def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)


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
app.config(bg='#0f4b6e')

var = IntVar()
frame = Frame(app, padx=10, pady=10)
frame.pack(expand=True)

# Gender
gen_lb = Label(frame, text='Gender : ')
gen_lb.grid(row=1, column=1)
frame2 = Frame(frame)
frame2.grid(row=1, column=2, pady=5)

male_rb = Radiobutton(frame2, text='Pria', variable=var, value=1)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(frame2, text='Wanita', variable=var, value=2)
female_rb.pack(side=RIGHT)

# Name
nama_lb = Label(frame, text="Nama : ")
nama_lb.grid(row=2, column=1)
nama_tf = Entry(frame, bg='#c0fefc')
nama_tf.grid(row=2, column=2, pady=5)

# Height & Weight
weight_lb = Label(frame, text="Berat Badan (kg) : ",)
weight_lb.grid(row=3, column=1)
weight_tf = Entry(frame, bg='#c0fefc')
weight_tf.grid(row=3, column=2, pady=5)

height_lb = Label(frame, text="Tinggi Badan (cm) : ")
height_lb.grid(row=4, column=1)
height_tf = Entry(frame, bg='#c0fefc')
height_tf.grid(row=4, column=2, pady=5)

# Button Hitung, Reset, Exit, Terimakasih
frame3 = Frame(frame)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(frame3, text='Hitung', command=calculate_bmi,
                 bg='#0f4b6e', fg='white')
cal_btn.pack(side=LEFT)

ucapan_btn = Button(frame, text='Terimakasih', command=ucapan_kata)
ucapan_btn.grid(row=6, columnspan=3, pady=10)

reset_btn = Button(frame3, text='Reset', command=reset_entry)
reset_btn.pack(side=LEFT)

exit_btn = Button(frame3, text='Exit', command=lambda: app.destroy())
exit_btn.pack(side=RIGHT)

app.mainloop()
