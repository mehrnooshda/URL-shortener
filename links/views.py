import json
from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from django.utils import timezone
from .models import URL
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['usernaame']
        print(name)
        return JsonResponse({'message': 'Success'})
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username = username, password = password)
#             login(request, user)
#             return JsonResponse({'message': 'Successfully registered'})
#     else:
#         # form = UserCreationForm()
#         # return JsonResponse({'msg': 'hfu'})
#         return render(request, 'registration/register.html', {'form': form})



@csrf_exempt
# @login_required()
def hash1_url(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        original_url = data['original_url']
        print('original_url', original_url)

        url = URL(original_url=original_url, creation_date=timezone.now())
        url.save()
        return JsonResponse({'message': 'Success',
                             'id': url.id})
@csrf_exempt
# @login_required()
def hash_url(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        original_url = data['original_url']
        print('original_url', original_url)

        url = URL(original_url=original_url, creation_date=timezone.now())
        url.save()
        return JsonResponse({'message': 'Success',
                             'id': url.id})


def lookup_url_and_redirect(request, short_url):
    try:
        record = URL.objects.get(shortened_url=short_url)
        redirected_url = record.original_url
        return JsonResponse({'message': 'Success',
                             'redirect url': redirected_url})
    except URL.DoesNotExist:
        return JsonResponse({'message': 'Not Found'})