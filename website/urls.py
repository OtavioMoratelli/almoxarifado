from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('itens/', views.itens_emp, name='itens'),
    path('emprestimos/', views.emprestimos, name='emprestimos'),
    path('novo_emprestimo/', views.novoEmprestimo, name='novoEmprestimo'),

]
