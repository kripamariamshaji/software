
from django.urls import path
from app import views

urlpatterns = [
    
    path('index', views.index, name='index'),




    #***************************** Manager ******************************

    path('manager_Dashboard',views.manager_Dashboard), 
    path('manager_dept',views.manager_dept),
    path('manager_emp_dept',views.manager_emp_dept),  
    path('manager_projects',views.manager_projects), 
    path('manager_proj_list', views.manager_proj_list),
    path('manager_proj_details', views.manager_proj_details),
    path('manager_proj_manager', views.manager_proj_manager),
    path('manager_proj_manager1', views.manager_proj_manager1),
    path('manager_proj_manager2', views.manager_proj_manager2),
    path('manager_completed_proj', views.manager_completed_proj),
    path('manager_completed_proj_details', views.manager_completed_proj_details),
    path('manager_completed_proj_manager', views.manager_completed_proj_manager),
    path('manager_completed_proj_manager_list', views.manager_completed_proj_manager_list),
    path('manager_completed_proj_manager_tl', views.manager_completed_proj_manager_tl),
    path('manager_emp_dept_list', views.manager_emp_dept_list),
    path('manager_emp_dept_details', views.manager_emp_dept_details),
    path('manager_emp_profile', views.manager_emp_profile),
    path('manager_emp_involved_projects', views.manager_emp_involved_projects),
    path('manager_emp_attendance', views.manager_emp_attendance),
    path('manager_emp_attendance_show',views.manager_emp_attendance_show),

    path('manager_upcoming',views.manager_upcoming),
    path('manager_createproject',views.manager_createproject), 
    path('manager_upcoming_project',views.manager_upcoming_project),
    path('manager_give_project',views.manager_give_project),
    path('manager_accepted_project',views.manager_accepted_project),
    path('manager_rejected_project',views.manager_rejected_project),
    path('manager_task',views.manager_task),
    path('manager_givetask',views.manager_givetask),
    path('manager_current_task',views.manager_current_task),
    path('manager_previous_task',views.manager_previous_task),
    path('manager_registration_details',views.manager_registration_details), 
    path('manager_new_department',views.manager_new_department),
    path('manager_create_department',views.manager_create_department),
    path('manager_attendance',views.manager_attendance), 
    path('manager_attendance_show',views.manager_attendance_show),
    path('manager_reported_issues',views.manager_reported_issues),
    path('manager_issues',views.manager_issues),
    path('manager_issues_form',views.manager_issues_form),
    path('manager_myissues',views.manager_myissues),
    path('manager_reported_detail',views.manager_reported_detail),
    path('manager_reported_issue_show',views.manager_reported_issue_show),

    
    
]
