from django.shortcuts import render, redirect
from .models import Task, Comment
from .forms import TaskForm, CommentForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def price(request):
    return render(request, 'main/price.html')


def feedback(request):
    tasks = Task.objects.order_by('-id')
    comments = Comment.objects.order_by('id')
    response_data = {
        'tasks': tasks,
        'comments': comments
    }
    return render(request, 'main/feedback.html', response_data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def createComment(request, pk):
    error = ''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.keys_id = pk
            form.save()
            return redirect('feedback')
        else:
            error = 'Форма была неверной'
    form = CommentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/createComment.html', context)
