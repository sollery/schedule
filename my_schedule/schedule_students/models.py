from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from datetime import datetime


class Student(models.Model):
    name = models.CharField('Студент', max_length=100,
                            validators=[RegexValidator('[А-ЯЕа-яё]+\s[А-ЯЕа-яё]{1}\.\s*[А-ЯЕа-яё]{1}\.')])

    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Subject(models.Model):
    title = models.CharField('Название предмета', max_length=100)
    teacher = models.CharField('Преподаватель', max_length=100,
                               validators=[RegexValidator('[А-ЯЕа-яё]+\s[А-ЯЕа-яё]{1}\.\s*[А-ЯЕа-яё]{1}\.')])

    def __str__(self):
        return f'{self.title} {self.teacher}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Lesson(models.Model):
    date = models.DateField('Дата', default=timezone.now)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} - {self.subject}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'


class Mark(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.BigIntegerField('Оценка')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student.name} {self.lesson} {self.value}'


    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

# Create your models here.
