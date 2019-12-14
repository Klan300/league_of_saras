from django.contrib import admin
from .models import Deck,Card,Playerscore


class CardInline(admin.StackedInline):
    model = Card
    extra = 2

class DeckAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,     {'fields': ['deck_name']}),
    ]
    inlines = [CardInline]

    list_display = ('deck_name','number_of_card')

admin.site.register(Deck)