
import os
from rest_framework import routers
from django.http import JsonResponse
from django.urls import path
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

def api_root(request):
	codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
	base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
	endpoints = {
		"users": base_url + "users/",
		"teams": base_url + "teams/",
		"activities": base_url + "activities/",
		"leaderboard": base_url + "leaderboard/",
		"workouts": base_url + "workouts/",
	}
	return JsonResponse(endpoints)

urlpatterns = [
	path('', api_root),
] + router.urls
