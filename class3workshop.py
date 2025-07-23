import random
Boss_Saran_health = random.randint(1,50)
Bow_damage = 3
Sword_damage = 7
Mace_damage = 15
win = False
while True:
    choice = int(input("กด 1 เพื่อเข้าตี กด 2 เพื่อออก : "))
    if choice == 1:
        round = int(input("จะตีกี่รอบดี : "))
        print(f"บอสสรันปรากฏตัว อร๊ากกกก!! เลือดบอสสรัน = {Boss_Saran_health} หน่วย")
        for i in range(round):
            print("----------------------------------------------------------------")
            print(f"ตอนนี้เหลือ {round - (i)} รอบ")
            print(f"เลือดบอสสรันเหลือ {Boss_Saran_health} หน่วย")
            weapon = int(input("""
                ใส่เลขเลือกอาวุธที่ใช้โจมตี 
                1 .ธนูในตำนาน ดาเมจ 3 หน่วย
                2 .โครตอภิมหาดาบไลท์เซเบอร์ ดาเมจ 7 หน่วย
                3 .ลูกตุ้มขุมนรก ดาเมจ 15 หน่วย
                               """))
            if weapon == 1:
                Boss_Saran_health -= Bow_damage
            elif weapon == 2:
                Boss_Saran_health -= Sword_damage
            elif weapon == 3:
                Boss_Saran_health -= Mace_damage
            
            if Boss_Saran_health == 0:
                print("ยินดีด้วยคุณกำจัดบอสสรันลงแล้ว")
                win = True
            if Boss_Saran_health < 0:
                print("เจ้ามนุษย์หน้าโง่ ข้ายังไม่ตาย")
                Boss_Saran_health = 20
        if not win:
            print("มันจบแล้วเจ้ามนุษย์ตายซะ")
    if choice == 2:
        print("เจ้าขี้ขลาด!!")
        break

