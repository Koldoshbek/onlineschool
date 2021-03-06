# Generated by Django 3.0.3 on 2020-05-05 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=50)),
                ('no_of_ques', models.CharField(max_length=20)),
                ('total_marks', models.CharField(max_length=20)),
                ('type_of_exam', models.CharField(choices=[('1', 'Math'), ('2', 'Art'), ('3', 'Music'), ('4', 'Computer')], max_length=5)),
                ('type_of_class', models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth')], max_length=5)),
                ('time_duration', models.DurationField(default='00:00:00')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField(default=0)),
                ('question', models.TextField(max_length=500)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.CharField(choices=[('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4')], max_length=1)),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineexamination.Exams')),
            ],
        ),
    ]
