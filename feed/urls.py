from django.conf.urls import url
# from django.contrib import admin
from feed import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^feedback$', views.FeedbackFormView.as_view()),
]
