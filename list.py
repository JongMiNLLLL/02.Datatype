jongmin = ["이종민", '20', '010-2680-****']
name = jongmin[0]
age = jongmin[1]
phone = jongmin[2]

print(type(jongmin))
print(name, age, phone)
print(jongmin[0])
print(jongmin[0:3])

names = ['하니', '민지', '다니엘'], ['20', '20', '19'], ['010-****-****', '010-****-****', '010-****-****']
print(names[0][0:2])

numbers = [1,2,3,4,5]
result = numbers[2]+numbers[4]
print(result)

print(len(numbers))
print(len(names))


#리스트에 요소 추가 및 제거하기
last = [1,2,3]
last.append(30)
print(last)
last.remove(3)
print(last)
