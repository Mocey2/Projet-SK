from django.shortcuts import render, get_object_or_404, redirect
from .models import ArticleBlog, Commentaire
from django.contrib.auth.decorators import login_required

def liste_articles(request):
    articles = ArticleBlog.objects.all().order_by('-date_publication')
    return render(request, 'blog/liste_articles.html', {'articles': articles})

def detail_article(request, article_id):
    article = get_object_or_404(ArticleBlog, pk=article_id)
    commentaires = article.commentaires.all().order_by('-date_commentaire')
    return render(request, 'blog/detail_article.html', {
        'article': article,
        'commentaires': commentaires
    })

@login_required
def commenter_article(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(ArticleBlog, pk=article_id)
        contenu = request.POST.get('contenu')
        Commentaire.objects.create(
            article=article,
            auteur=request.user,
            contenu=contenu
        )
    return redirect('blog:detail_article', article_id=article_id)
