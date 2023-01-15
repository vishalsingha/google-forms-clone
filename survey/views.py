from secrets import choice
from urllib import response
from django.shortcuts import HttpResponse, redirect, render
import json
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import *
import pandas as pd
import os
import csv
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    if request.user is not None:
        forms = Form.objects.all()

        data = {"forms":forms}
        try:
            myforms = Form.objects.filter(owner = request.user)
            data["myforms"] = myforms
        except:
            pass
        # print(list(forms))
    return render(request, 'home.html', data)

def survey(request):
    return render(request, "form.html")



@csrf_exempt
def save_survey(request):
    if request.method == 'POST':
        form_data = json.loads(request.body)
        data = form_data['surveydata']
        quepk_list = []
        for que in data:
            que_data = data.get(que)

            pk_list = []
            if que_data['que_type']=='1':
                options = que_data['options']
                for op in options:
                    if op:
                        ch = Choices(choice = op)
                        ch.save()
                        pk_list.append(ch.pk)

            que_obj = Questions(question = que_data['que_des'], question_type = que_data['que_type'], required = True)
            que_obj.save()
            quepk_list.append(que_obj.pk)
            que_obj.choices.add(*pk_list)

        # print(form_data["login_req"])
        frm = Form(title = form_data["form_title"], description = form_data["form_des"], login_required=form_data["login_req"] ,owner=request.user)
        frm.save()
        frm.owner = request.user
        frm.questions.add(*quepk_list)
        return render(request, "home.html")
    # print("hello again")
    return HttpResponse("dcbjkds")



@login_required
def show_form(request, key):
    form_data = Form.objects.get(pk=key)


    form_data_json = {
        "id" : form_data.pk,
        "title" : form_data.title,
        "description": form_data.description,
        "owner" : form_data.owner, 
        "login_required" : form_data.login_required, 
        "collect_email" : form_data.collect_email, 
        "created_at" : form_data.created_at, 
        "updated_at" : form_data.updated_at, 
        "questions": [que for que in form_data.questions.all()]

    }
    # print(form_data.owner)
    
    return render(request, "form_render.html", {"form_data":form_data_json})

def save_response(request, key):
    if request.method=="POST":
        ans_lst = []
        for que in request.POST:
            temp  = que.split("_")
            if len(temp)==3:
                qid = temp[-1]
                qfk = Questions.objects.get(pk = qid)
                ans = request.POST[que]
                ans_obj = Answer(answer = ans, answer_to = qfk)
                ans_obj.save()
                ans_lst.append(ans_obj)
        frm = Form.objects.get(pk = key)
        res = Responses(form_id = frm, responder_ip= 10, responder = request.user, responder_email = request.user.email)
        res.save()
        res.response.add(*ans_lst)

        messages.info(request, "Your Response has been  saved", extra_tags='success')

    return redirect('/')


def download_excel(request, key):

    frm = Form.objects.get(pk = key)
    all_response = Responses.objects.filter(form_id = frm)

    cols = ['user_email'] + [q.question for q in frm.questions.all()]


    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{frm.title}.csv"'
    writer = csv.writer(response)

    writer.writerow(cols)
    for res in all_response:
        user_name = res.responder_email
        user_res = [ans.answer for ans in res.response.all()]
        row = [user_name] + user_res
        print(row)
        writer.writerow(row)
    return response



