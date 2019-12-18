from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.exceptions import ObjectDoesNotExist

from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from time import sleep
from threading import Event

from .models import Deck, Card, Playerscore


class DeckModelTest(TestCase):
    
    def setUp(self):
        self.deck1 = Deck.objects.create(deck_name='English')
        self.deck2 = Deck.objects.create(deck_name='Science')
        self.deck3 = Deck.objects.create(deck_name='Animal')
        self.deck4 = Deck.objects.create(deck_name='7-11')
        self.deck5 = Deck.objects.create(deck_name='House')
        self.card1 = Card.objects.create(deck=self.deck1, card_name='Alphabet')
        self.card2 = Card.objects.create(deck=self.deck3, card_name='Tiger')
        self.card2 = Card.objects.create(deck=self.deck3, card_name='Cat')
        self.card3 = Card.objects.create(deck=self.deck4, card_name='Milk')
        self.card4 = Card.objects.create(deck=self.deck4, card_name='Milk')
        self.card5 = Card.objects.create(deck=self.deck4, card_name='Milk')
    
    def test_deck_count(self):
        self.assertEqual(5, Deck.objects.count())

    def test_card_count(self):
        english = Card.objects.get(deck=self.deck1)
        self.assertEqual(english.deck, self.deck1)

    def test_deck_name(self):
        self.assertEqual(str(self.deck1), 'English')
        self.assertEqual(str(self.deck2), 'Science')
    
    def test_card_name(self):
        self.assertEqual(str(self.card1), 'Alphabet')

    def test_delete_deck(self):
        Deck.objects.get(deck_name="Animal").delete()
        self.assertEqual(Deck.objects.count(), 4)
        with self.assertRaises(ObjectDoesNotExist):
            Deck.objects.get(deck_name="Animal").delete()
        with self.assertRaises(ObjectDoesNotExist):
            Deck.objects.get(deck_name="Wrong").delete()
    
    def test_change_question(self):
        name = Deck(id=1, deck_name='Sport')
        name.save()
        self.assertEqual(Deck.objects.get(id=1), name)
    
    def test_add_non_exist_question_by_id(self):
        name = Deck(id=100, deck_name='Sport')
        name.save()
        self.assertEqual(Deck.objects.count(), 6)
    
    def test_number_card_with_deck(self):
        c = Card.objects.filter(deck=1)
        self.assertEqual(c.count(), 1)
        c = Card.objects.filter(deck=2)
        self.assertEqual(c.count(), 0)
        c = Card.objects.filter(deck=3)
        self.assertEqual(c.count(), 2)
    
    # def test_method_deck_number_of_card(self):
    #     deck = Deck()
    #     num = deck.number_of_card()
    #     self.assertEqual(num, 6)


class TestLoginPage(StaticLiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.deck1 = Deck.objects.create(deck_name='English')
        self.deck2 = Deck.objects.create(deck_name='Science')
        User = get_user_model()
        self.user = User.objects.create_user(username='normal', email='normal@user.com', password='foo')
    
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

    # def test_login_page_redirect_to_login_google(self):
    #     self.browser.get(self.live_server_url + self.test_login)
    #     self.browser.find_element_by_id('btn').click()
    #     sleep(1)
    #     self.browser.find_element_by_partial_link_text('Google').click()
    #     sleep(300)
    #     self.browser.find_element_by_id("identifierId").send_keys('hijimmybug')
    #     self.browser.find_element_by_id("identifierNext").click()
    #     self.browser.find_element_by_name("password").send_keys('1qaz2wsx3edc4rfv5tghb6yhn7ujm')
    #     self.browser.find_element_by_id("passwordNext").click()
    #     sleep(60)
    #     # url = urlparse(self.browser.current_url)
    #     # self.assertEquals(url.netloc, 'accounts.google.com')
    

# class TestHomePage(StaticLiveServerTestCase):

#     @classmethod
#     def setUpTestData(cls):
#         cls.deck1 = Deck.objects.create(deck_name='English')
#         cls.deck2 = Deck.objects.create(deck_name='Science')
#         cls.deck3 = Deck.objects.create(deck_name='Animal')
#         cls.deck4 = Deck.objects.create(deck_name='7-11')
#         cls.deck5 = Deck.objects.create(deck_name='House')
#         cls.card1 = Card.objects.create(deck=cls.deck1, card_name='Alphabet')
#         cls.card2 = Card.objects.create(deck=cls.deck3, card_name='Tiger')
#         cls.card2 = Card.objects.create(deck=cls.deck3, card_name='Cat')
#         cls.card3 = Card.objects.create(deck=cls.deck4, card_name='Milk')
#         cls.card4 = Card.objects.create(deck=cls.deck4, card_name='Milk')
#         cls.card5 = Card.objects.create(deck=cls.deck4, card_name='Milk')
#         cls.card6 = Card.objects.create(deck=cls.deck4, card_name='Taro')
#         cls.card7 = Card.objects.create(deck=cls.deck4, card_name='Pokki')
#         cls.card8 = Card.objects.create(deck=cls.deck4, card_name='Oishi')
#         cls.card9 = Card.objects.create(deck=cls.deck4, card_name='Ichitan')
#         cls.card10 = Card.objects.create(deck=cls.deck4, card_name='Dutchmill')
#         cls.card11 = Card.objects.create(deck=cls.deck4, card_name='Seaweed')
#         cls.card12 = Card.objects.create(deck=cls.deck4, card_name='Drug')
    
#     def setUp(self):
#         options = Options()
#         options.headless = True
#         self.browser = webdriver.Firefox(options=options)

#     def tearDown(self):
#         self.browser.close()
    
#     def test_main_page(self):
#         # TODO Login before test this method
#         self.browser.find_element_by_class_name('open-button').click()
#         topic = self.browser.find_element_by_class_name('topic')
#         self.assertEqual(topic, '7-11')
        
#         list_button = self.browser.find_elements_by_class_name('bt')
#         self.assertListEqual(list_button, ['Scoreboard', 'Play'])
    
#     def test_click_main_page_redirect_to_scoreboard(self):
#         # TODO Login before test this method
#         self.browser.find_element_by_class_name('open-button').click()
#         topic = self.browser.find_element_by_class_name('topic')
#         self.browser.find_element_by_partial_link_text('Scoreboard').click()
#         expected_url = self.live_server_url + reverse('scoreboard') + reverse('7/11') + reverse('45')
#         self.assertEqual(self.browser.current_url, expected_url)

#     def test_main_page_redirect_to_logout(self):
#         # TODO Login before test this method
#         logout = self.browser.find_element_by_partial_link_text('logout')
#         self.assertEqual(logout, "logout")
#         logout.click()
#         self.assertEqual(self.current_url, self.live_server_url)
    
#     def test_main_page_redirect_to_setting_page(self):
#         # TODO Login before test this method
#         self.browser.find_element_by_class_name('open-button').click()
#         topic = self.browser.find_element_by_class_name('topic')
#         self.browser.find_element_by_partial_link_text('Play').click()
#         expected_url = self.live_server_url + reverse('setting') + reverse('7/11')
#         self.assertEqual(self.browser.current_url, expected_url)
        

# class TestSettingAndPlayPage(StaticLiveServerTestCase):

#     @classmethod
#     def setUpTestData(cls):
#         cls.deck1 = Deck.objects.create(deck_name='English')
#         cls.deck2 = Deck.objects.create(deck_name='Science')
#         cls.deck3 = Deck.objects.create(deck_name='Animal')
#         cls.deck4 = Deck.objects.create(deck_name='7-11')
#         cls.deck5 = Deck.objects.create(deck_name='House')
#         cls.card1 = Card.objects.create(deck=cls.deck1, card_name='Alphabet')
#         cls.card2 = Card.objects.create(deck=cls.deck3, card_name='Tiger')
#         cls.card2 = Card.objects.create(deck=cls.deck3, card_name='Cat')
#         cls.card3 = Card.objects.create(deck=cls.deck4, card_name='Milk')
#         cls.card4 = Card.objects.create(deck=cls.deck4, card_name='Milk')
#         cls.card5 = Card.objects.create(deck=cls.deck4, card_name='Milk')
#         cls.card6 = Card.objects.create(deck=cls.deck4, card_name='Taro')
#         cls.card7 = Card.objects.create(deck=cls.deck4, card_name='Pokki')
#         cls.card8 = Card.objects.create(deck=cls.deck4, card_name='Oishi')
#         cls.card9 = Card.objects.create(deck=cls.deck4, card_name='Ichitan')
#         cls.card10 = Card.objects.create(deck=cls.deck4, card_name='Dutchmill')
#         cls.card11 = Card.objects.create(deck=cls.deck4, card_name='Seaweed')
#         cls.card12 = Card.objects.create(deck=cls.deck4, card_name='Drug')
    
#     def setUp(self):
#         options = Options()
#         options.headless = True
#         self.browser = webdriver.Firefox(options=options)
#         # TODO login before test this method
#         self.browser.find_element_by_class_name('open-button').click()
#         topic = self.browser.find_element_by_class_name('topic')
#         self.browser.find_element_by_partial_link_text('Play').click()

#     def tearDown(self):
#         self.browser.close()

#     def test_45_seconds_redirect(self):
#         self.browser.find_element_by_id('45').click()
#         self.browser.find_element_by_id('play').click()
#         expected_url = self.live_server_url + reverse('playing') + reverse('7-11')
#         self.assertEqual(expected_url, self.browser.current_url)
    
#     def test_60_seconds_redirect(self):
#         self.browser.find_element_by_id('60').click()
#         self.browser.find_element_by_id('play').click()
#         expected_url = self.live_server_url + reverse('playing') + reverse('7-11')
#         self.assertEqual(expected_url, self.browser.current_url)
    
#     def test_90_seconds_redirect(self):
#         self.browser.find_element_by_id('90').click()
#         self.browser.find_element_by_id('play').click()
#         expected_url = self.live_server_url + reverse('playing') + reverse('7-11')
#         self.assertEqual(expected_url, self.browser.current_url)
    
#     def test_play_correct(self):
#         self.browser.find_element_by_id('60').click()
#         self.browser.find_element_by_id('play').click()
#         for i in range(9):
#             sleep(1)
#             self.browser.find_element_by_id('correct').click()
#         sleep(1)
#         self.browser.find_element_by_class_name('btn btn-warning').click()
#         expected_url = self.live_server_url + reverse('playing') + reverse('7-11') + reverse('summary')
#         self.assertEqual(expected_url, self.browser.current_url)
    
#     def test_play_redirect_to_main_page(self):
#         self.browser.find_element_by_id('60').click()
#         self.browser.find_element_by_id('play').click()
#         for i in range(9):
#             sleep(1)
#             self.browser.find_element_by_id('correct').click()
#         sleep(1)
#         self.browser.find_element_by_class_name('btn btn-warning').click()
#         self.browser.find_element_by_partial_link_text('menu').click()
#         expected_url = self.live_server_url + reverse('home')
#         self.assertEqual(expected_url, self.browser.current_url)
    
#     def test_play_redirect_to_scoreboard(self):
#         self.browser.find_element_by_id('60').click()
#         self.browser.find_element_by_id('play').click()
#         for i in range(9):
#             sleep(1)
#             self.browser.find_element_by_id('correct').click()
#         sleep(1)
#         self.browser.find_element_by_class_name('btn btn-warning').click()
#         expected_url = self.live_server_url + reverse('scoreboard') + reverse("7-11") + reverse("60")
#         self.browser.find_element_by_partial_link_text('Scoreboard').click()
#         self.assertEqual(expected_url, self.browser.current_url)


class UsersManagersTest(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='normal', email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username='super', email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='super', email='super@user.com', password='foo', is_superuser=False)


# class TestViews(TestCase):

#     def test_project_list_GET(self):
#         client = Client()
#         response = client.get(index)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'templates/Cardgame/index.html')
    