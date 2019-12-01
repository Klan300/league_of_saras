from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Deck(models.Model):
    deck_name = models.CharField(max_length=200,unique=True)

    def number_of_card(self):
        deck = Deck.objects.filter(deck_name=self.deck_name)[0]
        return deck.card_set.count()

    def __str__(self):
        return self.deck_name


class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=200)

    def __str__(self):
        return self.card_name


class Playerscore(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    time = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
