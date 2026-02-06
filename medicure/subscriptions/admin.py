from django.contrib import admin
from .models import Subscription, PaymentHistory

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'status', 'payment_status', 'end_date')
    list_filter = ('plan', 'status', 'payment_status')
    search_fields = ('user__username', 'razorpay_order_id')

@admin.register(PaymentHistory)
class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('subscription', 'amount', 'status', 'payment_date')
