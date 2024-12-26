class ATM:
    # ATM 생성자 / ATM 시작 잔고 설정, 기본적으로 미작동상태(사용자가 시작해야 작동함)
    def __init__(self, atm_bal):
        self.atm_balance = atm_bal
        self.atm_status = False
        self.now_account = None

    # ATM기기의 현재 상태 리턴 True/False
    def check_status(self):
        return self.atm_status

    # 통장을 받음
    def get_account(self, account):
        if self.check_status():
            self.now_account = account
            bank.check_account(self.now_account)

    # bank_DB 데이터 받기
    def get_bank_DB(self):
        return bank.bank_DB

    # 잔고조회
    def view_balance(self):
        db = self.get_bank_DB()
        print(f"{self.now_account.name}님의 현재 잔고 : {db[self.now_account.name]["Balance"]}원")

    # 입금 절차 실행
    def run_deposit(self, money):
        # 금액이 0이거나 마이너스 인경우 진행 X
        if money <= 0:
            print("금액을 확인해주세요.")

        else:
            # ATM 잔고를 증가시키고 Bank_DB에 데이터 저장
            self.atm_balance += money
            bank.get_changed_balance(self.now_account,money)

            print(f"{money}원이 입금되었습니다.")
            # 현재 계좌의 잔고 출력
            self.view_balance()
    
    # 출금 절차 실행
    def run_withdraw(self, money):
        # 금액이 0이거나 마이너스 인경우 진행 X
        if money <= 0:
            print("금액을 확인해주세요.")

        else:
            # bank_DB에 현재 계좌의 잔고를 확인하여 진행
            if bank.check_balance(self.now_account,money):

                # ATM 잔고를 감소시키고 Bank_DB에 데이터 저장
                self.atm_balance -= money
                bank.get_changed_balance(self.now_account, -money)

                print(f"{money}원이 출금되었습니다.")
                # 현재 계좌의 잔고 출력
                self.view_balance()
            else:
                print("잔고가 부족합니다!")


class Bank:
    # Bank 생성자 // 정보 저장을 위한 필드 생성
    def __init__(self):
        self.bank_DB = {}  # 딕셔너리 형태로 정보를 저장

    # Bank DB에 정보 추가 // 동명이인 고려 X -> 이름을 키값으로(간단하게), 계좌번호와 잔고를 저장
    def add_account(self, account):
        self.bank_DB[account.name] = {"ID": account.id, "Balance":account.balance}

    # ATM이 받은 통장이 Bank_DB에 있는지 체크
    def check_account(self, account):
        if account.name in self.bank_DB:
            print("통장이 확인되었습니다.")
        else:
            print("존재하지 않는 통장입니다.")

    # 요청받은 계좌의 잔고 체크 후 논리값 리턴
    def check_balance(self, account, money):
        balance = self.bank_DB[account.name]["Balance"]
        if balance >= money:
            return True
        else:
            return False


    # 변동된 데이터를 받아와 저장
    # 금액 변동사항 처리 기능
    def get_changed_balance(self,account,money):
        self.bank_DB[account.name]["Balance"] += money


class User:
    # User 생성자 // 이름을 매개변수로 받아 저장
    def __init__(self, name):
        self.name = name

    # 통장 보기
    def view_account(self, account):
        account.display_account()

    # ATM 기기 사용 시작
    def atm_start(self):
        print("ATM기기 사용 시작")
        atm.atm_status = True
        print("통장을 넣어주세요.")

    # ATM 기기 사용 종료
    def atm_end(self):
        print("ATM기기 사용 종료")
        atm.atm_status = False

    # 통장 넣음
    def atm_input(self, account):
        atm.get_account(account)

    # ATM 입금
    def atm_deposit(self, money):
        atm.run_deposit(money)

    # ATM 출금
    def atm_withdraw(self, money):
        atm.run_withdraw(money)

class Account:
    # Account 생성자 // 계좌번호, 이름, 잔고 를 입력받아 계좌생성
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance
        print(f"{self.name}님의 계좌가 생성되었습니다.")

    # 통장내용 출력 기능
    def display_account(self):
        print(f"예금주 : {self.name}")
        print(f"계좌번호 : {self.id}")
        print(f"잔고 : {self.balance}원")


atm = ATM(0)
user = User("YSJ")
ysj_account = Account("123-1233-31", "YSJ", 0)
bank = Bank()
bank.add_account(ysj_account)

# print(bank.user_info)

user.view_account(ysj_account)
user.atm_start()
user.atm_input(ysj_account)

user.atm_deposit(10000)
user.atm_withdraw(5000)