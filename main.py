import datetime

# 버거류 : "이름",가격, 소분류,

menu = {
    "1": {"burger": {  # 21~
        "21": ["더블쿼터파운더치즈", 6000, "beef"],
        "22": ["쿼터파운더치즈", 5000, "beef"],
        "23": ["불고기", 3000, "beef"],
        "24": ["더블불고기", 3500, "beef"],
        "25": ["빅맥", 4500, "beef"],
        "26": ["치즈", 3000, "beef"],
        "27": ["베이컨토마토디럭스", 5000, "beef"],
        "28": ["햄버거", 2500, "beef"],
        "29": ["맥스파이상하이", 5500, "chicken"],
        "30": ["맥치킨", 4500, "chicken", 0, 0, 1],
        "31": ["맥크리스피디럭스", 6000, "chicken"]
    }},
    "2": {"mac_lunch": {  # 101~  # 세트에서 변동불가
        "101": ["빅맥세트", 5500],
        "102": ["더블불고기세트", 4500],
        "103": ["베이컨토마토디럭스세트", 6000]
    }},
    "3": {"mac_morning": {  # 151~
        "151": ["에그맥머핀", 2800],
        "152": ["소시지에그맥머핀", 3000],
        "153": ["베이컨에그맥머핀", 3300],
        "154": ["치킨맥머핀", 3000]
    }},
    "4": {"happy_snack": {  # 251~
        "251": ["드립커피M", 1000],
        "252": ["제로콜라M", 1000],
        "253": ["치즈버거", 2000],
        "254": ["치즈스틱2조각", 2000],
        "255": ["후렌치후라이S", 1000]
    }},
    "5": {"side": {  # 201~
        "201": ["맥윙2조각", 2000],
        "202": ["맥윙4조각", 3500],
        "203": ["맥윙8조각", 6000],
        "204": ["치즈스틱2조각", 2000],
        "205": ["치즈스틱4조각", 3800],
        "206": ["후렌치후라이S", 1000],
        "207": ["후렌치후라이M", 1500],
        "208": ["후렌치후라이L", 1500],
        "209": ["맥너겟4조각", 2000],
        "210": ["맥너겟6조각", 2800]
    }},
    "6": {"dessert": {  # 301~
        "301": ["맥플러리", 3000, 1, 0, 0],
        "302": ["아이스크림콘", 1000, 1, 0, 0]
    }},
    "7": {"mac_cafe": {  # 351~
        "351": ["카페라떼", 2000],
        "352": ["아이스카페라떼", 2000],
        "353": ["드립커피", 1000],
        "354": ["아이스드립커피", 1000]
    }},
    "8": {"drink": {  # 401~
        "401": ["콜라M", 1000],
        "402": ["콜라L", 1500],
        "403": ["콜라제로M", 1000],
        "404": ["콜라제로L", 1500],
        "405": ["사이다M", 1000],
        "406": ["사이다L", 1500],
        "407": ["오렌지주스", 1000],
        "408": ["생수", 1000]
    }},
    "9": {"happy_meal1": {  # 501~ #오전
        "501": ["에그맥머핀", 4000],
        "502": ["소시지에그맥머핀", 4200],
        "503": ["베이컨에그맥머핀", 4500],
        # 551~ #오후
        "551": ["치즈버거", 4200],
        "552": ["햄버거", 3800],
        "553": ["불고기버거", 4200],
    }}
}

basket = []

dining_option = None

reset_system = 0


# 시간에 따른 카테고리 출력
def current_category():  # 현재 지정된 카테고리
    category = {
        "1": "버거",
        "2": "맥런치",
        "3": "맥모닝",
        "4": "해피스낵",
        "5": "사이드",
        "6": "디저트",
        "7": "맥카페",
        "8": "음료",
        "9": "해피밀",
        "0": "처음으로"
    }
    now = datetime.datetime.now()
    nowtime = now.hour * 60 + now.minute

    if not basket:
        if 240 <= nowtime < 630:  # 새벽 4시 ~ 오전 10시 30분
            del category["2"]  # 맥런치 제외
        elif 630 <= nowtime < 840:  # 오전 10시 30분 ~ 오후 2시
            del category["3"]  # 맥모닝 제외
        else:  # 그 외 시간
            del category["2"]  # 맥런치 제외
            del category["3"]  # 맥모닝 제외
    else:  # 장바구니에 품목있으면 주문하기 활성화
        if 240 <= nowtime < 630:  # 새벽 4시 ~ 오전 10시 30분
            del category["2"]  # 맥런치 제외
            category["10"] = "내역확인 후 주문하기"
        elif 630 <= nowtime < 840:  # 오전 10시 30분 ~ 오후 2시
            del category["3"]  # 맥모닝 제외
            category["10"] = "내역확인 후 주문하기"
        else:
            del category["2"]  # 맥런치 제외
            del category["3"]  # 맥모닝 제외
            category["10"] = "내역확인 후 주문하기"

    return category


# 카테고리 출력
def display_category(category):
    print("====카테고리====")
    for key, value in category.items():
        print(f"{key}. {value}")

def display_burger_menu(burger_menu, sort_burger):
    print(f"=== {sort_burger} 버거===")
    for menu_item_num,(menu_item_name, menu_item_type) in burger_menu.items():
        if sort_burger == "전체" or menu_item_type == sort_burger:
            print(f"{menu_item_num}. {menu_item_name}")

while True:  # w1
    print("1. 주문하기")
    w1_choice = input("입력:")
    if w1_choice == "1":
        reset_system = 0
        while reset_system != 1:  # 포장, 매장, 처음
            print("1. 포장하기, 2. 매장식사, 0. 처음으로")
            dining_choice = input("입력:")

            if dining_choice == "1":
                dining_option = "포장"
            elif dining_choice == "2":
                dining_option = "매장식사"
            else:
                break

            while reset_system != 1:  # 카테고리 출력
                now_category = current_category()
                display_category(now_category)
                category_choice = input("카테고리 입력:")

                # 카테고리의 메뉴 출력
                if category_choice == "1" and category_choice in now_category:
                    burger_menu = menu["1"]["burger"]
                    print("=버거 소분류=")
                    print("1. 전체 2. 비프버거 3. 치킨버거")
                    sort_burger_choice = input("버거 소분류 선택:")
                    sort_burger_category = {"1":"전체","2":"beef","3":"chicken"}
                    sort_burger = sort_burger_category.get(sort_burger_choice, "전체")
                    display_burger_menu(burger_menu, sort_burger)

                elif category_choice == "0":
                    reset_system = 1
                    break
                else:
                    print("잘못된 카테고리")
                    continue
