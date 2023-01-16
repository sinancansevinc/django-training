from rest_framework.urls import path
from . import views
urlpatterns = [
    path('',views.PlayersListView.as_view()),
    path('<int:pk>',views.PlayersMixinView.as_view(),name='player-detail'),
    path('<int:pk>/update',views.PlayersMixinView.as_view(),name='player-update'),
    path('<int:pk>/delete',views.PlayersMixinView.as_view(),name='player-delete')

]
