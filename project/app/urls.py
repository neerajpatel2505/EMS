from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homePageView,name='home'),
    path('uregister/',views.userRegistrationView,name='uregistration'),
    path('insert/',views.insertUserDataBase,name='userinsert'),
    path('userloginpage/',views.userLoginPage,name='userloginpage'),
    path('ulogin/',views.uLogin,name='ulogin'),
    #========================================================================
    path('aregister/',views.adminRegistrationView,name='aregistration'),
    path('admininsert/',views.insertAdminDataBase,name='admininsert'),
    path('adminloginpage/',views.adminLoginPage,name='adminloginpage'),
    path('alogin/',views.aLogin,name='alogin'),
    #========================================================================
    path('enquiry/',views.enquiryView,name='enquiry'),
    path('enquiryinsert/',views.insertEnquiryDataBase,name='enquiryinsert'),
    #========================================================================
    path('showpage/',views.showPage,name='showpage'),
    path('editpage/<int:pk>/',views.EditPage,name='editpage'),
    path('update/<int:pk>/',views.UpdateData,name='update'),
    path('delete/<int:pk>/',views.DeleteData,name='delete'),
    #=======================For API Use=================================================
    path('user_data/<int:pk>/',views.user_details_pk,name='user_data'),
    path('user_list/',views.user_details_list,name='user_data'),
    path('admin_data/<int:pk>/',views.admin_details_pk,name='admin_data'),
    path('admin_list/',views.admin_details_list,name='admin_data'),
    path('enquiry_data/<int:pk>/',views.enquiry_details_pk,name='enquiry_data'),
    path('enquiry_list/',views.enquiry_details_list,name='enquiry_data'),
    ]