from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    # データの作成が完了したときの遷移先URL
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    # データの削除が完了したときの遷移先URL
    success_url = reverse_lazy('list')
