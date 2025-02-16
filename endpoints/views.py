from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.views import View
from endpoints.models import Endpoint, EndpointUsage, ResponseType, RequestMethod
import json


class EndpointView(View):
	def get_response(self, request, endpoint_name):
		endpoint = Endpoint.objects.filter(endpoint=endpoint_name).first()
		if not endpoint:
			return HttpResponseNotFound()
		if endpoint.method != RequestMethod.ANY and request.method.upper() != endpoint.method:
			return HttpResponseNotAllowed(permitted_methods=[endpoint.method])
		EndpointUsage.objects.create(endpoint=endpoint, method=request.method.upper())
		if endpoint.response_type == ResponseType.JSON:
			return JsonResponse(json.loads(endpoint.response), status=endpoint.status_code, safe=False)
		return HttpResponse(endpoint.response, status=endpoint.status_code)

	def head(self, request, endpoint_name,  *args, **kwargs):
		return self.get_response(request, endpoint_name)

	def get(self, request, endpoint_name,  *args, **kwargs):
		return self.get_response(request, endpoint_name)

	def post(self, request, endpoint_name,  *args, **kwargs):
		return self.get_response(request, endpoint_name)

	def put(self, request, endpoint_name,  *args, **kwargs):
		return self.get_response(request, endpoint_name)

	def patch(self, request, endpoint_name,  *args, **kwargs):
		return self.get_response(request, endpoint_name)

	def delete(self, request, endpoint_name,  *args, **kwargs):
		return self.get_response(request, endpoint_name)

class EndpointUsageView(View):
	def get(self, request, endpoint_name,  *args, **kwargs):
		usages = EndpointUsage.objects.filter(endpoint__endpoint=endpoint_name)
		usage_data = list(usages.values("endpoint__endpoint", "method", "created_at"))
		return JsonResponse({"count": usages.count(), "usage": usage_data}, status=200)
