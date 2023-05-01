from django.urls import path

from new_app import views

urlpatterns = [
  path("indexx", views.indexx, name="indexx"),

  path("", views.join, name="join"),
  path('save_candidate', views.save_candidate, name='save_candidate'),

  path('education/', views.education, name='education'),

  path("view", views.view, name="view"),
  path('candidate/<int:candidate_id>/update/', views.update_candidate, name='update_candidate'),

  path("delete/<int:id>/", views.delete, name="delete"),

]
