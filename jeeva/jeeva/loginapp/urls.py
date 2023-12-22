from django.urls import path
from loginapp import views

urlpatterns = [
    path('',views.indexPage,name="indexpage"),
    path('indexPage',views.indexPage,name="indexpage"),
    path('agi',views.getAllAgricultures,name="getAllAgricultures"),
    path('edu',views.getAllEducations,name="getAllEducations"),
    path('food',views.getAllFoodandhealths,name="getAllFoodandhealths"),
    path('enter',views.getAllSmallenterprises,name="getAllSmallenterprises"),
    path('vehi',views.getAllVehicles,name="getAllAgricultures"),
    

    path('add',views.addUser,name="addUser"),
    path('login_api',views.login_api,name="login_api"),
    
    path('LoginSignUpPage',views.LoginSignUpPage,name="LoginSignUpPage"),
    path('agriculturePage',views.agriculturePage,name="agriculturePage"),
    path('enterprisePage',views.enterprisePage,name="enterprisePage"),
    path('educationPage',views.educationPage,name="educationPage"),
    path('healthPage',views.healthPage,name="healthPage"),
    
    path('borrowPage',views.borrowPage,name="borrowPage"),
    path('aboutUsPage',views.aboutUsPage,name="aboutUsPage"),
    path('jeevaworkPage',views.jeevaworkPage,name="jeevaworkPage"),
    path('impactPage',views.impactPage,name="impactPage"),
    path('pressPage',views.pressPage,name="pressPage"),
    path('borrow',views.borrow,name="borrow"),

    



    
]