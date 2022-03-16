from django.shortcuts import render

# Create your views here.


#***********************developer***********************************************
def index(request):
    return render(request,'index.html')



#******************  Manager ******************************************

def manager_Dashboard(request):
    return render(request,'manager\manager_Dashboard.html')

def manager_dept(request):
    return render(request,'manager\manager_dept.html') 
def manager_emp_dept(request):
    return render(request,'manager\manager_emp_dept.html')   
def manager_projects(request):
    return render(request,'manager\manager_projects.html')
def manager_proj_list(request):
    return render(request,'manager\manager_proj_list.html')
def manager_proj_details(request):
    return render(request,'manager\manager_proj_details.html')
def manager_proj_manager(request):
    return render(request,'manager\manager_proj_manager.html')
def manager_proj_manager1(request):
    return render(request,'manager\manager_proj_manager1.html')
def manager_proj_manager2(request):
    return render(request,'manager\manager_proj_manager2.html')

def manager_completed_proj(request):
    return render(request,'manager\manager_completed_proj.html')
def manager_completed_proj_details(request):
    return render (request,'manager\manager_completed_proj_details.html')
def manager_completed_proj_manager(request):
    return render(request, 'manager\manager_completed_proj_manager.html')
def manager_completed_proj_manager_list(request):
    return render(request,'manager\manager_completed_proj_manager_list.html')
def manager_completed_proj_manager_tl(request):
    return render(request,'manager\manager_completed_proj_manager_tl.html')
def manager_emp_dept_list(request):
    return render(request,'manager\manager_emp_dept_list.html')
def manager_emp_dept_details(request):
    return render(request,'manager\manager_emp_dept_details.html')
def manager_emp_profile(request):
    return render(request,'manager\manager_emp_profile.html')
def manager_emp_involved_projects(request):
    return render(request,'manager\manager_emp_involved_projects.html')
def manager_emp_attendance(request):
    return render(request,'manager\manager_emp_attendance.html')

def manager_emp_attendance_show(request):
    return render(request,'manager\manager_emp_attendance_show.html')


def manager_upcoming(request):
    return render(request,'manager\manager_upcoming.html')

def manager_createproject(request):
    return render(request,'manager\manager_createproject.html')

def manager_upcoming_project(request):
    return render(request,'manager\manager_upcoming_project.html')

def manager_give_project(request):
    return render(request,'manager\manager_give_project.html')

def manager_accepted_project(request):
    return render(request,'manager\manager_accepted_project.html')

def manager_rejected_project(request):
    return render(request,'manager\manager_rejected_project.html')

def manager_task(request):
    return render(request,'manager\manager_task.html')

def manager_givetask(request):
    return render(request,'manager\manager_givetask.html')

def manager_current_task(request):
    return render(request,'manager\manager_current_task.html')

def manager_previous_task(request):
    return render(request,'manager\manager_previous_task.html')

def manager_registration_details(request):
    return render(request,'manager\manager_registration_details.html')  

def manager_new_department(request):
    return render(request,'manager\manager_new_department.html') 

def manager_create_department(request):
    return render(request,'manager\manager_create_department.html')

def manager_attendance(request):
    return render(request,'manager\manager_attendance.html') 

def manager_attendance_show(request):
    return render(request,'manager\manager_attendance_show.html')

def manager_reported_issues(request):
    return render(request,'manager\manager_reported_issues.html') 

def manager_issues(request):
    return render(request,'manager\manager_issues.html')

def manager_issues_form(request):
    return render(request,'manager\manager_issues_form.html')

def manager_myissues(request):
    return render(request,'manager\manager_myissues.html')


def manager_reported_detail(request):
    return render(request,'manager\manager_reported_detail.html')

def manager_reported_issue_show(request):
    return render(request,'manager\manager_reported_issue_show.html')



    
