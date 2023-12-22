import json
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse


from .models import agriculture,education,foodandhealth,smallenterprise,vehicles,borrower,volunteer
from .models import BorrowModel
# Create your views here.

# def getAllagricultures(request):
#     agi_list=agriculture.objects.all()
#     return agi_list



def getAllAgricultures(request):
    all_agi=agriculture.objects.all()
    serialized_agi = serialize('json', all_agi)
    parsed_agi = json.loads(serialized_agi)

    return JsonResponse({'all_agi': parsed_agi}, safe=False)

def getAllEducations(request):
    all_edu=education.objects.all()
    serialized_edu = serialize('json', all_edu)
    parsed_edu = json.loads(serialized_edu)

    return JsonResponse({'all_edu': parsed_edu}, safe=False)

def getAllFoodandhealths(request):
    all_food=foodandhealth.objects.all()
    serialized_food = serialize('json', all_food)
    parsed_food = json.loads(serialized_food)

    return JsonResponse({'all_food': parsed_food}, safe=False)

def getAllSmallenterprises(request):
    all_enter=smallenterprise.objects.all()
    serialized_enter= serialize('json', all_enter)
    parsed_enter= json.loads(serialized_enter)

    return JsonResponse({'all_enter': parsed_enter}, safe=False)

def getAllVehicles(request):
    all_vehi=vehicles.objects.all()
    serialized_vehi= serialize('json', all_vehi)
    parsed_vehi = json.loads(serialized_vehi)

    return JsonResponse({'all_vehi': parsed_vehi}, safe=False)




def addUser(request):
    if request.method == 'POST':
        u_name=request.POST['user_name']
        u_email=request.POST['user_email']
        u_password=request.POST['user_password']
        u_phone=request.POST['user_phone']

        query=volunteer(volunteer_name=u_name,volunteer_email=u_email,volunteer_password=u_password,volunteer_phone=u_phone)
        query.save()
        
    return render(request,'index.html')


def login_api(request):

    if request.method=='POST':
        flag=0
        login_email=request.POST['login_email']
        login_password=request.POST['login_password']
        
        allVolunteers=volunteer.objects.all()
        for eachVolunteer in allVolunteers:
            print(eachVolunteer.volunteer_email)
            print(eachVolunteer.volunteer_password)

            if eachVolunteer.volunteer_email==login_email and eachVolunteer.volunteer_password==login_password:
                flag=1
                break
    if flag==1:
        return render(request,'index.html')
    else:
        return HttpResponse ("user is not existing")
    
def indexPage(request):
    return render(request,'index.html')
    
# def home(request):
#     return render(request,'LoginSignUp.html')

def LoginSignUpPage(request):
    return render(request,'LoginSignUp.html')

def agriculturePage(request):
    return render(request,'agriculture.html')

def enterprisePage(request):
    return render(request,'enterprise.html')

def educationPage(request):
    return render(request,'education.html')

def healthPage(request):
    return render(request,'health.html')

def borrowPage(request):
    return render(request,'borrow.html')

def aboutUsPage(request):
    return render(request,'about.html')

def jeevaworkPage(request):
    return render(request,'jeevawork.html')

def impactPage(request):
    return render(request,'impact.html')

def pressPage(request):
    return render(request,'press.html')

def borrow(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        adhaar_number = request.POST.get('adhaar_number')
        category = request.POST.get('category')
        borrower_img = request.POST.get('borrower_img')
        # borrow_amount= request.POST.get('borrow_amount')
        description = request.POST.get('description')

        query = BorrowModel(
            full_name=full_name,
            gender=gender,
            age=age,
            adhaar_number=adhaar_number,
            category=category,
            borrower_img=borrower_img,
            # borrow_amount=borrow_amount,
            description=description
        )
        query.save()

        AllBorrowModel=BorrowModel.objects.all()

        context={
            'AllBorrowModel':AllBorrowModel
        }
        print(context)
        return render(request,'BorrowersCard.html',context)
    else:
        return HttpResponse("not success")

# def getAllBorrowModel(request):
#     AllBorrowModel=BorrowModel.objects.all()

#     context={
#         'AllBorrowModel':AllBorrowModel
#     }
#     print(context)
#     return render(request,'BorrowersCard.html',context)

    