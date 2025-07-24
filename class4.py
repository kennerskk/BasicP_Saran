# def grade(score):
#     if score >= 80:
#         print("a")
#     elif score >= 70:
#         print("b")
#     elif score >= 60:
#         print("c")
#     elif score >= 50:
#         print("d")
#     else:
#         print("f")
# def add(x,y):
#     return x+y
# x = add(7,3)
# print(x)

def calculate(amount,price):
    result = (amount*price)*1.07
    return result
    

def Menu():
    while True:
        choice = int(input("1เพื่อคำนวน 2เพื่ออก : "))

        if choice == 1:
            amount = float(input("ใส่จำนวน : "))
            price = float(input("ใส่ราคา : "))
            print(f"ราคารวม vat เท่ากับ{calculate(amount,price)} บาท")
        elif choice == 2:
            print("เลิกคำนวน")
            break

Menu()