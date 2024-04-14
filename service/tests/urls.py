from django.urls import path
from .views import test_view, start_test, result_test

urlpatterns = [
    path('tests/<int:set_id>/<int:test_id>/', test_view, name='test_detail'),
    path('main_tests/', start_test, name='main_tests'),
    path('results/<int:set_id>,', result_test, name='result_tests'),
]
