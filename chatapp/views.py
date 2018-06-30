# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import auth
from django.template.loader import render_to_string
from django.views import View

from .forms import *
from .models import *


# Create your views here.
def login(request):
    user = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        is_val = form.is_valid()
        if is_val:
            data = form.cleaned_data
            user = auth.authenticate(request, username=data['username'], password=data['password'])
            try:
                ChatUser.objects.get(user=user)
            except:
                form.add_error('username', ['Логин или пароль введены неверно'])
                is_val = False
        if is_val:
            auth.login(request, user)

            return HttpResponseRedirect("../app/")
    else:
        form = LoginForm()

    return render(request, 'login.html', locals())


def logout(request):
    pass


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        is_val = form.is_valid()
        data = form.cleaned_data
        if is_val:
            chat_user = form.save(commit=False)
            chat_user.user = User.objects.create_user(data['username'], data['email'], data['password'])
            chat_user.save()

        return HttpResponseRedirect('../login/')

    else:
        form = RegistrationForm()

    return render(request, "registration.html", locals())


def index(request):
    search_form = SearchForm()
    usr = ChatUser.objects.get(user=request.user)
    # frds = usr.friends.all()
    # Получить список чатов для текущего пользователя
    chats = request.user.chat_set.all()

    return render(request, "index.html", locals())


def get_messages(request, id):
    chat_id = id
    usr = ChatUser.objects.get(user=request.user)
    # Получить список сообщений чата
    messages = Message.objects.filter(chat_id=id)
    # Получить список чатов
    chats = request.user.chat_set.all()
    # Получить текущий чат
    current_chat = chats.get(pk=id)
    # Сохранить сообщение
    '''
    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.chat = Chat.objects.get(pk=id)
            message.save()

        return HttpResponseRedirect('', locals())
    else:
        form = MessageForm()
    '''

    return render(request, "index.html", locals())


def message_create(request):
    if request.method == "POST":
        text = request.POST['text']
        # author
        author = request.user
        # chat
        chat_id = request.POST['chat_id']
        chat = Chat.objects.get(pk=chat_id)
        msg = Message.objects.create(author=author, text=text, chat=chat)

        # print("form = ",chat_id)

        return JsonResponse({
            'id': msg.id,
            'text': msg.text,
            'author': msg.author.username,
            'time': msg.date,
            'renderedTemplate': render_to_string('message.html', {'message': msg}, request)
        })


def add_contact(request):
    if request.method == 'POST':
        cnct_id = request.POST['cnct_id']
        frd = ChatUser.objects.get(pk=cnct_id)
        print('uuuu', frd)
        ch_usr = ChatUser.objects.get(user=request.user)
        ch_usr.friends.add(frd)
        return JsonResponse({})
        



# class Search(View):
#     def post(self,request):
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             q = form.cleaned_data['query']
#             print('q = ', q)
#             usrs = ChatUser.objects.filter(first_name__icontains=q)
#             return JsonResponse({
#                 #имя
#                 'users': q,
#                 #фамилия
#                 #картинка
#                 #темлейт
#             })


def search(request):
    if request.method == "POST":
        res = request.POST.get('query', False)
        print('res', res)
        if res:
            usrs = ChatUser.objects.filter(first_name__contains=res)
        else:
            usrs = ''
        print('usrs', usrs)
        return JsonResponse({

            'renderedTemplate': render_to_string('search_usr.html', {'usrs': usrs}, request)

        })
