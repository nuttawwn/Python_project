from tkinter import *
import math

def cal_bmi (event):
    h = math.pow(float(txt_height.get())/100,2)
    w = int(txt_weight.get())
    r = (w / h)
    result = float("{:.1f}".format(r)) # แปลงค่าทศนิยมเป้น 2 ตำแหน่ง
    if result >= 30 :
        label_result.configure(text="โรคอ้วนอันตราย !!! ")
        label_result_int.configure(text=result)

    elif result >= 25.0 and result <= 29.9 :
        label_result.configure(text="โรคอ้วน")
        label_result_int.configure(text=result)

    elif result >= 23.0 and result <= 24.9 :
        label_result.configure(text="น้ำหนักเกินมาตราฐาน")
        label_result_int.configure(text=result)

    elif result >= 18.5 and result <= 22.9 :
        label_result.configure(text="สมส่วน")
        label_result_int.configure(text=result)

    else:
        label_result.configure(text="น้ำหนักต่ำกว่าเกณฑ์")
        label_result_int.configure(text=result)

main_widow_1 = Tk()

#ข้อมูลของส่วนสูง
label_height = Label(main_widow_1,text = "ส่วนสูง",font = ("TH sarabun new",15)).grid(row = 0,column = 0)
label_height_unit = Label(main_widow_1,text = "Cm.",font = ("TH sarabun new",15)).grid(row = 0,column = 2)
txt_height = Entry(main_widow_1,font = ("TH sarabun new",15))
txt_height.grid(row = 0,column = 1)

#ข้อมูลของน้ำหนัก
label_weight = Label(main_widow_1,text = "น้ำหนัก",font = ("TH sarabun new",15)).grid(row = 1,column = 0)
label_weight_unit = Label(main_widow_1,text = "Kg.",font = ("TH sarabun new",15)).grid(row = 1,column = 2)
txt_weight = Entry(main_widow_1,font = ("TH sarabun new",15))
txt_weight.grid(row = 1,column = 1)

#ข้อมูลของผลลัพธ์ตัวเลข
label_result_int = Label(main_widow_1,text = "ผลลัพธ์",font = ("TH sarabun new",15))
label_result_int.grid(row = 2,column = 1)
#ข้อมูลเกณฑ์ของผลลัพธ์
label_result = Label(main_widow_1,text = "อยู่ในเกณฑ์",font = ("TH sarabun new",15))
label_result.grid(row = 3,column = 1)

#ปุ่มคำนวณBMI
btn_cal = Button(main_widow_1,text = "คำนวณ",font = ("TH sarabun new",13))
btn_cal.bind('<Button-1>',cal_bmi)
btn_cal.grid(row = 4,column = 1)

main_widow_1.mainloop()
