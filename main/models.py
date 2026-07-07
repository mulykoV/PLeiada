from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    TYPE_CHOICES = [
        ('poem',    'Вірш'),
        ('prose',   'Проза'),
        ('thought', 'Думка'),
    ]

    author    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title     = models.CharField(max_length=200, blank=True, null=True, verbose_name='Назва')
    body      = models.TextField(verbose_name='Текст')
    post_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='thought', verbose_name='Тип')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    background = models.CharField(max_length=20, default='default')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Допис'
        verbose_name_plural = 'Дописи'

    def __str__(self):
        return f"{self.get_post_type_display()} — {self.author.first_name} ({self.created_at:%d.%m.%Y})"

    @property
    def is_long(self):
        """Проза понад 600 символів — відображається як книга"""
        return self.post_type == 'prose' and len(self.body) > 600

    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def recent_likes_count(self):
        """Лайки за останні 7 днів — для алгоритму стрічки"""
        week_ago = timezone.now() - timezone.timedelta(days=7)
        return self.likes.filter(created_at__gte=week_ago).count()


class Like(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post       = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'post')  # один лайк від одного юзера
        verbose_name = 'Вподобання'

    def __str__(self):
        return f"{self.user.first_name} → {self.post}"


class Follow(models.Model):
    follower  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('follower', 'following')  # не можна підписатись двічі
        verbose_name = 'Підписка'

    def __str__(self):
        return f"{self.follower.first_name} → {self.following.first_name}"