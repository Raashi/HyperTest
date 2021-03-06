from django.db import models
from django.utils.translation import ugettext as _

from hypertest.user.models import VKUser


class GenderChoices(models.IntegerChoices):
    ANY = 0, 'Any'
    MALE = 1, 'Male'
    FEMALE = 2, 'Female'


class Test(models.Model):
    title = models.CharField(_('Title'), max_length=127)
    description = models.CharField(_('Description'), max_length=255, blank=True, null=True)
    picture = models.ImageField(_('Picture'), blank=True, null=True, upload_to='tests')

    published = models.BooleanField(_('Published'), default=False)
    vip = models.BooleanField(_('VIP'), default=False)
    price = models.IntegerField(_('Price'), default=0)
    gender = models.IntegerField(_('For gender'), choices=GenderChoices.choices, default=GenderChoices.ANY)

    user = models.ForeignKey(VKUser, on_delete=models.SET_NULL, related_name='tests', verbose_name=_('Creator'),
                             blank=True, null=True)

    passed_count = models.IntegerField(_('Passed count'), default=0)

    publish_date = models.DateTimeField(_('Publish date'), null=True)
    creation_date = models.DateTimeField(_('Creation date'), auto_now_add=True)
    modification_date = models.DateTimeField(_('Modification date'), auto_now=True)

    class Meta:
        db_table = 'test'
        verbose_name = _('Test')
        verbose_name_plural = _('Tests')
        # ordering = ['-id']

    def __str__(self):
        return self.title


class Result(models.Model):
    result_id = models.IntegerField(_('Result ID'))
    test = models.ForeignKey(verbose_name=_('Test'), to=Test, on_delete=models.CASCADE, related_name='results')
    text = models.CharField(_('Text'), max_length=255)
    description = models.CharField(_('Description'), max_length=255, blank=True, null=True)
    picture = models.ImageField(_('Picture'), blank=True, null=True, upload_to='tests-results')

    class Meta:
        db_table = 'test_result'
        verbose_name = _('Test result')
        verbose_name_plural = _('Test results')

        unique_together = [['result_id', 'test']]

    def __str__(self):
        return f'{self.result_id}: {self.text} ({self.test.title})'


class Question(models.Model):
    question_id = models.IntegerField(_('Question ID'))
    test = models.ForeignKey(verbose_name=_('Test'), to=Test, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(_('Text'), max_length=255)
    picture = models.ImageField(_('Picture'), blank=True, null=True, upload_to='tests-questions')

    class Meta:
        db_table = 'test_question'
        verbose_name = _('Test question')
        verbose_name_plural = _('Test questions')

        unique_together = [['question_id', 'test']]

    def __str__(self):
        return f'{self.question_id}: {self.text} ({self.test.title})'


class Answer(models.Model):
    answer_id = models.IntegerField(_('Question Answer ID'))
    question = models.ForeignKey(verbose_name=_('Question'), to=Question, related_name='answers',
                                 on_delete=models.CASCADE)
    result = models.ForeignKey(verbose_name=_('Result'), to=Result, related_name='answers',
                               on_delete=models.SET_NULL, blank=True, null=True)
    text = models.CharField(_('Text'), max_length=255)

    class Meta:
        db_table = 'test_question_answer'
        verbose_name = _('Test question answer')
        verbose_name_plural = _('Test question answers')

        unique_together = [['answer_id', 'question']]

    def __str__(self):
        return f'{self.answer_id}: {self.text} ({self.question.text})'


class TestPass(models.Model):
    test = models.ForeignKey(verbose_name=_('Test'), to=Test, related_name='passes', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name=_('VK User'), to=VKUser, related_name='tests_passed', on_delete=models.CASCADE)
    date = models.DateTimeField(_('Pass date'), auto_now=True)

    class Meta:
        db_table = 'test_pass'
        verbose_name = _('Test pass')
        verbose_name_plural = _('Tests\' passes')

        constraints = [
            models.UniqueConstraint(fields=['test', 'user'], name='test_pass_unique_idx')
        ]

    def __str__(self):
        return f'User: {self.user.id}, test: {self.test.title} ({self.test.id})'
