from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.core.urlresolvers import reverse
from forms import ArtistForm


def index(request):
    form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def thankyou(request):
    return render(request, 'bh2017/thankyou.html')

def addArtist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('bh2017:thankyou'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})
