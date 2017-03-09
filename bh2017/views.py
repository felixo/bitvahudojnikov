from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.core.urlresolvers import reverse
from models import Artist
from forms import ArtistForm
from django.contrib.auth.models import User



def index(request):
    form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def thankyou(request):
    return render(request, 'bh2017/thankyou.html')

def addArtist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(form.data['name'], form.data['email'], 'johnpassword')
            profile = form.save(commit=False)
            if profile.user_id is None:
                profile.user_id = user.id
            profile.save()
            return HttpResponseRedirect(reverse('bh2017:thankyou'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})
