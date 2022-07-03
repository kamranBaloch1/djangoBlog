

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("blogPost/<str:slug>",views.blogPost,name="blogPost"),
    path("postComment",views.postComment,name="postComment"),
    path('contact/',views.contact,name="contact"),
    path('privacy-policy/',views.privacyPolicy,name="privacyPolicy"),
    path('login/',views.loginUser,name="login"),
    path('signup/',views.signupUser,name="signup"),
    path('logout/',views.logoutUser,name="logout"),
    path('allblogs/',views.allblogs,name="allblogs"),
    path('category/<str:cat>',views.category,name="category"),
    path('search/',views.search,name="search")
]
