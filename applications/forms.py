from __future__ import unicode_literals
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from crispy_forms.bootstrap import FormActions
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse
from django.forms import Form, ModelForm, ChoiceField, FileField, CharField, Textarea

from accounts.models import Organisation
from .models import Application, Referral, Condition, Compliance, Vessel


User = get_user_model()


class BaseFormHelper(FormHelper):
    form_class = 'form-horizontal'
    label_class = 'col-xs-12 col-sm-4 col-md-3 col-lg-2'
    field_class = 'col-xs-12 col-sm-8 col-md-6 col-lg-4'


class ApplicationCreateForm(ModelForm):
    class Meta:
        model = Application
        fields = ['app_type', 'organisation']

    def __init__(self, *args, **kwargs):
        # User must be passed in as a kwarg.
        user = kwargs.pop('user')
        super(ApplicationCreateForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper()
        self.helper.form_id = 'id_form_create_application'
        self.helper.attrs = {'novalidate': ''}
        self.helper.add_input(Submit('save', 'Save', css_class='btn-lg'))
        self.helper.add_input(Submit('cancel', 'Cancel'))
        # Limit the organisation queryset.
        self.fields['organisation'].queryset = Organisation.objects.filter(delegates__in=[user.emailuserprofile])
        self.fields['organisation'].help_text = '''The company or organisation
            on whose behalf you are applying (leave blank if not applicable).'''

        # Add labels for fields
        self.fields['app_type'].label = "Application Type"


class ApplicationLicencePermitForm(ModelForm):
    class Meta:
        model = Application
        fields = ['title', 'description',
            'proposed_commence', 'proposed_end', 'cost', 'project_no', 'related_permits', 'over_water',
            'purpose', 'max_participants', 'proposed_location', 'address', 'vessels',
            'jetties', 'jetty_dot_approval', 'jetty_dot_approval_expiry',
            'drop_off_pick_up', 'food', 'beverage', 'byo_alcohol', 'sullage_disposal', 'waste_disposal',
            'refuel_location_method', 'berth_location', 'anchorage', 'operating_details',
            'cert_survey', 'cert_public_liability_insurance', 'risk_mgmt_plan', 'safety_mgmt_procedures',
            'brochures_itineries_adverts', 'other_supporting_docs', 'land_owner_consent', 'deed']

    def __init__(self, *args, **kwargs):
        super(ApplicationLicencePermitForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper()
        self.helper.form_id = 'id_form_update_licence_permit'
        self.helper.attrs = {'novalidate': ''}
        self.helper.add_input(Submit('save', 'Save', css_class='btn-lg'))
        self.helper.add_input(Submit('cancel', 'Cancel'))

        # Add labels for fields
        self.fields['description'].label = "Proposed Commercial Acts or Activities"
        self.fields['project_no'].label = "Riverbank Project Number"
        self.fields['purpose'].label = "Purpose of Approval"
        self.fields['proposed_commence'].label = "Proposed Commencement Date"
        self.fields['proposed_end'].label = "Proposed End Date"
        self.fields['max_participants'].label = "Maximum Number of Participants"
        self.fields['address'].label = "Address of any landbased component of the commercial activity"
        self.fields['proposed_location'].label = "Location / Route and Acces Points"
        self.fields['jetties'].label = "List all jetties to be used"
        self.fields['jetty_dot_approval'].label = "Do you have approval to use Departmen of Transport service jetties?"
        self.fields['drop_off_pick_up'].label = "List all drop off and pick up points"
        self.fields['food'].label = "Food to be served?"
        self.fields['beverage'].label = "Beverage to be served?"
        self.fields['byo_alcohol'].label = "Do you allow BYO alcohol?"
        self.fields['sullage_disposal'].label = "Details of sullage disposal method"
        self.fields['waste_disposal'].label = "Details of waste disposal method"
        self.fields['refuel_location_method'].label = "Location and method of refueling"
        self.fields['anchorage'].label = "List all anchorage areas"
        self.fields['operating_details'].label = "Hours and days of operation including length of tours / lessons"
        self.fields['cert_survey'].label = "Certificate of Survey"
        self.fields['cert_public_liability_insurance'].label = "Public Liability Insurance Certificate"
        self.fields['risk_mgmt_plan'].label = "Risk managment Plan (if available)"
        self.fields['safety_mgmt_procedures'].label = "Safety Management Procedures (if available)"
        self.fields['brochures_itineries_adverts'].label = "Brocures, itineraries or advertisements (if available)"
        self.fields['other_supporting_docs'].label = "Other relevant supporting documentation (if available)"

        # TODO: all document fields.


class ApplicationPermitForm(ModelForm):
    class Meta:
        model = Application
        fields = ['title', 'description',
            'proposed_commence', 'proposed_end', 'cost', 'project_no', 'related_permits', 'over_water',
            'documents', 'other_supporting_docs', 'land_owner_consent', 'deed']

    def __init__(self, *args, **kwargs):
        super(ApplicationPermitForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper()
        self.helper.form_id = 'id_form_update_permit'
        self.helper.attrs = {'novalidate': ''}
        self.helper.add_input(Submit('save', 'Save', css_class='btn-lg'))
        self.helper.add_input(Submit('cancel', 'Cancel'))

        # Add labels and help text for fields
        self.fields['proposed_commence'].label = "Proposed commencement date"
        self.fields['proposed_commence'].help_text = "(Please consider routine assessment takes approximately 4 - 6 weeks, and set your commencement date accordingly)"
        self.fields['proposed_end'].label = "Proposed end date"
        self.fields['cost'].label = "Approximate cost"
        self.fields['project_no'].label = "Riverbank project number (if applicable)"
        self.fields['related_permits'].label = "Details of related permits"
        self.fields['description'].label = "Description of works, acts or activities"
        self.fields['documents'].label = "Attach more detailed descripton, maps or plans"
        self.fields['other_supporting_docs'].label = "Attach supporting information to demonstrate compliance with relevant Trust policies"


class ApplicationPart5Form(ModelForm):
    class Meta:
        model = Application
        fields = ['title', 'description',
            'cost', 'project_no', 'documents', 'other_supporting_docs', 'land_owner_consent', 'deed',
            'river_reserve_lease', 'current_land_use']

    def __init__(self, *args, **kwargs):
        super(ApplicationPart5Form, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper()
        self.helper.form_id = 'id_form_update_part_5'
        self.helper.attrs = {'novalidate': ''}
        self.helper.add_input(Submit('save', 'Save', css_class='btn-lg'))
        self.helper.add_input(Submit('cancel', 'Cancel'))


class ApplicationLodgeForm(ModelForm):
    class Meta:
        model = Application
        fields = ['app_type', 'title', 'description', 'submit_date']

    def __init__(self, *args, **kwargs):
        super(ApplicationLodgeForm, self).__init__(*args, **kwargs)
        app = kwargs['instance']
        self.helper = BaseFormHelper(self)
        self.helper.form_id = 'id_form_lodge_application'
        self.helper.form_action = reverse('application_lodge', args=(app.pk,))
        # Disable all form fields.
        for k, v in self.fields.items():
            self.fields[k].disabled = True
        # Define the form layout.
        self.helper.layout = Layout(
            HTML('<p>Confirm that this application should be lodged for assessment:</p>'),
            'app_type', 'title', 'description', 'submit_date',
            FormActions(
                Submit('lodge', 'Lodge', css_class='btn-lg'),
                Submit('cancel', 'Cancel')
            )
        )


class ReferralForm(ModelForm):
    class Meta:
        model = Referral
        fields = ['referee', 'period', 'details', 'documents']

    def __init__(self, *args, **kwargs):
        # Application must be passed in as a kwarg.
        app = kwargs.pop('application')
        super(ReferralForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper(self)
        self.helper.form_id = 'id_form_referral_create'
        self.helper.attrs = {'novalidate': ''}
        # Limit the referee queryset.
        referee = Group.objects.get_or_create(name='Referee')[0]
        existing_referees = app.referral_set.all().values_list('referee__email', flat=True)
        self.fields['referee'].queryset = User.objects.filter(groups__in=[referee]).exclude(email__in=existing_referees)
        # TODO: business logic to limit the document queryset.
        self.helper.form_id = 'id_form_refer_application'
        self.helper.add_input(Submit('save', 'Save', css_class='btn-lg'))
        self.helper.add_input(Submit('cancel', 'Cancel'))


class ReferralCompleteForm(ModelForm):
    class Meta:
        model = Referral
        fields = ['feedback']

    def __init__(self, *args, **kwargs):
        super(ReferralCompleteForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper(self)
        self.helper.form_id = 'id_form_referral_complete'
        self.helper.add_input(Submit('complete', 'Complete', css_class='btn-lg'))
        self.helper.add_input(Submit('cancel', 'Cancel'))


class ReferralRecallForm(ModelForm):
    class Meta:
        model = Referral
        exclude = ['effective_to', 'application', 'referee', 'details', 'sent_date', 'period', 'response_date', 'feedback', 'documents', 'status']

    def __init__(self, *args, **kwargs):
        super(ReferralRecallForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper(self)
        self.helper.form_id = 'id_form_referral_recall'
        self.helper.add_input(Submit('recall', 'Recall', css_class='btn-lg'))
        self.helper.add_input(Submit('cancel', 'Cancel'))


class ConditionCreateForm(ModelForm):
    class Meta:
        model = Condition
        fields = ['condition']

    def __init__(self, *args, **kwargs):
        super(ConditionCreateForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper(self)
        self.helper.attrs = {'novalidate': ''}
        self.fields['condition'].required = True
        self.helper.add_input(Submit('save', 'Save', css_class='btn-lg'))
        self.helper.add_input(Submit('cancel', 'Cancel'))


class ConditionApplyForm(ModelForm):
    class Meta:
        model = Condition
        fields = ['condition']

    def __init__(self, *args, **kwargs):
        super(ConditionApplyForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper(self)
        self.helper.form_id = 'id_form_condition_apply'
        self.helper.add_input(Submit('apply', 'Apply', css_class='btn-lg'))
        self.helper.add_input(Submit('cancel', 'Cancel'))


class AssignCustomerForm(ModelForm):
    """A form for assigning an application back to the customer.
    """
    feedback = CharField(
        required=False, widget=Textarea, help_text='Feedback to be provided to the customer.')

    class Meta:
        model = Application
        fields = ['app_type', 'title', 'description']

    def __init__(self, *args, **kwargs):
        super(AssignCustomerForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper(self)
        self.helper.form_id = 'id_form_assign_application'
        self.helper.attrs = {'novalidate': ''}
        # Disable all form fields.
        for k, v in self.fields.items():
            self.fields[k].disabled = True
        # Re-enable the feedback field.
        self.fields['feedback'].disabled = False
        # Define the form layout.
        self.helper.layout = Layout(
            HTML('<p>Reassign this application back to the applicant, with feedback:</p>'),
            'app_type', 'title', 'description', 'feedback',
            FormActions(
                Submit('assign', 'Assign', css_class='btn-lg'),
                Submit('cancel', 'Cancel')
            )
        )


class AssignProcessorForm(ModelForm):
    """A form for assigning a processor (admin officer) to an application.
    """
    class Meta:
        model = Application
        fields = ['app_type', 'title', 'description', 'submit_date', 'assignee']

    def __init__(self, *args, **kwargs):
        super(AssignProcessorForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper(self)
        self.helper.form_id = 'id_form_assign_application'
        self.helper.attrs = {'novalidate': ''}
        # Limit the assignee queryset.
        processor = Group.objects.get_or_create(name='Processor')[0]
        self.fields['assignee'].queryset = User.objects.filter(groups__in=[processor])
        self.fields['assignee'].required = True
        # Disable all form fields.
        for k, v in self.fields.items():
            self.fields[k].disabled = True
        # Re-enable the assignee field.
        self.fields['assignee'].disabled = False
        # Define the form layout.
        self.helper.layout = Layout(
            HTML('<p>Assign this application for processing:</p>'),
            'app_type', 'title', 'description', 'submit_date', 'assignee',
            FormActions(
                Submit('assign', 'Assign', css_class='btn-lg'),
                Submit('cancel', 'Cancel')
            )
        )


class AssignAssessorForm(ModelForm):
    """A form for assigning an assessor to an application.
    """
    class Meta:
        model = Application
        fields = ['app_type', 'title', 'description', 'submit_date', 'assignee']

    def __init__(self, *args, **kwargs):
        super(AssignAssessorForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper(self)
        self.helper.form_id = 'id_form_assign_application'
        self.helper.attrs = {'novalidate': ''}
        # Limit the assignee queryset.
        assessor = Group.objects.get_or_create(name='Assessor')[0]
        self.fields['assignee'].queryset = User.objects.filter(groups__in=[assessor])
        self.fields['assignee'].required = True
        # Disable all form fields.
        for k, v in self.fields.items():
            self.fields[k].disabled = True
        # Re-enable the assignee field.
        self.fields['assignee'].disabled = False
        # Define the form layout.
        self.helper.layout = Layout(
            HTML('<p>Assign this application for assessment:</p>'),
            'app_type', 'title', 'description', 'submit_date', 'assignee',
            FormActions(
                Submit('assign', 'Assign', css_class='btn-lg'),
                Submit('cancel', 'Cancel')
            )
        )


class AssignApproverForm(ModelForm):
    """A form for assigning a manager to approve an application.
    """
    class Meta:
        model = Application
        fields = ['app_type', 'title', 'description', 'submit_date', 'assignee']

    def __init__(self, *args, **kwargs):
        super(AssignApproverForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper(self)
        self.helper.form_id = 'id_form_approve_application'
        self.helper.attrs = {'novalidate': ''}
        # Limit the assignee queryset.
        approver = Group.objects.get_or_create(name='Approver')[0]
        self.fields['assignee'].queryset = User.objects.filter(groups__in=[approver])
        self.fields['assignee'].required = True
        self.fields['assignee'].label = 'Manager'
        # Disable all form fields.
        for k, v in self.fields.items():
            self.fields[k].disabled = True
        # Re-enable the assignee field.
        self.fields['assignee'].disabled = False
        # Define the form layout.
        self.helper.layout = Layout(
            HTML('<p>Assign this application to a manager for approval/issue:</p>'),
            'app_type', 'title', 'description', 'submit_date', 'assignee',
            FormActions(
                Submit('assign', 'Assign', css_class='btn-lg'),
                Submit('cancel', 'Cancel')
            )
        )


class ApplicationIssueForm(ModelForm):
    assessment = ChoiceField(choices=[
        (None, '---------'),
        ('issue', 'Issue'),
        ('decline', 'Decline'),
        # TODO: Return to assessor option.
        #('return', 'Return to assessor'),
    ])

    class Meta:
        model = Application
        fields = ['app_type', 'title', 'description', 'submit_date']

    def __init__(self, *args, **kwargs):
        super(ApplicationIssueForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper(self)
        self.helper.form_id = 'id_form_application_issue'
        self.helper.attrs = {'novalidate': ''}
        # Disable all form fields.
        for k, v in self.fields.items():
            self.fields[k].disabled = True
        # Re-enable the assessment field.
        self.fields['assessment'].disabled = False
        # Define the form layout.
        self.helper.layout = Layout(
            HTML('<p>Issue or decline this completed application:</p>'),
            'app_type', 'title', 'description', 'submit_date', 'assessment',
            FormActions(
                Submit('save', 'Save', css_class='btn-lg'),
                Submit('cancel', 'Cancel')
            )
        )


class ComplianceCreateForm(ModelForm):
    supporting_document = FileField(required=False, max_length=128)

    class Meta:
        model = Compliance
        fields = ['condition', 'compliance', 'supporting_document']

    def __init__(self, *args, **kwargs):
        # Application must be passed in as a kwarg.
        application = kwargs.pop('application')
        super(ComplianceCreateForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper(self)
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.fields['condition'].queryset = Condition.objects.filter(application=application)


class VesselCreateForm(ModelForm):
    class Meta:
        model = Vessel
        fields = ['vessel_type', 'name', 'vessel_id', 'registration', 'size', 'engine',
            'passenger_capacity']

    def __init__(self, *args, **kwargs):
        # User must be passed in as a kwarg.
        super(VesselCreateForm, self).__init__(*args, **kwargs)
        self.helper = BaseFormHelper()
        self.helper.form_id = 'id_form_create_vessel'
        self.helper.attrs = {'novalidate': ''}
        self.helper.add_input(Submit('save', 'Save', css_class='btn-lg'))
        self.helper.add_input(Submit('cancel', 'Cancel'))
