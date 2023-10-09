from django.shortcuts import render

# Create your views here.

def reviews(request):
    name_1 = "Егор"
    email_1 = "egorsmirnov316@gmail.com"
    review_1 = "Всё отлично"


    return render(request, 'reviews.html', {"name_1":name_1, "email_1":email_1, "review_1":review_1})