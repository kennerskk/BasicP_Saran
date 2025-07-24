# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    print("--------------------------------------")
    x = 1
    for i in movie_list:
        print (f"{x} {i["movie_name"]} tiket price : {i["ticket_price"]} Bath")
        x +=1

# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(age,select,movies):
    if age>=int(movies[select-1]["age_restriction"]):
        return True
    elif movies[select-1]["age_restriction"] == "G":
        return True
    else:
        return False

# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    if genre == "Sci-Fi":
        base_price += 50
        return base_price
    else:
        return base_price
    # ถ้าไม่ใช่ คืนราคาเดิม

# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movies):
    show_movies(movies)
    select = int(input("what movie?"))
    age = int(input("input ur age"))
    if check_age(age,select,movies):
            basicprice = movies[select-1]["ticket_price"]
            name = movies[select-1]["movie_name"]
            totalprice = calculate_price(basicprice,movies[select-1]["genre"])
            sub = int(input("1.subthai 2.thaidub"))
            tribe = ""
            if sub == 1:
                tribe = "subthai"
            elif sub == 2:
                tribe = "thaidub"
            print(f"""
    ยืนยันการซื้อ
    ดูเรื่อง {name}
    ชนิด {tribe}
    ราคา {totalprice}
    
""")
    else:
                print("อายุไม่ผ่านเกณฑ์")
def main():
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]
    while True:
        choice = int(input("1) for show movie name 2) for buy ticket"))
        if choice == 1:
            show_movies(movies)
        if choice == 2:
             buy_ticket(movies)          
main()
