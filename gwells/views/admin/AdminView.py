"""
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from django.views import generic
from django.forms import modelformset_factory
from django.forms import modelform_factory
from gwells.models.Survey import Survey

from django.contrib.auth.mixins import LoginRequiredMixin

class AdminView(LoginRequiredMixin, generic.TemplateView):
    context_object_name = 'context'
    template_name = 'gwells/site_admin.html'

    def get_context_data(self, **kwargs):
        """
        Return the context for the page.
        """

        context = super(AdminView, self).get_context_data(**kwargs)

        survey_form_set = modelformset_factory(Survey, fields=('survey_introduction_text','survey_link', 'survey_page', 'survey_enabled'), extra=0)

        survey_forms = survey_form_set(queryset=Survey.objects.all().order_by('-update_date'))
        survey_form = modelform_factory(Survey, fields=('survey_introduction_text', 'survey_link', 'survey_page', 'survey_enabled'))

        context['forms'] = survey_forms

        context['form'] = survey_form()
        return context
