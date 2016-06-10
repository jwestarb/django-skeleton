from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

home = HomeView.as_view()