from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse  
from .models import Question, Option

# def index(request):  
#     template = loader.get_template('index.html') # getting our template  
#     if request.method == "POST":
#         question = request.POST['qs']
#         print(f'Question: {question}')
#         answer = request.POST['Options[]']
#         print(f'Answer: {answer}')
#     # print(f'Question: {question}')
#     # print(f'Answer: {answer}')

#     return HttpResponse(template.render())       # rendering the template in HttpResponse  
 
def post_answers(request):
#     if request.method == "POST":
#         question = request.POST['qs']
#         qs = Question.objects.create(text=question)
#         qs.save()
#         answers = request.POST.getlist('Options[]')
#         for answer in answers:
#              ops = Option.objects.create(question=qs, text=answer)
#              ops.save()
#         print(answers)
    if request.method == "POST":
         question = request.POST['qs']

         options=request.POST.getlist('Options[]')
         # options=request.POST.getlist('options')
         cleaned_options = [op for op in options if op]
         print(cleaned_options)
         # qs.save()
         a = Question.objects.create(options=[cleaned_options],question=question, )
    
    all = Question.objects.all()
  
    return render(request, 'index.html', {'all':all})
