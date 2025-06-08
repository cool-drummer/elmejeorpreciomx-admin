from django.contrib import admin
from auth_mercado_libre.models import MercadoToken


class MercadoLibreAdmin(admin.ModelAdmin):
    list_display = (
        'access_token',
        'token_type',
        'expires_in',
        'scope',
        'user_id',
        'refresh_token',
    )
    search_fields = (
        'access_token',
        'token_type',
        'expires_in',
        'scope',
        'user_id',
        'refresh_token',
    )

admin.site.register(MercadoToken, MercadoLibreAdmin)
