from django.test import TestCase
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from time import sleep

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


class TestListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('Cardgame/chromedriver/chromedriver.exe')
    
    def tearDown(self):
        self.browser.close()
    
    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)

        # The user requests the page for the first time
        alert = self.browser.find_element_by_class_name('home')
        self.assertEquals(
            alert.find_element_by_tag_name('h1').text,
            'league of saras'
        )
