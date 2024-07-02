#Quiz 1
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
email = input("이메일 주소를 입력하세요: ")
phone = input("연락처를 입력하세요: ")

dic = {name : [age,email,phone]}

print(dic)

name_2 = input("이름을 입력하세요: ")
age_2 = input("나이를 입력하세요: ")
email_2 = input("이메일 주소를 입력하세요: ")
phone_2 = input("연락처를 입력하세요: ")

dic_2 = {name_2 : [age_2,email_2,phone_2]}

print(dic_2)

#Quiz 2
exchange = {"달러": 1320, "엔": 950, "위안": 182}
money = [13, 200, 13]

total = exchange['달러'] * money[0] + exchange['엔'] * money[1] + exchange['위안'] * money[2]
print('가지고 계신 돈은' , total,   '원 입니다.')
