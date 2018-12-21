"""live_nasa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from api.views import detail_view
from api.views import create_comment
from api.views import comment_list
from api.views import pick_date

urlpatterns = [
    path('admin/', admin.site.urls),
    # Create
    path('nasa/comment/', create_comment),
    # Details about Comment - TextField
    path('nasa/comment/detail/<int:nasa_id>', detail_view),
    # List all Commments
    path('nasa/allcomments/', comment_list),
    # Date-picker
    path('nasa/date_picker/', pick_date),



    # date picker is html
    # <input type = date, id = nasa_data
    #search for button
]
