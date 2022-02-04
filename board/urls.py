from django.urls import URLPattern, path
from . import views

app_name = "board"
urlpatterns=[
    path('index/', views.index, name="index"),
    path('detail/<bpk>', views.detail, name="detail"),
    path('delete/<bpk>', views.delete, name="delete"),
    path('create/', views.create, name="create"),
    path('update/<bpk>', views.update, name="update"),
    path('createrep/<bpk>', views.createreply, name="createreply"),
    path('dreply/<bpk>/<rpk>',views.dreply,name="dreply"),
    path('likey/<bpk>', views.likey, name="likey"),
    path('unlikey/<bpk>', views.unlikey, name="unlikey")
]