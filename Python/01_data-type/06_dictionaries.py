
# Dictionaries

# 키와 값의 깡으로 구성된 데이터 구조로, 키를 통해 값을 찾을 수 있으므로 매우 빠른 조회 성능을 보여준다.
# 키는 중복 불가 

teacher = {'name' : 'pig', 'team' : 'ohgiraffers'}

print(type(teacher))
print(teacher['name'])


# 생성 후 키 값 쌍 추가 / 수정 / 삭제
teacher['age'] = 20
print(teacher['age'])


# in 키워드 : 키값의 존재 여부를 확인 할 수 있다. 
print('name' in teacher)


# 1. get()
# 매개변수로 전달 받은 key에 해당하는 값을 반환한다.
print(teacher.get('name'))

# 2. keys()
print(teacher.keys())

# 3. values()
print(teacher.values())

# 4. items()
print(teacher.items())
print(teacher)

# 5. pop(키)
print(teacher.pop('age'))
print(teacher)

# 6. clear()
teacher.clear()
print(teacher)


