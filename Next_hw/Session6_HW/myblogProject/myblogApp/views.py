from django.shortcuts import render, redirect
from .models import Posting
import time

# Create your views here.
def index(request):
    len_postings = len(Posting.objects.all())
    len_movies = len(Posting.objects.filter(category="Movie"))
    len_dramas = len(Posting.objects.filter(category="Drama"))
    len_programmings = len(Posting.objects.filter(category="Programming"))
    return render(request, 'index.html', {'len_postings':len_postings, 'len_movies':len_movies, 'len_dramas':len_dramas, 'len_programmings':len_programmings})

def movie(request):
    postings = Posting.objects.filter(category="Movie")
    len_postings = len(postings)
    return render(request, 'movie.html', {'postings':postings, 'len_postings':len_postings, })

def drama(request):
    postings = Posting.objects.filter(category="Drama")
    len_postings = len(postings)
    return render(request, 'drama.html', {'postings':postings, 'len_postings':len_postings, })

def programming(request):
    postings = Posting.objects.filter(category="Programming")
    len_postings = len(postings)
    return render(request, 'programming.html', {'postings':postings, 'len_postings':len_postings, })

def new(request):
    return render(request, 'new.html')

def submit(request):
    tm = time.localtime(time.time())
    new_posting = Posting.objects.create(
        title = request.POST['title'],
        category = request.POST['category'],
        content = request.POST['content'],
        writetime = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)
    )
    return redirect('detail', posting_pk=new_posting.pk)

def detail(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    return render(request, 'detail.html', {'posting':posting, })











