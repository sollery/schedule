from django.shortcuts import render
from django.db import models
from django.shortcuts import render
from .models import Mark,Student,Lesson,Subject
from django.db.models import Avg


def main_show(request):
    return render(request,'schedule_students/main.html')


def put_marks(request, lesson_id):
    error = ''
    if request.method == 'POST':
        for stud_id in request.POST:
            try:
                int(stud_id)
            except:
                continue
            if int(request.POST[stud_id]) > 0:
                temp = Mark(value=request.POST[stud_id], student_id=stud_id, lesson_id=lesson_id)
                temp.save()

    students = Student.objects.all()
    marks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    content = {'students': students, 'marks': marks,'error': error}
    return render(request, 'schedule_students/students.html', content)


def schedule_show(request):
    lesson_tb = Lesson.objects.all()
    content = {'lesson_tb': lesson_tb}
    return render(request, 'schedule_students/lessons.html', content)


def performance_show(request):
    student_rating = Student.objects.annotate(total=Avg('mark__value')).values('id','name', 'total').order_by('-total')
    empty = 'нет оценок'
    content = {'student_rating': student_rating, 'empty': empty}
    return render(request,'schedule_students/performance.html',content,)


def performance_stud_show(request,stud_id):
    student = Student.objects.filter(id=stud_id)
    mark = Mark.objects.filter(student=stud_id)
    empty = 'У этого студента еще нет оценок'
    content = {'student': student,'mark': mark, 'empty': empty}
    return render(request, 'schedule_students/performance_stud_show.html', content)

