from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from employee_app.views import *

urlpatterns = [
    path('employee/', EmployeeApiView().as_view()),
    path('employee/<int:pk>/', Employee_ApiView.as_view()),

    path('employee/buildings/', employee_building_view,name='buildinginformationMap'),
    path('employee/buildings/<int:pk>/', employee_map_building_view, name='buildingDirectionInfor'),
    path('employee/buildings/report/', employee_reports_view, name='reportBuilding'),
    path('employee/report/<int:pk>/', employee_reports_information_view,name='buildingreportInformation'),
    path('employee/building/boardroom/', employee_boardrooms_view,name='boardroombuildings'),
    path('employee/booking/boardroom/<int:pk>/', employee_book_boardrooms_view, name='buildingboardroominformation'),
    path('employee/buildings/parking/', employee_parkings_view, name='parkingBuildings'),
    path('employee/booking/parking/<int:pk>/', employee_book_parkings_view,name='buildingsparkingbookingInfor'),
    path('employee/profile/', employee_profile,name='employeeprofile'),
    path('employee/notification/', employee_notification,name='notificationEmployee')
]

urlpatterns = format_suffix_patterns(urlpatterns)