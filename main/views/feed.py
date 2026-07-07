from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from main.models import Post, Like, Follow

# Дозволені ключі тем фону — мають збігатись з тими, що використовуються в feed.html
BACKGROUND_CHOICES = {'default', 'amber', 'dusk', 'midnight', 'moss', 'rose'}


def get_feed_posts(user):
    week_ago = timezone.now() - timezone.timedelta(days=7)

    following_ids = Follow.objects.filter(
        follower=user
    ).values_list('following_id', flat=True)

    # Дописи підписок + свої власні
    followed_posts = Post.objects.filter(
        author_id__in=list(following_ids) + [user.id]
    ).select_related('author').prefetch_related('likes').order_by('-created_at')

    # Решта — чужі, на кого не підписаний
    other_posts = Post.objects.exclude(
        author_id__in=list(following_ids) + [user.id]
    ).select_related('author').prefetch_related('likes')

    other_posts = sorted(
        other_posts,
        key=lambda p: p.likes.filter(created_at__gte=week_ago).count(),
        reverse=True
    )

    liked_ids = set(
        Like.objects.filter(user=user).values_list('post_id', flat=True)
    )

    all_posts = list(followed_posts) + list(other_posts)

    for post in all_posts:
        post.user_liked = post.id in liked_ids

    return all_posts


@login_required
def main_feed(request):
    posts = get_feed_posts(request.user)
    return render(request, 'main/feed.html', {
        'posts': posts,
        'user': request.user,
    })


@login_required
@require_POST
def create_post(request):
    post_type  = request.POST.get('post_type', 'thought')
    title      = request.POST.get('title', '').strip() or None
    body       = request.POST.get('body', '').strip()
    background = request.POST.get('background', 'default')

    if post_type not in ('thought', 'poem', 'prose'):
        post_type = 'thought'

    # Фони доступні тільки для думок і віршів
    if post_type == 'prose' or background not in BACKGROUND_CHOICES:
        background = 'default'

    if not body:
        return redirect('feed')

    Post.objects.create(
        author=request.user,
        title=title,
        body=body,
        post_type=post_type,
        background=background,
    )
    return redirect('feed')


@login_required
@require_POST
def toggle_like(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({'error': 'not found'}, status=404)

    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({
        'liked': liked,
        'count': post.likes.count(),
    })