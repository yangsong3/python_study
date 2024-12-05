import datetime

# 현재 시간 계산
now = datetime.datetime.now()
nowtime = now.hour * 60 + now.minute

# 메뉴 데이터
menu = {
    "1": {"burger": {
        "21": ["더블쿼터파운더치즈", 6000, "비프버거"],
        "22": ["쿼터파운더치즈", 5000, "비프버거"],
        "23": ["불고기", 3000, "비프버거"],
        "24": ["더블불고기", 3500, "비프버거"],
        "25": ["빅맥", 4500, "비프버거"],
        "26": ["치즈", 3000, "비프버거"],
        "27": ["베이컨토마토디럭스", 5000, "비프버거"],
        "28": ["햄버거", 2500, "비프버거"],
        "29": ["맥스파이상하이", 5500, "치킨버거"],
        "30": ["맥치킨", 4500, "치킨버거"],
        "31": ["맥크리스피디럭스", 6000, "치킨버거"]
    }},
    "2": {"mac_lunch": {
        "101": ["빅맥세트", 5500],
        "102": ["더블불고기세트", 4500],
        "103": ["베이컨토마토디럭스세트", 6000]
    }}
}

# 장바구니 데이터
cart = []

# 다이닝 옵션
dining_option = None

# 시간 조건에 따른 카테고리 필터링
def get_available_categories(nowtime):
    categories = {
        "1": "버거",
        "2": "맥런치",
        "0": "처음으로"
    }
    if 240 <= nowtime < 630:  # 새벽 4시 ~ 오전 10시 30분
        del categories["2"]  # 맥런치 제외
    elif 630 <= nowtime < 840:  # 오전 10시 30분 ~ 오후 2시
        pass  # 맥모닝 제외 없음
    else:
        del categories["2"]  # 맥런치 제외
    return categories

# 카테고리 출력
def display_categories(categories):
    print("\n=== 카테고리 ===")
    for key, value in categories.items():
        print(f"{key}. {value}")
    print("================")

# 버거 메뉴 출력 (소분류 적용)
def display_burger_menu(burger_menu, subcategory):
    print(f"\n=== 버거 메뉴 ({subcategory}) ===")
    for item_num, (item_name, item_price, item_type) in burger_menu.items():
        if subcategory == "전체" or item_type == subcategory:
            print(f"{item_num}. {item_name} - {item_price}원 ({item_type})")
    print("================")

# 장바구니 출력
def view_cart():
    if not cart:
        print("\n장바구니가 비어 있습니다.")
        return
    print("\n=== 장바구니 ===")
    total_price = 0
    for item in cart:
        print(f"{item['name']} - {item['price']}원")
        total_price += item['price']
    print(f"총 금액: {total_price}원")
    print("=================")

# 메인 프로그램
def main():
    global dining_option
    print("맥도날드 키오스크에 오신 것을 환영합니다!")
    while True:
        print("\n1. 시작하기")
        print("2. 종료하기")
        choice = input("선택: ")

        if choice == "1":
            # 다이닝 옵션 선택
            print("\n=== 다이닝 옵션 ===")
            print("1. 포장하기")
            print("2. 매장식사")
            dining_choice = input("선택: ")
            dining_option = "포장" if dining_choice == "1" else "매장식사"

            # 메인 카테고리 출력
            while True:
                available_categories = get_available_categories(nowtime)
                display_categories(available_categories)
                category_choice = input("카테고리 번호를 선택하세요: ")

                if category_choice in available_categories and category_choice == "1":
                    # 버거 메뉴 출력 (소분류 선택)
                    burger_menu = menu["1"]["burger"]
                    print("\n=== 버거 소분류 ===")
                    print("1. 전체")
                    print("2. 비프버거만")
                    print("3. 치킨버거만")
                    subcategory_choice = input("소분류를 선택하세요: ")
                    subcategory_map = {"1": "전체", "2": "비프버거", "3": "치킨버거"}
                    subcategory = subcategory_map.get(subcategory_choice, "전체")
                    display_burger_menu(burger_menu, subcategory)

                    # 메뉴 선택
                    item_choice = input("메뉴 번호를 선택하세요: ")
                    if item_choice in burger_menu:
                        item_name, item_price, _ = burger_menu[item_choice]
                        print(f"{item_name}을 선택하셨습니다.")
                        cart.append({"name": item_name, "price": item_price})
                        view_cart()
                    else:
                        print("잘못된 선택입니다. 다시 시도하세요.")

                elif category_choice == "0":
                    print("처음 화면으로 돌아갑니다.")
                    break
                else:
                    print("잘못된 선택입니다. 다시 시도하세요.")

        elif choice == "2":
            print("키오스크를 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()
