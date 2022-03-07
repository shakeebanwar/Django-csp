from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "core/home_view.html"


class GoogleSlidesView(TemplateView):
    template_name = "core/google_slides_view.html"
