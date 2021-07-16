from django.contrib import admin

from home.models import App, Plan, Subscription

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'framework', 'user', 'created', 'modified')
    search_fields = ('name', 'domain_name')
    list_filter = ('created', 'modified')

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created', 'modified')
    search_fields = ('name',)
    list_filter = ('created', 'modified')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('app', 'plan', 'active', 'created', 'modified')
    search_fields = ('app', 'plan')
    list_filter = ('active', 'created', 'modified')

