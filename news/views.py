from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm


# Create your views ere.
def add_article(request):
    error = ''
    accept = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            accept = 'Статья была добавлена в ленту'

            try:
                News.objects.create(**form.cleaned_data)
                return redirect('')
            except:
                #form.add_error(None, 'Ошибка добовления поста')
                print('Something go wrong')
    else:
        form = NewsForm()
    return render(request, 'add_article.html', {'form': form, 'error': error, 'accept': accept})


def news(request):
    news1 = News.objects.order_by('-date')
    return render(request, 'news.html', {'news': news1})


def full_text(request, post_id):
    full = News.objects.get(pk=post_id)
    return render(request, 'news_detail.html', {'full': full})



