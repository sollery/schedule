from django.test import TestCase, Client
from .models import *
import random


class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Student.objects.create(name='Захаров И. Д.')
        Student.objects.create(name='Сошников А. В.')
        Student.objects.create(name='Абрамов А. Д.')
        Student.objects.create(name='Сидоров А. И.')
        Student.objects.create(name='Солдатов М. В.')
        Subject.objects.create(title='SQL', teacher='Бутусов Д. Ю.')
        Lesson.objects.create(date='2022-05-08', subject_id=1)

    def test_student(self):
        stud = Student.objects.get(pk=1)
        self.assertEqual(stud.name, 'Захаров И. Д.')

    def test_get_count_students(self):
        stud = Student.objects.all()
        self.assertEqual(stud.count(), 5)

    def test_order_students(self):
        students = Student.objects.all().order_by('name')
        self.assertEqual(students[0].name, 'Абрамов А. Д.')

    def test_client(self):
        student = Student.objects.all()[0]
        marks = [i for i in range(1, 12)]
        mark_val = random.choice(marks)
        les = Lesson.objects.all()[0]
        client = Client()
        client.post(f'/lesson/{str(les.id)}/', {str(student.id): str(mark_val)})
        mark = Mark.objects.get(student_id=student.id, lesson_id=les.id)
        self.assertEqual(mark.value, mark_val)
















































































































# Create your tests here.
