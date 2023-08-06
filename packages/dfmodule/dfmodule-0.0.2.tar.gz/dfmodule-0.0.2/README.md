# dfmodule
 common use data flow project

> 패키지 빌드

1. root path에 setup.py 작성

2. root/[패키지 폴더] 안에 __init__.py 에 __version__ = '0.0.1' 작성
 - 이후 패키지 업데이트시 버전을 올려준다. setup, __init__ 동시에 올려야 함.

3. root 폴더 위치에서 cmd 열고 아래 명령어 실행
 - python setup.py sdist bdist_wheel

> PyPI에 패키지 업로드

4. twine 패키지 설치
 - pip install twine

5. 다음의 명령어 실행하여 패키지 업로드
 - twine upload dist/*

6. 업로드시 PyPI의 username, password를 작성한다.
- username: __token__
- password: PyPI에서 발급받은 토큰
도 가능