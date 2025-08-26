from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("",views.main,name="main"),
    path("services",views.services,name="services"),
    path("portfolio",views.portfolio,name="portfolio"),
    path("contact",views.contact,name="contact"),
    path("login",views.customlogin,name="login"),
    path("signup",views.signup,name="signup"),
    path("reset",views.reset,name="reset"),
    path("abtad",views.abtad,name="abtad"),
    path("abtman",views.abtman,name="abtman"),
    path("abtcust",views.abtcust,name="abtcust"),
    path("subscribe",views.subscribe,name="subscribe"),
 
]
