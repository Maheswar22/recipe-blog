# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import User,Cheff,Recipe
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):

    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('task:recipes_list'))
        else:
            return render(request, 'task/base.html', {})

    else:
        return render(request, 'task/base.html', {})

def recipe_list(request):
    recipes_list = Recipe.objects.order_by('-updated_at')
    return render(request, 'task/recipes_list.html', {'recipes_list' : recipes_list})

def delete_recipe(request, pk):
    Recipe.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('task:recipes_list'))

def recipe_detail(request,pk):
    details = Recipe.objects.get(pk=pk)
    return render(request, 'task/recipe_detail.html', {'details': details})

def signup(request):

    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, email=email, password=password)
        Cheff.objects.create(username=user, name=name)
        return HttpResponseRedirect(reverse('task:index'))
    else:
        return render(request, 'task/signup.html', {})

def cerate_recipe(request):
    if request.method == "POST":
        user = request.user
        u = User.objects.get(username=user)
        cheff_name = Cheff.objects.get(username=u)
        Recipe.objects.create(
            cheff_name = cheff_name,
            recipe_name = request.POST['recipe_name'],
            ingeridents = request.POST['ingeridents'],
            process = request.POST['process'],
        )
        return HttpResponseRedirect(reverse('task:recipes_list'))
    else:
        return render(request, 'task/create_recipe.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('task:index'))
