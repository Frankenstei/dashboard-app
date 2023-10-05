"""
URL configuration for dashboardAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Team/', views.TeamListCreateView.as_view(), name='Team-list'),
    path('Team/<int:pk>/', views.TeamRetrieveUpdateDestroyView.as_view(), name='Team-detail'),
    path('CustomerContacts/', views.CustomerContactsListCreateView.as_view(), name='CustomerContacts-list'),
    path('CustomerContacts/<int:pk>/', views.CustomerContactsRetrieveUpdateDestroyView.as_view(), name='CustomerContacts-detail'),
    path('dataInvoice/', views.dataInvoiceListCreateView.as_view(), name='dataInvoice-list'),
    path('dataInvoice/<int:pk>/', views.dataInvoiceRetrieveUpdateDestroyView.as_view(), name='dataInvoice-detail'),
    path('create-user/', views.UserCreateView.as_view(), name='create-user'),
]
