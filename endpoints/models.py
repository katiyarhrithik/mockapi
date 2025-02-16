from django.db import models
from django.utils.translation import gettext_lazy as _
from mockapi.models import CreatedTimestampMixin, UpdatedTimestampMixin


class RequestMethod(models.TextChoices):
	ANY = "ANY", _("Any")
	GET = "GET", _("Get")
	POST = "POST", _("Post")
	PUT = "PUT", _("Put")
	PATCH = "PATCH", _("Patch")
	DELETE = "DELETE", _("Delete")

class ResponseType(models.TextChoices):
    TEXT = "TEXT", _("Text/Html")
    JSON = "JSON", _("Json")

class Endpoint(CreatedTimestampMixin, UpdatedTimestampMixin):
	endpoint = models.CharField(max_length=50, unique=True, null=False)
	method = models.CharField(max_length=10, choices=RequestMethod)
	response = models.TextField()
	response_type = models.CharField(max_length=5, choices=ResponseType)
	status_code = models.IntegerField(default=200)

class EndpointUsage(CreatedTimestampMixin):
	endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)
	method = models.CharField(max_length=10, choices=RequestMethod)

