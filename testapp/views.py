from django.shortcuts import render
from testapp.models import StudentModel

# Create your views here.
def home_view(request):
    return render(request,"home.html")


def age_view(request):
    print(request.COOKIES)
    if request.method=="POST":
        username=request.POST.get("name")
        if username:
            response=render(request,"age.html",{"name":username,})
            response.set_cookie("name",username)
            return response
        else:
            return render(request,"home.html",{"error":"Name is Required"})
    else:
        return render(request,"home.html")

def course_view(request):
    if request.method == "POST":
        username = request.POST.get("name")
        age = int(request.POST.get("age"))
        if username and age:
            response = render(request, "course.html", {"name": username, "age": age})
            response.set_cookie("age", age)
            return response
        else:
            return render(request, "home.html", {"error": "Name and Age are Required"})
    else:
        return render(request, "home.html")


def final_course_view(request):
    if request.method == "POST":
        username = request.POST.get("name")
        age = int(request.POST.get("age"))
        course = request.POST.get("course")
        if username and age and course:
            student = StudentModel(name=username, age=age, course=course)
            student.save()
            print(StudentModel.objects.all())
            response = render(request, "result.html", {"name": username, "age": age, "course": course})
            response.set_cookie("course", course)
            return response
        else:
            return render(request, "home.html", {"error": "All fields are required."})
    else:
        return render(request, "home.html")


def result_view(request):
    username = request.COOKIES.get("name")
    age = request.COOKIES.get("age")
    course = request.COOKIES.get("course")
    if not all([username, age, course]):
        return render(request, "home.html", {"error": "Incomplete data. Please fill out the form again."})
    return render(request, "result.html", {"name": username, "age": age, "course": course})