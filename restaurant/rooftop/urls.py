from django.conf.urls import url
from rooftop.views import about,contact,menu,gallery,review
urlpatterns=[
    url(r'^about/$',about, name="about"),
    url(r'^contact/$',contact, name="contact"),
    url(r'^menu/$',menu, name="menu"),
    url(r'^gallery/$',gallery, name="gallery"),
    url(r'^review/$',review, name="review"),
   # url(r'^allreview/$',allreview, name="allreview"),

    

]