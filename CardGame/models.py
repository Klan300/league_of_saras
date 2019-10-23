from django.db import models

# Create your models here.
class Deck(models.Model):
    deck_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.deck_name


class Card(models.Model):
    deck = models.ForeignKey(Deck,on_delete=models.CASCADE)
    card_name = models.CharField(max_length=200)

    def __str__(self):
        return self.card_name
    