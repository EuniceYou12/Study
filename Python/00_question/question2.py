### **문제: 은행 관리 프로그램**

# 1. `Account` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행 계좌의 소유주 이름과 초기 잔액을 설정합니다.
#     - `deposit` 메서드를 사용하여 입금을 처리합니다.
#     - `withdraw` 메서드를 사용하여 출금을 처리합니다. 출금할 금액이 잔액보다 크면 출금을 허용하지 않습니다.
#     - `display_balance` 메서드를 사용하여 현재 잔액을 출력합니다.
# 2. `Bank` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행의 이름을 설정합니다.
#     - `create_account` 메서드를 사용하여 새로운 계좌를 생성합니다.
#     - `get_account` 메서드를 사용하여 계좌를 반환합니다.
#     - `display_accounts` 메서드를 사용하여 현재 은행에 있는 모든 계좌 정보를 출력합니다.
# 3. 사용자가 여러 번 계좌를 생성하고 입금, 출금, 잔액 조회 등의 작업을 수행할 수 있도록 하세요. 
# 사용자가 프로그램을 종료하고 싶을 때에는 "종료"를 입력하면 됩니다.

#1. Account 클래스 정의
#Account 클래스는 계좌 소유주와 잔액을 관리합니다. 이 클래스에는 입금, 출금, 잔액 조회 메소드가 포함되어야 합니다.
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다. 현재 잔액: {self.balance}원")
        else:
            print("입금 금액은 0보다 커야 합니다.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다. 현재 잔액: {self.balance}원")
        else:
            print("잔액이 부족하거나 잘못된 출금 금액입니다.")

    def display_balance(self):
        print(f"{self.owner}님의 현재 잔액은 {self.balance}원입니다.")

# 2. Bank 클래스 정의
# Bank 클래스는 여러 계좌를 관리합니다. 이 클래스에는 계좌 생성, 계좌 검색, 모든 계좌 정보 출력 메소드가 포함되어야 합니다.

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, owner, initial_balance=0):
        if owner in self.accounts:
            print(f"{owner}님은 이미 계좌를 가지고 있습니다.")
        else:
            new_account = Account(owner, initial_balance)
            self.accounts[owner] = new_account
            print(f"{owner}님의 계좌가 생성되었습니다.")

    def get_account(self, owner):
        return self.accounts.get(owner, None)

    def display_accounts(self):
        if not self.accounts:
            print("현재 은행에 계좌가 없습니다.")
        else:
            print(f"{self.name} 은행의 계좌 목록:")
            for owner, account in self.accounts.items():
                print(f"{owner}: {account.balance}원")

# 3. 사용자 인터페이스
# 사용자가 여러 번 계좌를 생성하고 입금, 출금, 잔액 조회 등의 작업을 수행할 수 있도록 하는 코드를 작성합니다. 
# 사용자가 "종료"를 입력하면 프로그램이 종료됩니다.

def main():
    bank = Bank("OpenAI Bank")
    while True:
        print("\n--- 은행 관리 프로그램 ---")
        print("1. 계좌 생성")
        print("2. 입금")
        print("3. 출금")
        print("4. 잔액 조회")
        print("5. 모든 계좌 정보 보기")
        print("6. 종료")
        choice = input("원하는 작업의 번호를 입력하세요: ")

        if choice == "1":
            owner = input("소유주 이름을 입력하세요: ")
            initial_balance = int(input("초기 잔액을 입력하세요: "))
            bank.create_account(owner, initial_balance)
        elif choice == "2":
            owner = input("소유주 이름을 입력하세요: ")
            amount = int(input("입금할 금액을 입력하세요: "))
            account = bank.get_account(owner)
            if account:
                account.deposit(amount)
            else:
                print("계좌를 찾을 수 없습니다.")
        elif choice == "3":
            owner = input("소유주 이름을 입력하세요: ")
            amount = int(input("출금할 금액을 입력하세요: "))
            account = bank.get_account(owner)
            if account:
                account.withdraw(amount)
            else:
                print("계좌를 찾을 수 없습니다.")
        elif choice == "4":
            owner = input("소유주 이름을 입력하세요: ")
            account = bank.get_account(owner)
            if account:
                account.display_balance()
            else:
                print("계좌를 찾을 수 없습니다.")
        elif choice == "5":
            bank.display_accounts()
        elif choice == "6":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()



# 선생님 답안

# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"{amount}원이 입금되었습니다.")
#         else:
#             print("입금액은 0보다 커야 합니다.")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"{amount}원이 출금되었습니다.")
#         else:
#             print("잔액이 부족합니다.")

#     def display_balance(self):
#         print(f"{self.owner}님의 현재 잔액은 {self.balance}원 입니다.")

# class Bank:
#     def __init__(self, name):
#         self.name = name
#         self.accounts = []

#     def create_account(self, owner, balance=0):
#         account = Account(owner, balance)
#         self.accounts.append(account)
#         print(f"{owner}님의 계좌가 생성되었습니다.")

#     def get_account(self, owner):
#         for account in self.accounts:
#             if account.owner == owner:
#                 return account
#         print(f"{owner}님의 계좌를 찾을 수 없습니다.")

#     def display_accounts(self):
#         print(f"{self.name}의 모든 계좌 정보:")
#         for account in self.accounts:
#             print(f"소유주: {account.owner}, 잔액: {account.balance}원")

# # 은행 생성
# bank = Bank("MyBank")

# # 메인 프로그램
# while True:
#     print("\n1. 계좌 생성")
#     print("2. 입금")
#     print("3. 출금")
#     print("4. 잔액 조회")
#     print("5. 은행 계좌 목록")
#     print("종료")

#     choice = input("원하는 작업을 선택하세요: ")

#     if choice == "종료":
#         print("프로그램을 종료합니다.")
#         break
#     elif choice == "1":
#         owner = input("소유주 이름을 입력하세요: ")
#         bank.create_account(owner)
#     elif choice == "2":
#         owner = input("소유주 이름을 입력하세요: ")
#         account = bank.get_account(owner)
#         if account:
#             amount = int(input("입금할 금액을 입력하세요: "))
#             account.deposit(amount)
#     elif choice == "3":
#         owner = input("소유주 이름을 입력하세요: ")
#         account = bank.get_account(owner)
#         if account:
#             amount = int(input("출금할 금액을 입력하세요: "))
#             account.withdraw(amount)
#     elif choice == "4":
#         owner = input("소유주 이름을 입력하세요: ")
#         account = bank.get_account(owner)
#         if account:
#             account.display_balance()
#     elif choice == "5":
#         bank.display_accounts()
