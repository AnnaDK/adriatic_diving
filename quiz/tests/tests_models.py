from django.test import TestCase
from quiz.models import Quiz
# test if Quiz model is passing values correctly


class TestModels(TestCase):

    def test_quiz_model(self):
        quiz = Quiz.objects.create(
            name='quiz1',
            question='question',
            option_one='option_one',
            option_two='option_two',
            option_three='option_three',
            option_four='option_four',
            option_one_checkbox=False,
            option_two_checkbox=False,
            option_three_checkbox=False,
            option_four_checkbox=False,
            answer='answer'
        )
        quiz.save()
        self.assertEquals(quiz.name, 'quiz1')
        self.assertEquals(quiz.question, 'question')
        self.assertEquals(quiz.option_one, 'option_one')
        self.assertEquals(quiz.option_two, 'option_two')
        self.assertEquals(quiz.option_three, 'option_three')
        self.assertEquals(quiz.option_four, 'option_four')
        self.assertEquals(quiz.option_one_checkbox, False)
        self.assertEquals(quiz.option_two_checkbox, False)
        self.assertEquals(quiz.option_three_checkbox, False)
        self.assertEquals(quiz.option_four_checkbox, False)
        self.assertEquals(quiz.answer, 'answer')
