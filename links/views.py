from django.shortcuts import render
import json
from hashids import Hashids
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone

from .models import URL


@csrf_exempt
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