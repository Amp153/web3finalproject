# Create your tests here.
import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Title
from django.urls import reverse


class TitleModelTests(TestCase):

    def test_was_published_recently_with_future_title(self):
        """
        was_published_recently() returns False for titles whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_title = Title(pub_date=time)
        self.assertIs(future_title.was_published_recently(), False)

    def test_was_published_recently_with_old_title(self):
        """
        was_published_recently() returns False for titles whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_title = Title(pub_date=time)
        self.assertIs(old_title.was_published_recently(), False)

    def test_was_published_recently_with_recent_title(self):
        """
        was_published_recently() returns True for titles whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_title = Title(pub_date=time)
        self.assertIs(recent_title.was_published_recently(), True)

#Keep outside of class
def create_title(title_text, days):
    """
    Create a title with the given `title_text` and published the
    given number of `days` offset to now (negative for titles published
    in the past, positive for titles that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Title.objects.create(title_text=title_text, pub_date=time)

class TitleIndexViewTests(TestCase):

    def test_no_titles(self):
        """
        If no titles exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('forums:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No forums are available.")
        self.assertQuerysetEqual(response.context['latest_title_list'], [])

    def test_past_title(self):
        """
        Titles with a pub_date in the past are displayed on the
        index page.
        """
        create_title(title_text="Past title.", days=-30)
        response = self.client.get(reverse('forums:index'))
        self.assertQuerysetEqual(
            response.context['latest_title_list'],
            ['<Title: Past title.>']
        )

    def test_future_title(self):
        """
        Titles with a pub_date in the future aren't displayed on
        the index page.
        """
        create_title(title_text="Future title.", days=30)
        response = self.client.get(reverse('forums:index'))
        self.assertContains(response, "No forums are available.")
        self.assertQuerysetEqual(response.context['latest_title_list'], [])

    def test_future_title_and_past_title(self):
        """
        Even if both past and future titles exist, only past titles
        are displayed.
        """
        create_title(title_text="Past title.", days=-30)
        create_title(title_text="Future title.", days=30)
        response = self.client.get(reverse('forums:index'))
        self.assertQuerysetEqual(
            response.context['latest_title_list'],
            ['<Title: Past title.>']
        )

    def test_two_past_titles(self):
        """
        The titles index page may display multiple titles.
        """
        create_title(title_text="Past title 1.", days=-30)
        create_title(title_text="Past title 2.", days=-5)
        response = self.client.get(reverse('forums:index'))
        self.assertQuerysetEqual(
            response.context['latest_title_list'],
            ['<Title: Past title 2.>', '<Title: Past title 1.>']
        )

class TitleDetailViewTests(TestCase):
    
    def test_future_title(self):
        """
        The detail view of a title with a pub_date in the future
        returns a 404 not found.
        """
        future_title = create_title(title_text='Future title.', days=5)
        url = reverse('forums:detail', args=(future_title.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_title(self):
        """
        The detail view of a title with a pub_date in the past
        displays the title's text.
        """
        past_title = create_title(title_text='Past Title.', days=-5)
        url = reverse('forums:detail', args=(past_title.id,))
        response = self.client.get(url)
        self.assertContains(response, past_title.title_text)