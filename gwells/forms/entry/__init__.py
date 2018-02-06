from gwells.forms.entry.ActivitySubmissionCommentForm import ActivitySubmissionCommentForm
from gwells.forms.entry.ActivitySubmissionDevelopmentForm import ActivitySubmissionDevelopmentForm
from gwells.forms.entry.ActivitySubmissionFilterPackForm import ActivitySubmissionFilterPackForm
from gwells.forms.entry.ActivitySubmissionGpsForm import ActivitySubmissionGpsForm
from gwells.forms.entry.ActivitySubmissionLocationForm import ActivitySubmissionLocationForm
from gwells.forms.entry.ActivitySubmissionScreenIntakeForm import ActivitySubmissionScreenIntakeForm
from gwells.forms.entry.ActivitySubmissionSurfaceSealForm import ActivitySubmissionSurfaceSealForm
from gwells.forms.entry.ActivitySubmissionTypeAndClassForm import ActivitySubmissionTypeAndClassForm
from gwells.forms.entry.ActivitySubmissionWaterQualityForm import ActivitySubmissionWaterQualityForm
from gwells.forms.entry.CasingForm import CasingForm
from gwells.forms.entry.LinerPerforationForm import LinerPerforationForm
from gwells.forms.entry.LithologyForm import LithologyForm
from gwells.forms.entry.ProductionDataForm import ProductionDataForm
from gwells.forms.entry.ScreenForm import ScreenForm
from gwells.forms.entry.WellCompletionForm import WellCompletionForm
from gwells.forms.entry.WellOwnerForm import WellOwnerForm

from gwells.models import *

from django import forms
from django.forms.models import inlineformset_factory

ActivitySubmissionLithologyFormSet = inlineformset_factory(ActivitySubmission, LithologyDescription, form=LithologyForm, fk_name='activity_submission', can_delete=False, extra=10)
ActivitySubmissionCasingFormSet = inlineformset_factory(ActivitySubmission, Casing, form=CasingForm, fk_name='activity_submission', can_delete=False, extra=5)
ActivitySubmissionLinerPerforationFormSet = inlineformset_factory(ActivitySubmission, LinerPerforation, form=LinerPerforationForm, fk_name='activity_submission', can_delete=False, extra=5)
ActivitySubmissionScreenFormSet = inlineformset_factory(ActivitySubmission, Screen, form=ScreenForm, fk_name='activity_submission', can_delete=False, extra=5)
ProductionDataFormSet = inlineformset_factory(ActivitySubmission, ProductionData, form=ProductionDataForm, fk_name='activity_submission', can_delete=True, min_num=1, max_num=1)

__all__ = ['ActivitySubmissionCasingFormSet',
           'ActivitySubmissionCommentForm',
           'ActivitySubmissionDevelopmentForm',
           'ActivitySubmissionLinerPerforationFormSet',
           'ActivitySubmissionGpsForm',
           'ActivitySubmissionFilterPackForm',
           'ActivitySubmissionLithologyFormSet',
           'ActivitySubmissionLocationForm',
           'ActivitySubmissionScreenFormSet',
           'ActivitySubmissionScreenIntakeForm',
           'ActivitySubmissionSurfaceSealForm',
           'ActivitySubmissionTypeAndClassForm',
           'ActivitySubmissionWaterQualityForm',
           'CasingForm',
           'LinerPerforationForm',
           'LithologyForm',
           'ProductionDataForm',
           'ProductionDataFormSet',
           'ScreenForm',
           'WellCompletionForm',
           'WellOwnerForm']
