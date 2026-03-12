from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Comment
from articles.models import Article
from audit_log.utils import log_action


# Create your views here.

@login_required
def add_comment(request, article_id):
    """ Add a comment to an article """
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        body = request.POST.get('body')
        if body:
            Comment.objects.create(
                article=article,
                author=request.user,
                body=body,
                is_approved=False
            )
            log_action(request.user, 'comment', f'Comment on: {article.title }', request)
            messages.success(request, 'Comment submitted and awaiting approval')
        return redirect('articles:article_detail', slug=article.slug)
    
    return redirect('articles:article_detail', slug=article.slug)



@login_required
def edit_comment(request,comment_id):
    """ Edit a comment (only the author can edit) """
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        messages.error(request, 'You can only edit your own comments')
        return redirect('articles:article_detail', slug=comment.article.slug)
    
    if request.method == 'POST':
        body = request.POST.get('body')
        if body:
            comment.body = body
            comment.save()
            messages.success(request, 'Comment updated successfully')
        return redirect('articles:article_detail', slug=comment.article.slug)
    
    return render(request, 'comments/edit_comment.html', {'comment': comment})



@login_required
def delete_comment(request, comment_id):
    """ Delete a comment (only the author can delete) """
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        messages.error(request, 'You can only delete your own comments')
        return redirect('articles:article_detail', slug=comment.article.slug)
    
    if request.method == 'POST':
        article_slug = comment.article.slug
        comment.delete()
        messages.success(request, 'Comment deleted')
        return redirect('articles:article_detail', slug=article_slug)
    
    return render(request, 'comments/delete_comment.html', {'comment': comment})
