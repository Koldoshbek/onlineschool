from django.contrib import admin
from .models import Question, Exams

admin.site.site_header = ""


class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ["question", "exam_name", "marks"]

    class Meta:
        model = Question


admin.site.register(Question, QuestionModelAdmin)


class ExamModelAdmin(admin.ModelAdmin):
    list_display = ["exam_name", "no_of_ques", "total_marks", "time_duration", "type_of_exam", "type_of_class", "date"]


admin.site.register(Exams, ExamModelAdmin)
