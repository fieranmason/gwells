#from gwells.forms.admin.SurveyForm import SurveyForm
#from django.views.generic.edit import FormView
#from django.urls import reverse
#from django.views.generic.edit import CreateView, UpdateView, DeleteView

#class SurveyView(FormView):
#    template_name = 'survey_form.html'
#    form_class = SurveyForm
#    success_url = reverse('site_admin')

#    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
#        print('validating survey form')
#        return True

#    def get_context_data(self, **kwargs):
#        """
#        Return the context for the page.
#        """
#        context = super(SurveyView, self).get_context_data(**kwargs)
#        return context

#class SurveyCreate(CreateView):
#    model = Survey
#    fields = ['name']

#class SurveyUpdate(UpdateView):
#    model = Survey
#    fields = ['name']

#class SuvreyDelete(DeleteView):
#    model = Survey
