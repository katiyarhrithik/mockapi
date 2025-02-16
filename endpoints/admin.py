from django.contrib import admin
from endpoints.models import Endpoint, EndpointUsage


class EndpointAdmin(admin.ModelAdmin):
    list_display = ["endpoint", "method", "response_type", "status_code", "usage"]
    ordering = ["-id"]
    readonly_fields = ("created_at", "updated_at",)

    def usage(self, obj):
        return EndpointUsage.objects.filter(endpoint_id=obj.id).count()

class EndpointUsageAdmin(admin.ModelAdmin):
    list_display = ("endpoint_name", "endpoint_id", "method", "created_at",)
    ordering = ["-id"]
    readonly_fields = ("endpoint", "endpoint_name", "method", "created_at",)

    def endpoint_name(self, obj):
        return obj.endpoint.endpoint

admin.site.register(Endpoint, EndpointAdmin)
admin.site.register(EndpointUsage, EndpointUsageAdmin)
