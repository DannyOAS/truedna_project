from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('pricing/', views.pricing, name='pricing'),
    path('faq/', views.faq, name='faq'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('order/peace-of-mind/', views.order_peace_of_mind, name='order_peace_of_mind'),
    path('order/legal-dna/', views.order_legal_dna, name='order_legal_dna'),
    path('order/<str:kit_type>/', views.order, name='order'),
    path('order/submit/', views.submit_order, name='submit_order'),
]
