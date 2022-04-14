from django.http import HttpResponse

from .models import Book


# def index(request):
#     latest_question_list = Book.objects.order_by('-published_time')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def login(request):
    if request.method == "POST":
        form = Login(request.POST)