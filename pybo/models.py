from django.db import models

# Create your models here.
#필요한 것들을 class로 작성한다. 
class Question(models.Model):
    subject = models.CharField(max_length = 200) #200자까지 입력 가능하다. 
    content = models.TextField() #글자 수 제한이 없는 데이터
    create_date = models.DateTimeField() #시간 관련 속성

    def __str__(self):
        return self.subject


class Answer(models.Model):
    #질문에 대한 답변이므로 question을 모델 속성으로 가져야 한다. 
    #foreignkey는 다른 모델과의 연결을 의미한다. 
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #답변에 연결된 질문이 삭제되면 답변도 함께 삭제하라
    content = models.TextField()
    create_date = models.DateTimeField()