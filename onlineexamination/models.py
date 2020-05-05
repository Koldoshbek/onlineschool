from django.db import models


class Exams(models.Model):
    exam_name = models.CharField(max_length=50)
    no_of_ques = models.CharField(max_length=20)
    total_marks = models.CharField(max_length=20)
    choose_class = (('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'))
    choose_type = (('1', 'Math'), ('2', 'Art'), ('3', 'Music'), ('4', 'Computer'))
    type_of_exam = models.CharField(max_length=5, choices=choose_type)
    type_of_class = models.CharField(max_length=5, choices=choose_class)
    time_duration = models.DurationField(default='00:00:00')
    date = models.DateTimeField()

    def __str__(self):
        return str(self.exam_name)


class Question(models.Model):
    exam_name = models.ForeignKey(Exams, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField(default=0)
    question = models.TextField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    choose = (('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4'))
    answer = models.CharField(max_length=1, choices=choose)

    def __str__(self):
        return str(self.question)
