from django.test import TestCase

# Create your tests here.

import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Issue
from django.urls impot	reverse
class IssueMethodTests(TestCase):
    def test_was_published_recently_with_future_issue(self):
        """
        was_published_recently() should return False for issues whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_issue = Issue(pub_date=time)
        self.assertIs(future_issue.was_published_recently(), False)



    def test_was_published_recently_with_old_issue(self):
        """
        was_published_recently() should return False for issues whose
        pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_issue = Issue(pub_date=time)
        self.assertIs(old_issue.was_published_recently(), False)
    def test_was_published_recently_with_recent_issue(self):
        """
        was_published_recently() should return True for issues whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_issue = Issue(pub_date=time)
        self.assertIs(recent_issue.was_published_recently(), True)i


    def create_issue(issue_text, days):
	    """
	    Creates a issue with the given `issue_text` and published the
	    given number of `days` offset to now (negative for questions published
	    in the past, positive for issues that have yet to be published).
	    """
	    time = timezone.now() + datetime.timedelta(days=days)
	    return Issue.objects.create(issue_text=issue_text, pub_date=time)
class IssueViewTests(TestCase):
    def test_index_view_with_no_issues(self):
        """
        If no issues exist, an appropriate message should be displayed.  
	"""
	response = self.client.get(reverse('polls:index'))
	self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
	self.assertQuerysetEqual(response.context['latest_issue_list'], [])
    def test_index_view_with_a_past_issue(self):
        """
	Issues with a pub_date in the past should be displayed on the index page.
	"""
	create_issue(issue_text="Past issue.", days=-30)
        response = self.client.get(reverse('polls:index'))
	self.assertQuerysetEqual(
	    response.context['latest_issue_list'],
            ['<Issue: Past issue.>']
	)
	def test_index_view_with_a_future_question(self):
		"""
		Questions with a pub_date in the future should not be displayed on
		the index page.
		"""
		create_question(question_text="Future question.", days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])
		def test_index_view_with_future_question_and_past_question(self):
			"""
			Even if both past and future questions exist, only past questions
			should be displayed.
			"""
			create_question(question_text="Past question.", days=-30)
			create_question(question_text="Future question.", days=30)
			response = self.client.get(reverse('polls:index'))
			self.assertQuerysetEqual(
					response.context['latest_question_list'],
					['<Question: Past question.>']
					)
			def test_index_view_with_two_past_questions(self):
				"""
				The questions index page may display multiple questions.
				"""
				create_question(question_text="Past question 1.", days=-30)
				create_question(question_text="Past question 2.", days=-5)
				response = self.client.get(reverse('polls:index'))
				self.assertQuerysetEqual(
						response.context['latest_question_list'],
						['<Question: Past question 2.>', '<Question: Past question 1.>']
						)

