from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import CSVImportForm,EmployeeForm
from django.http import HttpResponseRedirect
from.models import Employee
import csv
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def upload_view(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            csv_file = request.FILES['companies_sorted'].read().decode('utf-8').splitlines()
            print(csv_file)
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                print(row)
                Employee.objects.create(

                    keyword = row['keyword'],
                    name = row['name'],
                    domain = row['domain'],
                    year_founded = row['year_founded'],
                    industry = row['industry'],
                    size_range = row['size_range'],
                    locality = row['locality'],
                    country = row['country'],
                    cme =row['cme'],
                    tme = row['tme']
                )
            return HttpResponseRedirect("/")
    else:
        form = CSVImportForm()

    return render(request, "upload.html", {"form": form
    })

def Query_builder(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = EmployeeForm()

    return render(request, "Query_builder.html", {"form": form
                                           })
