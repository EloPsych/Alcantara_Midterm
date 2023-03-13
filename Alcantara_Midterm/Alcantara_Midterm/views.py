from django.shortcuts import render
from django.http import HttpResponse

def Midterm_A(request):
    job1 = "Reporting Executive"
    job2 = "Business Analyst"
    job3 = "Data Analyst"
    job4 = "Statistician"
    job5 = "Data Scientist"
    job6 = "Data Engineer/Data Architect"
    job7 = "Machine Learning Engineer"
    job8 = "Big Data Engineer"

    return HttpResponse (job1, job2, job3, job4, job5, job6, job7, job8)

