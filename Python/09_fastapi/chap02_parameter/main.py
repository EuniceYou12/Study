from fastapi import FastAPI

app = FastAPI()

# 경로 매개변수
# URL 경로에 들어가는 매개변수

# @app.get("/users/{user_id}")
# def get_user(user_id):
#   return {"user_id" : user_id}


# 파이썬은 원래 타입 없음. 그런데 fast api 통해서 타입 줄 수 있음.
# 타입을 정의하려면?
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#   return {"user_id" : user_id}


# 경로의 순서 문제 이해
# 인터프리터 언어는 순서가 중요해서
# 아래와 같이 endpoint를 줘도 위의 endpoint가 먼저 작용하므로 /users/aaa 는 에러가 남.
# @app.get("/users/aaa")
# def get_current_user():
#   return {"user_id":123}


# query string parameter 를 fastapi로 받음.
# 쿼리 매개변수
# 호스트 주소/path? 뒤에 오는 변수들을 쿼리 매개변수 라고 한다.
# 각 매개변수는 & 기호로 구분되고, key=value 쌍으로 정의된다.
# @app.get("/users")
# def get_users(limit: int, name: str):
#   return {"limit":limit, "name":name}


# http://127.0.0.1:8000/users?limit=123&name=aaaa
# Swagger => localhost:8000/docs


@app.get("/users")
def get_users(limit:int = 100): # 기본값 지정
  return {"limit":limit}
  
# 포트번호 바꾸는 명령어
# uvicorn main:app --port 8080 --reload