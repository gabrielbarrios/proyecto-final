from main.models import User, Tweet
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from main.forms import UserForm, TweetForm
from django.contrib.auth.decorators import login_required

def users(request):
    users = User.objects.all()
    return render_to_response('users.html', {
        'users': users,
    })

def add_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users')
    return render_to_response('add_user.html', {
        'form': form,
    }, RequestContext(request))

def add_tweet(request):
    form = TweetForm()
    if request.method == 'POST':
		form = TweetForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('users')
    return render_to_response('add_user.html', {
		'form': form,
    }, RequestContext(request))
