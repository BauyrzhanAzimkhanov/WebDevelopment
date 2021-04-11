from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

    if(request.method == 'GET'):
        return JsonResponse(company.to_json())
    elif(request.method == 'PUT'):
        data = json.loads(request.body)
        company.name = data['name']
        company.save()
        return JsonResponse(company.to_json())
    elif(request.method == 'DELETE'):
        company.delete()
        return JsonResponse({'message': 'deleted'}, status = 204)

@csrf_exempt
def get_companies(request):
    if(request.method == 'GET'):
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe = False)
    elif(request.method == 'POST'):
        data = json.loads(request.body)
        try:
            company = Company.objects.create(name = data['name'])
        except Exception as e:
            return JsonResponse({'message': str(e)})
        return JsonResponse(company.to_json())

@csrf_exempt
def get_company_vacancies(request, id):
    if(request.method == 'GET'):
        try:
            company = Company.objects.get(id=id)
            vacansies = Vacancy.objects.filter(company__in=[company])
            vacancies_json = [vacancy.to_json() for vacancy in vacansies]
        except Exception as e:
            return JsonResponse({'message': str(e)})
        return JsonResponse(list(vacancies_json), safe = False)

@csrf_exempt
def get_vacancy(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)
    if(request.method == 'GET'):
        return JsonResponse(vacancy.to_json())
    elif(request.method == 'PUT'):
        data = json.loads(request.body)
        vacancy.name = data['name']
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif(request.method == 'DELETE'):
        vacancy.delete()
        return JsonResponse({'message': 'deleted'}, status = 204)

@csrf_exempt
def get_vacancies(request):
    if(request.method == 'GET'):
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe = False)
    elif(request.method == 'POST'):
        data = json.loads(request.body)
        try:
            vacancy = Vacancy.objects.create(name = data['name'])
        except Exception as e:
            return JsonResponse({'message': str(e)})
        return JsonResponse(vacancy.to_json())

@csrf_exempt
def get_top_ten_vacancies(request):
    if(request.method == 'GET'):
        try:
            vacancies = Vacancy.objects.all().order_by('-salary')[:10]
            vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        except Exception as e:
            return JsonResponse({'message': str(e)})
        return JsonResponse(vacancies_json, safe = False)