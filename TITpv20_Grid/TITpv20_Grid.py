from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('400x350')

label_valik = Label(text='Выбери из списка  => ',font=("Arial", 15))
label_valik.grid(row=0,column=0)

LB = Listbox(height =7, width=30)
LB.grid(row=0,column=1)

year_v = StringVar() # текстовая переменная
loc_v = StringVar()
image_v = StringVar()
year_v.set(0)       # 0, чтобы не было галочки
loc_v.set(0)
image_v.set(0)

cb_year = Checkbutton(text='Год', var = year_v)
cb_year.grid(row=1,column=0,sticky='w')
cb_location = Checkbutton(text='Местоположение',var = loc_v)
cb_location.grid(row=2,column=0,sticky='w')
cb_image = Checkbutton(text='Изображение',var = image_v)
cb_image.grid(row=3,column=0,sticky='w')

def valik():
        global can, foto
        can.delete(ALL)
        if LB.curselection() != ():   # если выбор не пустой
                nr = LB.curselection()   
                chudo = LB.get(nr)       
                nr=nr[0];chudo_y='';chudo_l='' # первый элемент из кортежа
                if year_v.get() == '1':
                        chudo_y = goda[nr]
                if loc_v.get() == '1':
                        chudo_l = loc[nr]
                label_info.configure(text=chudo + '\n' + chudo_y+ '\n' + chudo_l)
                if image_v.get() == '1':   
                    foto = PhotoImage(file = photos[nr])
                    can.create_image(0,0,image=foto,anchor=NW)
                
        else:   
                messagebox.showinfo('Ошибка!','Выбери чудо света!')

nupp=Button(text='Выбор',width=15,command=valik)
nupp.grid(row=2,column=1)

label_info = Label(text="",borderwidth=1,relief="solid",font=("Arial", 10),width=20,height=4)
label_info.grid(row=4,column=0)

can = Canvas(root,width=150,height=150,bg='grey')
can.grid(row=4,column=1)


chudesa=['Пирамида Хеопса','Висячие сады Семирамиды','Статуя Зевса в Олимпии',
            'Храм Артемиды Эфесской','Мавзолей в Галикарнасе','Колосс Родосский',
            'Александрийский маяк']
goda = ['2550 г. до н. э.','600 г. до н. э.', '435 г. до н. э.',
            '550 г. до н. э.','351 г. до н. э.','между 292 и 280 гг. до н. э.',
                'III век до н. э.']

loc = ['Гиза','Вавилон','Олимпия','Эфес','Галикарнас','Родос','Александрия']

photos = ["1_heops.png","2_semiram.png","3_zevs.png","4_atrem.png","5_mavz.png",
                  "6_rodos.png","7_majak.png"]

for ch in chudesa:
	LB.insert(END,ch) # добавление чудес из списка Listbox

root.mainloop()

