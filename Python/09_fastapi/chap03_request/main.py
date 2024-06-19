
# 요청 응답

# POST, PUT, PATCH 등의 메소드를 사용하는 경우 HTTP 본문(body) 사용

# 단순 텍스트나 json 을 이용한다.

# pydantic 으로 요청 본문 받기
# 데이터 유효성 검사 및 설정 관리를 위한 라이브러리

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# BaseModel
# optional = 선택사항 이라 받아도 되고 안받아도 됨. HttpUrl 형식이어야 하고 기본값은 None 이다.
# body에 받는 내용..?
class UserInfo(BaseModel):
  name : str
  password : str
        # url 은 선택사항이며, URL 형식으로 받아야 한다. 기본값은 None 이다.
  url : Optional[HttpUrl] = None
# UserInfo 클래스(BaseModel 을 상속 받음)
# BaseModel 을 상속 받아야 request body 부분을 받을 클래스로 이용할 수 있음


# user:UserInfo  body에 받는 내용 =>user 라는 객체는 UserInfo 라는 타입임.
@app.post("/users")
def createUser(user:UserInfo):
  return user

