from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    name  = request.GET['name']
    age  = int(request.GET['age'])
    weight = float(request.GET['weight'])
    height = float(request.GET['height'])
    bmi = round(weight/(height**2))

    if (bmi < 18.5):
        result = "underweight"

    elif ( bmi >= 18.5 and bmi < 24.9):
        result = "Healthy"

    elif ( bmi >= 24.9 and bmi < 30):
        result = "overweight"

    elif ( bmi >=30):
        result = "Suffering from Obesity"

    params = {'age':age, 'height':height, 'weight':weight, 'bmi':bmi, 'name':name, 'result':result}
    return render(request, 'result.html', params)
