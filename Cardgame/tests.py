from django.test import TestCase

from .models import Deck, Card, Playerscore

class DeckModelTest(TestCase):
    def setUp(self):
        self.deck1 = Deck.objects.create(deck_name='English')
        self.deck2 = Deck.objects.create(deck_name='Science')
        self.card1 = Card.objects.create(deck=self.deck1, card_name='What is the alphabet?')
    
    def test_deck_count(self):
        self.assertEqual(2, Deck.objects.count())

    def test_card_count(self):
        english = Card.objects.get(deck=self.deck1)
        self.assertEqual(english.deck, self.deck1)
