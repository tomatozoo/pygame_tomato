from .forms import QuestionForm, AnswerForm
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Question

# Create your views here.
def index(request):
    return HttpResponse("Hello :D")

def index(request):
    page = request.GET.get('page', '1')
    #question 모델 데이터를 템플릿 파일을 사용하여 화면에 출력할 수 있다. 
    question_list = Question.objects.order_by('-create_date') #생성 날짜의 역순으로 출력
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list' : page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer=form.save(commit=False)
            answer.create_date=timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question':question, 'form' : form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question=form.save(commit=False)
            question.create_date=timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)