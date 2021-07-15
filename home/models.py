from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class TimestampModel(models.Model):
    """
    Abstract model that provides created_at and updated_at fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class App(TimestampModel):
    """
    App model that contains metadata of an app.
    """
    TYPE_CHOICE = (
        ('Web', _('Web')),
        ('Mobile', _('Mobile')),
    )

    FRAMEWORK_CHOICE = (
        ('Django', _('Django')),
        ('React Native', _('React Native')),
    )

    name = models.CharField(max_length=50)
    description = models.TextField(default='')
    type = models.CharField(max_length=255, choices=TYPE_CHOICE)
    framework = models.CharField(max_length=255, choices=FRAMEWORK_CHOICE)
    domain_name = models.CharField(max_length=50, default='')
    screenshot = models.ImageField(upload_to='screenshots', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , related_name='apps', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _('App')
        verbose_name_plural = _('Apps')
        indexes = [
            models.Index(fields=['name'], name='app_name_idx'),
            models.Index(fields=['domain_name'], name='domain_name_idx'),
        ]
        ordering = ('-updated_at',)
        constraints = [models.UniqueConstraint(fields=['name', 'user'], name='unique_app_name')]

    def __str__(self):
        return self.name


class Plan(TimestampModel):
    """
    Plan model for subscriptions pricing plan.
    """
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        verbose_name = _('Plan')
        verbose_name_plural = _('Plans')
        ordering = ('-updated_at',)
        constraints = [models.CheckConstraint(check=models.Q(price__gte=0), name='plan_price_gte_0')]


    def __str__(self):
        return self.name


class Subscription(TimestampModel):
    """
    Subscription model to tracks what plan is associated with an app.
    """

    app = models.OneToOneField(App, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.CASCADE)
    active = models.BooleanField()

    class Meta:
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')
        ordering = ('-updated_at',)

    def __str__(self):
        return '{} - {}'.format(self.app, self.plan)