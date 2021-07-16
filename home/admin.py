from django.contrib import admin

from home.models import App, Plan, Subscription

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'framework', 'user', 'created_at', 'modified_at')
    search_fields = ('name', 'domain_name')
    list_filter = ('created_at', 'modified_at')

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at', 'modified_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'modified_at')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('app', 'plan', 'active', 'created_at', 'modified_at')
    search_fields = ('app', 'plan')
    list_filter = ('active', 'created_at', 'modified_at')

