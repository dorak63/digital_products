from django.urls import path

from subscriptions.views import PackageView, SubscriptionView

urlpatterns = [
    path('packages/', PackageView.as_view()),
    path('subscription/', SubscriptionView.as_view())
]