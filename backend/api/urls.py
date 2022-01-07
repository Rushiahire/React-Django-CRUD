from django.urls import path
from . import views



urlpatterns=[
    path('',views.Home.as_view(),name='home'),
    path('add',views.NewTask.as_view(),name='newtask'),
    path('viewlist',views.TaskList.as_view(),name='viewlist'),
    path('detail/<str:key>',views.DetailView.as_view(),name='detailview'),
    path('delete/<str:key>',views.DeleteTask.as_view(),name='deletetask'),
    path('update/<str:key>',views.UpdateTask.as_view(),name='update')
]