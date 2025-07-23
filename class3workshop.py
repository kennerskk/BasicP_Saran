import random # นำเข้าไลบราลี่สำหรับสุ่ม
Boss_Saran_health = random.randint(1,50) # สุ่มเลข
First_Boss_Saran_health = Boss_Saran_health # กำหนดเลือดเริ่มต้นสำหรับแสดงตอนจบ
Bow_damage = random.randint(3,7) # กำหนดดาเมจ
Sword_damage = random.randint(5,11)
Mace_damage = random.randint(3,7)
win = False # กำหนดตัวแปรสำหรับตรวจสอบว่าชนะหรือไม่
while True: # อินฟินิตี้ลูปสำหรับรันเกม
    choice = int(input("กด 1 เพื่อเข้าตี กด 2 เพื่อออก : ")) # รับออปชั่นของเพลเยอ
    if choice == 1: # ถ้าเลือกตี
        round = int(input("จะตีกี่รอบดี : ")) # รับว่าจะตีกี่รอบดี
        print(f"บอสสรันปรากฏตัว อร๊ากกกก!! เลือดบอสสรัน = {Boss_Saran_health} หน่วย") # แสดงเลือดเริ่มต้นของ บอสสรัน
        for i in range(round): # ลูปตามจำนวนรอบที่ต้องการเข้าตี
            print("----------------------------------------------------------------")
            print(f"ตอนนี้เหลือ {round - (i)} รอบ")# บอกว่าเหลือกี่รอบ
            print(f"เลือดบอสสรันเหลือ {Boss_Saran_health} หน่วย") # บอกว่าเหลือเลือดเท่าไหร่
            weapon = int(input(f"""
                ใส่เลขเลือกอาวุธที่ใช้โจมตี 
                1 .ธนูในตำนาน ดาเมจ {Bow_damage} หน่วย
                2 .โครตอภิมหาดาบไลท์เซเบอร์ ดาเมจ {Sword_damage} หน่วย
                3 .ลูกตุ้มขุมนรก ดาเมจ {Mace_damage} หน่วย
                เลือกอะไร : """)) # รับอินพุตว่าอยากใช้อาวุธอะไร
            if weapon == 1: # ลบเลือด
                Boss_Saran_health -= Bow_damage
            elif weapon == 2:
                Boss_Saran_health -= Sword_damage
            elif weapon == 3:
                Boss_Saran_health -= Mace_damage
            
            if Boss_Saran_health == 0: # ถ้าเลือดบอสสรันหมด break กำหนด win เป็น false
                print(f"ยินดีด้วยคุณกำจัดบอสสรันเลือดเริ่มต้นที่ {First_Boss_Saran_health} ลงแล้ว ภายใน ",(i+1),"รอบ")
                win = True
                break
            if Boss_Saran_health < 0: # ถ้าบอสสรันเลือดลดต่ำกว่า 0 
                print("เจ้ามนุษย์หน้าโง่ ข้ายังไม่ตาย")
                Boss_Saran_health = 20 # เลือดเด้งกลับมา 20
        if not win: # เมื่อหลุดออกจากลูปก็เช็คต่อว่าชนะไหม ถ้าไม่ก็แสดงผลว่า แพ้
            print("มันจบแล้วเจ้ามนุษย์ตายซะ")
    if choice == 2: # ถ้าผู้เล่นเลือกไม่ตี
        print("เจ้าขี้ขลาด!!")
        break # จบลูปนอกสุดหยุดการทำงานของโค้ด

