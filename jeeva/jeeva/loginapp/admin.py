from django.contrib import admin
from .models import BorrowModel,borrower,volunteer,agriculture,education,foodandhealth,smallenterprise,vehicles,categories

# Register your models here.

# admin.site.register(donar)
admin.site.register(borrower)
admin.site.register(volunteer)
admin.site.register(agriculture)
admin.site.register(education)
admin.site.register(foodandhealth)
admin.site.register(smallenterprise)
admin.site.register(vehicles)
admin.site.register(categories)
admin.site.register(BorrowModel)
