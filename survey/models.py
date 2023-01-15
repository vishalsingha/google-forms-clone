
from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


class Choices(models.Model):
    choice = models.CharField(max_length=5000)

# # Create your models here.
# class User_ABS(AbstractUser, models.Model):
#     email = models.EmailField(unique = True)
    

QUESTION_TYPES = (
    (1, "MCQs"),
    (2, "True / False"),
    (3, "Phone"),
    (4, "Location"),
    (5, "Date")
)

class Questions(models.Model):
    question = models.CharField(max_length= 10000)
    question_type = models.IntegerField(choices=QUESTION_TYPES)
    required = models.BooleanField(default= False)
    choices = models.ManyToManyField(Choices, related_name = "choices", blank = True)


class Form(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, blank = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "owner")
    sucess_message = models.CharField(max_length = 10000, default = "Your response has been recorded.")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    questions = models.ManyToManyField(Questions, related_name = "questions")
    collect_email = models.BooleanField(default=False)
    login_required = models.BooleanField(default = False)

    def __str__(self):
        return self.title

class Answer(models.Model):
    answer = models.CharField(max_length=5000)
    answer_to = models.ForeignKey(Questions, on_delete = models.CASCADE ,related_name = "answer_to")

class Responses(models.Model):
    form_id = models.ForeignKey(Form, on_delete = models.CASCADE, related_name = "form_id")
    responder_ip = models.CharField(max_length=30)
    responder = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "responder", blank = True, null = True)
    responder_email = models.EmailField(blank = True)
    response = models.ManyToManyField(Answer, related_name = "response")

    def __str__(self):
        return self.form_id.title

    









