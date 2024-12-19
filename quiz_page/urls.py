from django.urls import path,re_path


from . import views


urlpatterns = [
    path("",views.starting_page,name="starting_page"),
    path("login",views.login_user,name="login_user"),
    path("student_dash_board",views.student_dashboard,name="dashboard"),
    path("logout_user",views.logout_user,name="logout"),
    path("register_user",views.register_user,name="register"),
    path('quiz',views.quiz,name="quiz"),
    path('result',views.result,name="result")
]