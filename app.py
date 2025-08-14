from flask import Flask, jsonify, render_template, request, make_response
from routes.user import user_bp
from routes.admin import admin_bp

app = Flask(__name__)

@app.route("/") # 사용자로 부터 받아온 URL에 해당하는 함수를 매칭해주기 위해서 사용합니다.
def index():
  return render_template("index.html", name="웅비")

@app.route('/set')
def set_cookie():
  # 1. "쿠키 설정 완료" 라는 내용이 담길 응답(편집)을 먼저 만들기
  resp = make_response("쿠키 설정 완료")

  # 2. 작성한 응답(편집)에 'username' 이라는 이름의 쿠키(도장 카드!!)
  resp.set_cookie('username', 'Seo')
  return resp

@app.route('/get')
def get_cookie():
  # 사용자의 요청(편지)에 붙어있는 쿠키(도장 카드)를 확인합니다.
  username = request.cookies.get('username')
  return f'지갑에서 꺼낸 쿠키: {username}'

if __name__ == '__main__':
  app.run(debug=True)

# from flask.json.provider import DefaultJSONProvider
# from flask import Flask, request, url_for

# 직렬화가 불가능한 데이터 타입을 직렬화 시키는 코드
# from datetime import datetime, date, time
# from decimal import Decimal
# from uuid import UUID
# from pathlib import Path

# 한글깨짐 방지 코드
# class StrJson(DefaultJSONProvider):
#   def default(self, obj):
#     if isinstance(obj, (datetime, date, time)):
#       return obj.isoformat()

 #__main__
# app.register_blueprint(user_bp)
# app.register_blueprint(admin_bp)
# app.secret_key = "niceboat" # 직접 작성하지는 않고 난수 발생시키는 기능을 이용해서 만듬
# # app.json = StrJson(app)

# @app.route("/now")
# def hello():
#   return jsonify({"time": datetime.now()})

# @app.route('/error')
# def error_example():
#   error = {"error": "잘못된 요청 입니다."}
#   return jsonify(error), 400 # 에러 코드 대처하는 코드

# # 전체 라우트 확인 -> flask routes

# @app.route("/") # 사용자로 부터 받아온 URL에 해당하는 함수를 매칭해주기 위해서 사용된다.
# def index():
#   return "Hello, OZ"

# # /search?query=flask&sort=recent # args => ?query=flask&sort=recent
# @app.route("/search")
# def search():
#   keyword1 = request.args.get('query')
#   return f'검색어 : {keyword1}'

# # http://localhost:5000/tags?tag=python&tag=flask&tag=jinja
# @app.route('/tags')
# def tags():
#   keywords = request.args.getlist('tag')
#   return f'태그목록 : {keywords}'

# # http://localhost:5000/shop?keyword=커피머신&category=전자제품
# @app.route('/shop')
# def shop():
#   keyword = request.args.get('keyword')
#   category = request.args.get('category')
#   return f'제품이름 : {keyword}, 분류 : {category}'

# # http://localhost:5000/filter?filter=brand&filter=price&filter=rating
# # 출력 예시 -> 적용된 필터 : ['brand', 'price', 'rating']
# @app.route('/filter')
# def filter():
#   filters = request.args.getlist('filter')
#   return f'필터 목록 : {filters}'

# #/user/출력을 원하는 이름 (값 매칭 확인)
# @app.route('/user/<username>')
# def show_user_profile(username):
#   return f'안녕하세요, {username}님 !!'

# # 데이터 타입설정 ★ (Default : str) ★
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#   return f'포스트 번호: {post_id}'

# # "/"는 임의로 추가할 수 없음. -> "path:" 추가하면 가능  http://127.0.0.1:5000/files/images/profile.jpg
# @app.route('/files/<path:filename>')
# def show_file(filename):
#   return f'파일경로 : {filename}'

# # http://localhost:5000/files/documents/python/lesson1.txt
# # 출력 예시 : 접근한 파일 경로 : documents/python/lesson1.txt
# @app.route('/files/<path:subpath>')
# def txt_file(subpath):
#   return f'파일경로 : {subpath}'

# # def 함수이름(인자 : 타입) -> 반환타입 : 
# # 정수를 받아 제곱을 계산하는 항수
# @app.route('/square/<int:number>')
# def square(number : int) -> str :
#   result = number ** 2
#   return f'root of {result} is {number}'

# # 나이 계산 API 만들기
# # URL : /birthday/<int:age>
# # 현재 연도는 2025년으로 가정해서 로직 구현
# # 타입 힌트를 포함하여 birthday 함수를 만들어주세요
# @app.route('/birthday/<int:age>')
# def birthday(age : int) -> str :
#   result = 2025 - age
#   return f'{age}에 태어난 사람의 나이는{result}입니다.'

# # 문제 2. 할인 계산 API
# # URL : /discount/<float:price>/<int:rate>
# # 할인율(rate)은 정수 %로 주어짐
# # 최종 가격을 계산하여 문자열로 반환
# @app.route('/discount/<int:price>/<int:rate>')
# def discount(price : float, rate: int) -> str :
#   result = price -((price * rate) / 100)
#   return f'원가는 {price}원 이며, 할인율은 {rate}% 최종 가격은 {result}원 입니다.'

# @app.route('/hello/<name>', endpoint='hello-oz-endpoint')
# def hello(name): # 함수명은 겹치면 안됩니다.
#   return f'Hello {name} !!'

# with app.test_request_context():
#   result = url_for("hello-oz-endpoint", name="ungbi") #/hello/웅비

# ------------------------ 08/11 파머님 라이브 세션 ------------------------

# @app.route('/user')
# def get_user():
#   user = {"name":"지수", "age":24}
#   return jsonify(user)

# @app.route('/users', methods=["POST"])
# def create_user():
#   data = {"id":1, "name":"지수"}
#   resp = jsonify(data)
#   resp.status_code = 201 # 전세계 공통 상태코드 
#   resp.headers["Location"] = f"/user/{data['id']}" # 딕셔너리 데이터 타입에서 해당하는 키 값을 찾고 그 안에 값을 변경할 때
#   return resp

# @app.route('/dict')
# def dict_json():
#   return jsonify({"a": 1})

# @app.route('/list')
# def list_json():
#   return jsonify([1,2,3])

# @app.route('/args')
# def args_json():
#   return jsonify(1,2,3)

# @app.route("/kwargs")
# def kwargs_json():
#   return jsonify(a=1, b=2)



# @app.route('/login')
# def login():
#   session['username'] = 'hong' # 키와 벨류 => dict / username 에 키가 있으면 값이 바뀜 (없으면 키값 생성 후 값을 넣음)
#   return '로그인 완료: 세션에 저장됨'

# @app.route('/status')
# def status():
#   username = session.get('username') # 임의의 값을 넣습니다.
#   return f'현재 사용자 : {username}'

# @app.route('/logout')
# def logout():
#   session.pop('username', None) # session.pop을 실행할때 해당 key값이 없을경우 에러 발생 ( None 추가 )
#   return "로그아웃 완료: 세션에서 제거됨"

# @app.route('/check')
# def check():
#   # 스크래핑 -> 후드가 있는지 없는지 확인
#   if 'username' in session :
#     return f"{session['username']}님이 로그인 중입니다."
#   return '로그인 해주세요.'

# @app.route("/users")
# def users():
#   data = {
#     "title" : "사용자 목록",
#     "users" : [
#       {"name": "지수", "age" : 30, "skills":["Python", "Flask"]},
#       {"name": "민수", "age" : 17, "skills":[]}
#     ]
#   }
#   return render_template("users.html", **data) # **data -> 언팩킹 { "title" : "사용자 목록", "users"}

# 리스트 안에 딕트, 딕트안에 리스트, -> 데이터 타입의 활용



# 직렬화가 가능한 python 생성한 데이터를 -> 직렬화 -> 
# json( Object <> dict, array <> list, string <> str, number <> int(float), boolean <> TrueFalse, null )

# json 지원하지 않는 데이터 타입
# 1. Datetime, date, time, decimal, set, UUID, Path, 커스텀


# ------------------------ 08/12 파머님 라이브 세션 ------------------------






