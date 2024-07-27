from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import UrlShortener
from .forms import UrlForm
import random
import string

def generate_short_url(length=7):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def url_view(request, short_url=None):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data['long_url']
            url = UrlShortener.objects.filter(long_url=long_url).first()
            print(url)
            if url:
                url.count += 1
                url.save()
            else:
               short_url = 'http://127.0.0.1:8000/' + generate_short_url()
               UrlShortener.objects.create(long_url=long_url, short_url=short_url)
               return HttpResponse(f"Short URL: {request.build_absolute_uri(short_url)}")
    elif short_url:
        url = get_object_or_404(UrlShortener, short_url=short_url)
        url.count += 1
        url.save()
        return redirect(url.long_url)
    
    form = UrlForm()
    return render(request, 'url_form.html', {'form': form})
