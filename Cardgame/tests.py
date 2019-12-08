from django.test import TestCase

from models import Deck, Card, Playerscore

class DeckModelTest(TestCase):
    def setUp(self):
        Deck.objects.create(deck_name='English')
        Deck.objects.create(deck_name='Science')
    
    def test_deck_count(self):
        self.assertEqual(2, Deck.objects.count())
