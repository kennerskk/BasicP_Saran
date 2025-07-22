distance = int(input("ระยะทางเท่าไหร่"))

if (distance > 5):
    if(distance > 500):
        print("ค่าส่ง",45,"บาทครับ")
    elif(distance > 300):
        print("ค่าส่ง",35,"บาทครับ")
    elif(distance > 100):
        print("ค่าส่ง",25,"บาทครับ")
    elif(distance > 50):
        print("ค่าส่ง",15,"บาทครับ")
    elif(distance > 5):
        print("ค่าส่ง",10,"บาทครับ")

else:
    print("ไม่ส่งโว้ย")