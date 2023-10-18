from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
# Create your views here.
class ReviewForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    review = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(min_value=1, max_value=5)

def reviews(request):
    if request.method == 'GET':
        form = ReviewForm()

        return render(request, 'reviews.html', {
            'form':form
            })

    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(11111111111111111111111111111111111111111, data, 22222222222222222222222222222222222222222222)
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')
            with open('./data.csv','a',encoding="UTF-8")as file:
                file.write(f'{name}|{email}|{review}|{rating}\n')
            return redirect('reviews')

        else:
            print(333333333)
            form = ReviewForm()
            return render(request, 'reviews.html', {'form':form})
