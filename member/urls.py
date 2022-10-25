from django.urls import path
from .import views

urlpatterns = [
    path("",views.index, name="index"),
    path("member/<str:pk>",views.member, name="mem"),
    path("createMember/",views.createMember, name="addmember"),
    path("updateMember/<str:pk>",views.updateMember, name="updatemember"),
    path("deleteMember/<str:pk>",views.deleteMember, name="deletemember"),
    path("payment/",views.payment, name="payment"),
    path("deletePayment/<str:pk>",views.deletePayment, name="deletePayment"),
    path("updatePayment/<str:pk>",views.updatePayment, name="updatePayment"),
    path("tyr/",views.tyr, name="tyr")
]
