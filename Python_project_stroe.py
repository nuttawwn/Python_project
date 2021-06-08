def title_menu (): #ส่วนไตเติ้ลเมนู
    print("ยินดีต้องรับเข้าสู่ระบบ")
    print("กรูณาป้อนข้อมูลรหัสผู้ใช้งาน")
    return login()

def login (): #ส่วน Login เข้าโปรแกรม
    un = input("Username : ")
    pw = input("Password : ")
    if un == "admin" and pw == "1234":
        print("เข้าสู่ระบบเรียบร้อยแล้ว")
        return show_menu (un)
    else:
        return wrong_user ()

def wrong_user (): #ส่วนป้องกันกรณีใส่รหัสผิดตอนเข้าโปรแกรม
    print("ใส่รหัสผ่านไม่ถูกต้อง กรุณาใส่อีกครั้ง")
    return login()

def show_menu (un): #ส่วนแสดงเมนูเมื่อเข้าโปรแกรม
    print("\nยินดีตอนรับ สวัสดีครับ",un)
    print("กรุณาเลือกระบบงานที่ต้องการทำงาน")
    print("1.โปรแกรมคำนวณเกรด")
    print("2.โปรแกรมคำนวณค่าใช้จ่าย")
    print("3.โปรแกรมคำนวณวิชาฟิสิกส์")
    print("4.โปรแกรมตำนวณเลข")
    print("5.โปรแกรมที่อยากให้พัฒนา")
    return select_menu(un)

def select_menu (un): #ส่วนเลือกเมนูเมื่อเข้าโปรแกรม
    job = input("\nกรุณาเลือกโปแกรมที่ต้องการ  : ")
    if job == "1" :
        return grade_cal(un)
    elif job == "2" :
        return price_cal (un)
    elif job == "3" :
        return physi_cal (un)
    elif job == "4" :
        return math_cal (un)
    elif job == "5" :
        return consult (un)
    elif job == "exit" or job == "Exit" or job == "EXIT":
        exit()
    else:
        return wrong_menu (un)

def wrong_menu (un): #ส่วนป้องกันกรณีเลือกเมนูผิด
    print("\nคุณเลือกเมนูไม่ถูกต้อง")
    return select_menu (un)

def exit_programe (un): #ส่วนสอบถามความต้องการใช้งานโปรแกรม
    print("\nคุณต้องการใช้งานต่อมั้ย")
    print("1.หากต้องการเล่นต่อพิมพ์ Y ")
    print("2.หากไม่ต้องหารใช้งานต่อพิมพ์ N ")
    print("3.หากต้องการเปลี่ยนรหัสผู้ใช้งานให้พิมพ์ C")
    ans = input("Y/N or C: ")
    if ans == "Y" or ans == "y" :
        return show_menu (un)
    elif ans == "N" or ans == "n" :
        exit()
    elif ans == "C" or ans == "c" :
        return title_menu()
    else:
        print("\nคุณเลือกเมนูไม่ถูกต้อง")
        return exit_programe(un)

def grade_cal (un): #ส่วนโปรแกรมคำนวณเกรด
    print("\nโปกแกรมคำนวณเกรด")
    grade = int(input("กรุณาระบุคะแนนปลายภาคของคุณ :"))
    if grade >= 80:
        print("คุณเกรด A")
    elif grade >= 76 and grade <= 79:
        print("คุณได้เกรด B+")
    elif grade >= 71 and grade <= 75:  # จะทำเงื่่อนไข elif เมื่อเงื่อนไขด้านบนเป็นเท็จ
        print("คุณได้เกรด B")
    elif grade >= 66 and grade <= 70:
        print("คุณได้เกรด C+")
    elif grade >= 61 and grade <= 65:
        print("คุณได้เกรด C")
    elif grade >= 56 and grade <= 60:
        print("คุณได้เกรด D+")
    elif grade >= 50 and grade <= 55:
        print("คุณได้เกรด D")
    else:
        print("คุณสอบไม่ผ่าน")
    return exit_programe(un)

def price_cal (un): #ส่วนโปรแกรมคำนวณราคา
    print("\nรายการค่าใช้จ่ายทั้งหมดที่ต้องชำระ")
    price = int(input("ราคาสินค้า : "))
    # vat = int(input("ราคาภาษี : "))
    vat = (7 / 100)
    vat_show = (price * vat)
    result = price + (price * vat)
    float(result)
    print("\nจำนวนราคาสินค้าทั้งหมด : ", price, "  บาท")
    print("\nจำนวนภาษีที่ชำระออกไป : ", vat_show, " บาท")
    print("\nรวมค่าใช้จ่ายทั้งหมดที่ต้องชำระ", result, "บาท")
    return exit_programe(un)

def physi_cal (un): #ส่วนโปรแกรมคำนวณความเร็วต้นวิชาฟิสิกส์
    print("\nโปรแกรมคำนวณหาระยะทางที่เคลื่อนที่ได้ ต่อ 1 หน่วยเวลา")
    s = int(input("ระยะทางที่เคลื่อนที่ได้ (หน่วยเป็น เมตร) : "))
    t = int(input("ระยะเวลาที่ใช้เคลื่อนที่ (หน่วยเป็น วินาที) : "))
    print("ความเร็วปลายที่ใช้  (V): ", (s / t), "m/s")
    return exit_programe(un)

def math_cal (un): #ส่วนโปรแกรมคำนวณเลข
    print("\nโปรแกรมตำนวณเลข")
    num_1 = int(input("จำนวนที่ 1 : "))
    num_2 = int(input("จำนวนที่ 2 : "))

    print("ผลลัพธ์การคำนวณโปรแกรมทั้ง 4 แบบ\n")

    print(num_1, "+", num_2, "=", (num_1 + num_2))
    print(num_1, "-", num_2, "=", (num_1 - num_2))
    print(num_1, "*", num_2, "=", (num_1 * num_2))
    print(num_1, "/", num_2, "=", int((num_1 / num_2)))

    return exit_programe(un)


def consult (un): #ส่วนโปรแกรมสอบความคิดเห็น
    new_job = input("\nโปรแกรมที่ต้องการให้เราพัฒนา : ")
    print("ขอบคุณสำหรับข้อเสนอแนะสำหรับโปรแกรมที่ท่าน เสนอมา", new_job)
    print("ทางเราจะขอนำความคคิดเห็นในครั้งนี้ไปพิจารณาอีกครั้งครับ ")
    print("ขอบคุณครับ")
    return exit_programe(un)

print(title_menu())