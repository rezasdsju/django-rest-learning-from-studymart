"""
URL configuration for djangorest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.urls import include, path

from drapi import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('aiinfo/', views.aiquest_info),
    # path('aiinfo/<int:pk>', views.aiquest_ins),
    # path('aicreate/', views.aiquest_create, name='aicreate'),
    # path('aicreate/<int:pk>', views.aiquest_create, name='aicreate'),
    # path('aicreate/', views.AiquestCreate.as_view(), name='aicreate'),
    # path('aicreate/<int:pk>', views.AiquestCreate.as_view(), name='aicreate'),
    # path('ailist/', views.AiquestList.as_view(), name='ailist'),
    # path('aicreate/', views.AiquestCreate.as_view(), name='aicreate'),
    #path('ailistcreate/', views.Aiquest_List_Create.as_view()),
    #path('airetrieve/', views.AiquestRetrieve.as_view()),
    #path('airetupdes/<int:pk>', views.Aiquest_Retrieve_Update_Destroy.as_view()),
    # path('aiupdate/<int:pk>', views.AiquestUpdate.as_view()),
    # path('aidestroy/<int:pk>', views.AiquestDestroy.as_view()),
    
    path('aiquest/', views.Aiquest_List_Create.as_view()),
    path('aiquest/<int:pk>', views.Aiquest_Retrieve_Update_Destroy.as_view()),
    
]
