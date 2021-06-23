from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import pymysql
import random
from json import dumps
from django.views.decorators.cache import cache_control

def index(request):
    return render(request, 'index.html')


def admitstudent(request):
    request.session['student_id'] = request.POST.get('student_id')
    request.session['student_name'] = request.POST.get('student_name')
    return redirect('/quiz')


def quiz(request):
    db = pymysql.connect(user="root",
                         host="localhost",
                         password="",
                         database="testpress")

    if (db):
        cursor = db.cursor()
        sql = "SELECT * FROM questions ORDER BY RAND () LIMIT 10"
        cursor.execute(sql)
        rows = cursor.fetchall()
        questions = []
        count=0
        for _ in rows:
            count+=1
            options = list(_[1:5])
            random.shuffle(options)
            questions.append({
                "question_number" : count,
                "question" : _[0],
                "answer": _[1],
                "options": [
                    options[0],
                    options[1],
                    options[2],
                    options[3]]
            })
        questions_json = dumps(questions)
        try:
            if request.session['student_id']:
                return render(request, 'quiz.html', {'data': questions_json})
        except:
            return redirect('/index')
def adminlogin(request):
        return render(request, 'adminlogin.html')

def adminauthenticate(request):
    if len(request.POST)>0:
        db=pymysql.connect(user="root",
                             host="localhost",
                             password="",
                             database="testpress")
        if(db):
            cursor = db.cursor()
            username=request.POST.get('username')
            password=request.POST.get('password')
            username2="SELECT * FROM user WHERE USERNAME='"+username+ "' AND PASSWORD ='"+password+"'"
            cursor.execute(username2)
            rows = cursor.fetchall()
            db.close()
            print(rows)
            if len(rows)>0:
                request.session['username'] = username
                return redirect('/admin_dashboard')
    else:
        return redirect('/admin_login')



def logout(request):
    try:
        del request.session['username']
        request.session.flush()
    except:
        pass
    return redirect('/admin_login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admindashboard(request):
    try:
        if request.session['username']:
            db = pymysql.connect(user="root",
                                 host="localhost",
                                 password="",
                                 database="testpress")
            if (db):
                cursor = db.cursor()
                sql = "SELECT * FROM questions"
                cursor.execute(sql)
                rows = cursor.fetchall()
                questions = []
                count = 0
                for _ in rows:
                    count += 1
                    options = list(_[1:5])
                    random.shuffle(options)
                    questions.append({
                        "question_number": count,
                        "question": _[0],
                        "answer": _[1],
                        "options": [
                            options[0],
                            options[1],
                            options[2],
                            options[3]]
                    })
                questions_json = dumps(questions)
                return render(request, 'dashboard.html',{"data":questions})
            else:
                return redirect('/admin_login')
    except:
        return redirect('/admin_login')


def addquestions(request):
    if len(request.POST)>0:
        db = pymysql.connect(user="root",
                             host="localhost",
                             password="",
                             database="testpress")
        question=request.POST.get('data[0][value]')
        answer=request.POST.get('data[1][value]')
        opt1=request.POST.get('data[2][value]')
        opt2=request.POST.get('data[3][value]')
        opt3=request.POST.get('data[4][value]')
        cursor = db.cursor()
        sql = "INSERT INTO QUESTIONS(QUESTION,CORRECT,OP1,OP2,OP3)VALUES('{0}','{1}','{2}','{3}','{4}')".format(question,answer,opt1,opt2,opt3)
        cursor.execute(sql)
        db.commit()
        db.close()
        return redirect('/admin_dashboard')
    else:
        return redirect('/admin_login')
