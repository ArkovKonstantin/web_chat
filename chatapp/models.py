# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat(models.Model):
    chatuser = models.ManyToManyField(User)
    chat_name = models.CharField(max_length=30, verbose_name='Название чата')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    objects = models.Manager()

    def __unicode__(self):
        return self.text


class ChatUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='День рождения')
    friends = models.ManyToManyField("self", symmetrical=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.user)
