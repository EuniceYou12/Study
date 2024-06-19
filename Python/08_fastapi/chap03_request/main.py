

# 요청 응답

# POST, PUT, PATCH 등의 메소드를 사용하는 경우 HTTP 본문(body) 사용

# 단순 텍스트나 json 을 이용한다.

# pydantic 으로 요청 본문 받기
# 데이터 유효성 검사 및 설정 관리를 위한 라이브러리

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class UserInfo(BaseModel):
    name : str
    password : str
    url : Optional[HttpUrl] = None

# Optional 은 선택이고 HttpUrl 은 형식이고 None 은 기본값
# Url은 선택사항이며, URL 형식으로 받아야한다.

@app.post("/users")
def createUser(user:UserInfo):
    return user 

# Post 요청에는 body에 담겨 오는데 UserInfo 클래스 (BaseModel 을 상속 받음)
# BaseModel 을 상속 받아야 request body 부분을 받을 클래스로 이용할 수 있음
# /User post 요청에 담겨온 body 부분을 userInfo 자료형에 담아 user 라는 객체를 생성한다.