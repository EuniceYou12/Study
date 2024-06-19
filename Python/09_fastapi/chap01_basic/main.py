
# fastAPI
# python 으로 작성된 API 를 만들기 위한 웹 프레임워크

# 장점
# 1. 고성능 = 아주 빠른 성능을 제공하며, 기존의 flask 같은 웹
# 프레임워크 보다 2배가량 빠르다.
# 2. 쉬운 사용 = 작성하기 쉬운 코드 방식을 가지고 있다.
# 3. 자동 문서화 = swagger 문서 지원
# 4. 비동기 지원 = 비동기 기능을 지원하여 비동기 작업을 쉽게 처리할 수 있다.

from fastapi import FastAPI

app = FastAPI()


@app.get("/") # GET 요청 받는 endpoint
def read_root():
  return {"hello":"world"}

# main.py 에서만 실행시키겠다. "name = 실행되는 파일의 이름"
# FastAPI를 main에서만 띄울 수 있게 막아주는 용도 
# main 모듈을 import 못하게 main을 다른 곳에서 임포트하면 실행되지 않게
# 가장 윗 상단이니까 다른 곳에서 import 되어서 잘못 실행되는 걸 막기 위함.
if __name__ == "__main__":
  uvicorn.run("main:app", reload=True)

# __name__ 변수
# python 에서는 각 파일이 실행 될 때마다 특별한 변수인 __name__ 을 갖는다.
# 스크립트가 실행될 때, __name__ 변수는 "__main__" 으로 설정된다.
# 스크립트가 다른 모듈에 임포트될 때 __name__ 변수는 해당 모듈의 이름으로 바뀐다.

# uvicorn main:app --reload

# main = main.py 파일을 의미
# app = main.py 에서 FastAPI() 객체를 식별하는 app 객체를 의미
# --reload = 파일에 변화가 생기면 재시작하겠다는 옵션

