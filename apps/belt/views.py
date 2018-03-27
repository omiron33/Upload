from django.shortcuts import render, redirect
from .models import User, Quote
from django.db.models import Count
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    if 'email' in request.session.keys():
        return redirect ('/quotes')
    return render(request, "belt/index.html")

def reg(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/main')
    else:
        userpass = request.POST['pw']
        hashpass = bcrypt.hashpw(userpass.encode(), bcrypt.gensalt())
        User.objects.create(name=request.POST['name'], alias=request.POST['alias'],email = request.POST['email'], password=hashpass, dob = request.POST['dob'])
        temp = User.objects.last()
        request.session['id'] = temp.id
        request.session['name'] = temp.name
        request.session['email'] = temp.email
    return redirect ('/quotes')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/main')
    else:
        temp = User.objects.filter(email = request.POST['logemail'])
        request.session['name'] = temp[0].name
        request.session['alias'] = temp[0].alias
        request.session['id'] = temp[0].id
        request.session['email'] = temp[0].email
        return redirect("/quotes")

def logout(request):
    request.session.flush()
    return redirect ('/main')

def quotes(request):
    if 'email' not in request.session:
        return redirect ('/main')
    
    else:
        context = {
            'user' : User.objects.get(email = request.session['email']),
            'quotes' : Quote.objects.exclude(likers = request.session['id']),
            'favorites' : Quote.objects.filter(likers = request.session['id'])
        }
        return render(request, 'belt/quotes.html', context)

def add(request):
    errors = Quote.objects.quote_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/main')
    else:
        Quote.objects.create(quote=request.POST['message'], author=request.POST['author'], poster_id = request.session['id'] )
    return redirect('/quotes')

def addfave(request,id):
    quote = Quote.objects.get(id = id)
    person = User.objects.get(id = request.session['id'])
    person.favorites.add(quote)
    return redirect ('/quotes')

def unfave(request, id):
    quote = Quote.objects.get(id=id)
    person = User.objects.get(id=request.session['id'])
    person.favorites.remove(quote)

    return redirect ('/quotes')

def user(request, id):
    person = User.objects.get(id = id)
    context = {
    'name' : person.name,
    'count' : person.quotes.count(),
    'user' : person.quotes.all()
    }
    return render(request, 'belt/user.html', context)