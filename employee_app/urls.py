from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from employee_app.views import *

app_name = 'employee_app'

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
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
    path('employee/notification/', employee_notification,name='notificationEmployee'),
    path('lease/', employee_leaseviewFunction ,name='buildingportfolio'),
    path('projects/', employee_projects,name='projects'),
    path('reporting/', employee_reporting,name='systemreporting'),
    path('employee/municipal/', employee_municipal,name='municipalServices'),
    path('employee/court/', employee_court,name='newcourt'),
    path('employee/renovations/', employee_renovations,name='renovationsnew'),
    path('employee/project/budget/', employee_projectbudget,name='projectBudget'),
    path('employee/reports/', employee_systempeporting,name='reportingInfa'),
    path('employee/new/building/', employee_newbuilding,name='newBuilding'),
    path('employee/AUMP/', employee_aump,name='aumpservice'),
]