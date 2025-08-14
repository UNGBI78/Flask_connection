from flask import Blueprint, render_template

# Blueprint 객체 생성 
#'user'는 Blueprint 이름, __name__ 은 현재 파일 이름, url_prefix는 접두 경로

user_bp = Blueprint('user', __name__, url_prefix='/user')

# 라우터 정의
@user_bp.route('/<username>')
def profile(username):
  return render_template('user.html', username=username)