from django.shortcuts import render

from joblib import load

models = load('./notebook/models.joblib')
# Create your views here.

def index(request):
    if request.method == 'POST':
        sepal_length = request.POST['sep_len']
        sepal_width = request.POST['sep_wid']
        petal_length = request.POST['pet_len']
        petal_width = request.POST['pet_wid']
        y_predict = models.predict([[float(sepal_length), float(sepal_width), float(petal_length), float(petal_width)]])
        if y_predict == 0:
            y_predict = 'Setosa'
        elif y_predict == 1:
            y_predict = 'Versicolor'
        else:
            y_predict = 'Virginica'
        return render(request, 'index.html', {'color_type':y_predict})
    return render(request, 'index.html') 
