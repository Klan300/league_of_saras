from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from time import sleep
from threading import Event
from urllib.parse import urlparse

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

    def test_deck_name(self):
        self.assertEqual(str(self.deck1), 'English')
        self.assertEqual(str(self.deck2), 'Science')
    
    def test_card_name(self):
        self.assertEqual(str(self.card1), 'What is the alphabet?')


class TestListPage(StaticLiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.deck1 = Deck.objects.create(deck_name='English')
        self.deck2 = Deck.objects.create(deck_name='Science')
    
    def tearDown(self):
        self.browser.close()
    
    def test_first_page(self):
        self.browser.get(self.live_server_url)

        # The user requests the page for the first time
        alert = self.browser.find_element_by_class_name('home')
        self.assertEquals(
            alert.find_element_by_tag_name('h1').text,
            'league of saras'
        )
    
    def test_login_page_redirect_to_login_facebook(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('btn').click()
        sleep(1)
        self.browser.find_element_by_partial_link_text('Facebook').click()
        url = urlparse(self.browser.current_url)
        self.assertEquals(url.netloc, 'www.facebook.com')

    def test_login_page_redirect_to_login_google(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('btn').click()
        sleep(1)
        self.browser.find_element_by_partial_link_text('Google').click()
        url = urlparse(self.browser.current_url)
        self.assertEquals(url.netloc, 'accounts.google.com')
