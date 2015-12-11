from django.views.generic import TemplateView

class GreenIndexView(TemplateView):
	template_name = "green.html"