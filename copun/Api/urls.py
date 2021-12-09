
from django.urls import path
from copun.Api.views import PutCopun,CopunAdd,CopunList

urlpatterns = [
    path('all_copun/', CopunList.as_view()),
    path('add/',CopunAdd.as_view()),
    path('put/<int:id>/',PutCopun.as_view()),
    path('delete/<int:id>/',PutCopun.as_view()),
]