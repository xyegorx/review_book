from django.shortcuts import render
# from django import forms
from django.shortcuts import redirect
from reviews.models import Review
from reviews.forms import ReviewForm
# Create your views here.


def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(11111111111111111111111111111111111111111, data, 22222222222222222222222222222222222222222222)
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')
            Review.objects.create(name=name, email=email, review=review, rating=rating)
            return redirect('reviews')

    print(333333333)
    form = ReviewForm()
    reviews = Review.objects.all()
    #review_1 = Review.objects.get(id = 1)
    #print(review_1.name)
    return render(request, 'reviews.html', {'form':form,'reviews':reviews})


