from django.apps import AppConfig

#여기에 클래스가 생겨났네. 
class PyboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pybo'

    #pyboConfig 클래스가 installed_apps에 추가되지 않으면, 데이터 베이스 관련 작업을 할 수 없다. 
    #장고는 모델을 이용하여
    #데이터베이스의 실체가 될 테이블을 만든다. 
    #이때 모델은 앱에 종속되어 있다. 
    #따라서 장고에 앱 파이보를 등록해야 진행할 수 있다. 