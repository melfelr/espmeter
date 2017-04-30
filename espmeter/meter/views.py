from django.views.generic.base import TemplateView

from meter.models import Sensor

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['sensors'] = Sensor.objects.all()
        return context