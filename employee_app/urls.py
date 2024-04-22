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
    path('employee/notification/', employee_notification,name='notificationEmployee'),
    path('employee/lease/', employee_leaseviewFunction ,name='buildingportfolio'),
    path('employee/projects/', employee_projects,name='projects'),
    path('employee/reporting/', employee_reporting,name='systemreporting'),
    path('employee/municipal/', employee_municipal,name='municipalServices'),
    path('employee/court/', employee_court,name='newcourt'),
    path('employee/renovations/', employee_renovations,name='renovationsnew'),
    path('employee/project/budget/', employee_projectbudget,name='projectBudget'),
    path('employee/reports/', employee_systempeporting,name='reportingInfa'),
    path('employee/new/building/', employee_newbuilding,name='newBuilding'),
    path('employee/AUMP/', employee_aump,name='aumpservice'),
    path('employee/Jform/', employee_jform,name='jformBuilding'),
    path('employee/accomodation/', employee_accomodation,name='accomodationservice'),
    path('employee/tresury/', employee_tresury,name='systetresury'),
    path('employee/infrastructure/', employee_infrastructure,name='infrastructureProjects'),
    path('employee/standard/', employee_standardform,name='standard'),
    path('employee/ITC/', employee_itc,name='itc'),
    path('employee/security/', employee_security,name='security'),
    path('employee/application/', employee_leaseapplication,name='leaseapplication'),
    path('employee/active/', employee_leaseactive,name='leaseactive'),
    path('employee/Adjusting/', employee_leaseadjust,name='adjusting'),

    path('employee/state/', employee_statebuilding,name='stateowened'),
    
    path('employee/private/', employee_privatelease,name='privatelease'),
    
    path('employee/templates/', employee_memotemplates,name='memotemplates'),
    
    path('employee/security/', employee_securityform,name='securityform'),
    path('employee/national/', employee_nationalincident,name='nationalincident'),
    
    
    
]