from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required, user_passes_test  
from blog.models import Article as mArticle, Paragraphe as mParagraphe, Profile as mProfile
from django.contrib.auth import logout as auth_logout, authenticate, login
from django.contrib.auth.models import User
from .forms import SignUpForm

def Home(request):
    miniPost = mArticle.objects.all().order_by('-pk')[:3]
    bestAuteur = mProfile.objects.all().order_by('-NbArticles')[:6]
    template = loader.get_template('blog/home.html')
    context = {
        'pageName' : "Accueil" + " - ",
        'miniPost' : miniPost,
        'bestAuteur' : bestAuteur,
    }
    return HttpResponse(template.render(context, request=request))

def Article(request, article_id):
    miniPost = mArticle.objects.all().order_by('-pk')[:3]
    article = get_object_or_404(mArticle, pk=article_id)
    paragraphes = mParagraphe.objects.filter(zArticle=article).order_by('NumOrder')

    template = loader.get_template('blog/article.html')
    context = {
        'articleName' : article.Titre,
        'pageName' : article.Titre + " - ",
        'miniPost' : miniPost,
        'article' : article,
        'paragraphes' : paragraphes,
        }
    return HttpResponse(template.render(context, request=request))

def Profile(request, profil_id):
    miniPost = mArticle.objects.all().order_by('-pk')[:3]
    profil = get_object_or_404(mProfile, pk=profil_id)
    articles = mArticle.objects.all().filter(Auteur=profil).order_by('-pk')
    template = loader.get_template('blog/profile.html')
    context = {
        'pageName' : profil.__str__() + " - ",
        'miniPost' : miniPost,
        'profil' : profil,
        'articles' : articles,
    }
    return HttpResponse(template.render(context, request=request))

@user_passes_test(lambda u: u.groups.filter(name='Auteur').exists(), login_url='/')
def Parametres(request, profil_id):
    miniPost = mArticle.objects.all().order_by('-pk')[:3] 
    template = loader.get_template('blog/settings.html')
    zUser = get_object_or_404(User, pk=profil_id)
    profil = mProfile.objects.get(User=zUser)
    if request.method == 'POST':
        profil.Bio = request.POST.get('Bio')
        profil.save()
    context = {
        'profil' : profil,
        'pageName' : "Paramètres - ",
        'miniPost' : miniPost,
    }
    return HttpResponse(template.render(context, request=request))

@user_passes_test(lambda u: u.groups.filter(name='Auteur').exists(), login_url='/')
def NewArticle(request, profil_id):
    miniPost = mArticle.objects.all().order_by('-pk')[:3] 
    template = loader.get_template('blog/createArticle.html')
    zUser = get_object_or_404(User, pk=profil_id)
    profil = mProfile.objects.get(User=zUser)
    if request.method == 'POST':
        zArticle = mArticle.objects.create(
            Auteur = profil,
            Titre = request.POST.get('Titre'),
            Intro = request.POST.get('Texte'),
            Image = request.POST.get('Image')
        )
        profil.NbArticles += 1
        profil.save()
        iterator = 0
        while request.POST.get('Para'+str(iterator)):
            paraContent = request.POST.get('Para'+str(iterator))
            titre = request.POST.get('Titre'+str(iterator))
            iterator+=1
            para = mParagraphe.objects.create(
                zArticle = zArticle,
                NumOrder = iterator,
                Content = paraContent,
                Titre = titre
            )
    context = {
        'profil' : profil,
        'pageName' : "Paramètres - ",
        'miniPost' : miniPost,
    }
    return HttpResponse(template.render(context, request=request))

def search(request):
    miniPost = mArticle.objects.all().order_by('-pk')[:3] 
    template = loader.get_template('blog/search.html')
    query = request.GET.get('query')
    if not query:
        articles = mArticle.objects.all().order_by('-pk')
    else:
        articles = mArticle.objects.filter(Titre__icontains=query).order_by('-pk')
    title = "Résultats pour la requête %s"%query
    context = {
        'articles': articles,
        'pageName': title + " - ",
        'title' : title,
        'miniPost' : miniPost,
    }
    return HttpResponse(template.render(context, request=request))

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})