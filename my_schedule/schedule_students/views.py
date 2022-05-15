from django.shortcuts import render
from django.db import models
from django.shortcuts import render
from .models import Mark,Student,Lesson,Subject
from django.db.models import Avg
from django.db.models import FilteredRelation, Q

def main_show(request):
    return render(request,'schedule_students/main.html')


def put_marks(request, lesson_id):
    print(request.POST)
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
    marks_stud = Mark.objects.filter(lesson_id=lesson_id)
    students_mark = dict(zip([(i.name, i.id) for i in students], [i.value for i in marks_stud]))
    for i in students:
        if (i.name, i.id) not in students_mark.keys():
            students_mark[i.name, i.id] = None
    print(students)
    print(marks_stud)
    print(students_mark)
    # marks_stud_1 = Student.objects.all(Q(mark__lesson_id=lesson_id) & Q(mark__isnull=True)).values('mark__value','name')
    # marks_stud = Student.objects.annotate(t=FilteredRelation('mark', condition=Q(mark__lesson_id=lesson_id),),).values('name', 'mark__value')
    marks = [i for i in range(0,13)]
    content = {'marks': marks,'students_mark': students_mark}
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

