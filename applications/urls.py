from django.conf.urls import url
from applications import views


urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home_page'),
    url(r'^applications/$', views.ApplicationList.as_view(), name='application_list'),
    url(r'^applications/apply/$', views.ApplicationApply.as_view(), name='application_apply'),
    url(r'^applications/create/$', views.ApplicationCreate.as_view(), name='application_create'),
    url(r'^applications/create-emergency-works/$', views.ApplicationCreateEW.as_view(), name='application_create_ew'),
    url(r'^applications/(?P<pk>\d+)/$', views.ApplicationDetail.as_view(), name='application_detail'),
    url(r'^applications/(?P<pk>\d+)/apply/(?P<action>\w+)/$', views.ApplicationApplyUpdate.as_view(), name='application_apply_form'),
    url(r'^applications/(?P<pk>\d+)/pdf/$', views.ApplicationDetailPDF.as_view(), name='application_detail_pdf'),
    url(r'^applications/(?P<pk>\d+)/actions/$', views.ApplicationActions.as_view(), name='application_actions'),
    url(r'^applications/(?P<pk>\d+)/comms/$', views.ApplicationComms.as_view(), name='application_comms'),
    url(r'^applications/(?P<pk>\d+)/comms-create/$', views.ApplicationCommsCreate.as_view(), name='application_comms_create'),
    url(r'^applications/(?P<pk>\d+)/update/$', views.ApplicationUpdate.as_view(), name='application_update'),
    url(r'^applications/(?P<pk>\d+)/lodge/$', views.ApplicationLodge.as_view(), name='application_lodge'),
    url(r'^applications/(?P<pk>\d+)/refer/$', views.ApplicationRefer.as_view(), name='application_refer'),
    url(r'^applications/(?P<pk>\d+)/create-condition/$', views.ConditionCreate.as_view(), name='condition_create'),
    url(r'^applications/(?P<pk>\d+)/assign-person/$', views.ApplicationAssignPerson.as_view(), name='application_assign_person'),
    url(r'^applications/(?P<pk>\d+)/assign-applicant/(?P<applicantid>\d+)/$', views.ApplicationAssignApplicant.as_view(), name='application_assign_applicant'),
    url(r'^applications/(?P<pk>\d+)/assign/(?P<action>\w+)/$', views.ApplicationAssign.as_view(), name='application_assign'),
    url(r'^applications/(?P<pk>\d+)/nextaction/(?P<action>\w+)/$', views.ApplicationAssignNextAction.as_view(), name='application_nextaction'),
    url(r'^applications/(?P<pk>\d+)/issue/$', views.ApplicationIssue.as_view(), name='application_issue'),
    url(r'^applications/(?P<pk>\d+)/create-compliance/$', views.ComplianceCreate.as_view(), name='compliance_create'),
    url(r'^applications/(?P<pk>\d+)/vessel/$', views.VesselCreate.as_view(), name='application_add_vessel'),
    url(r'^applications/(?P<pk>\d+)/newspaperpublication/$', views.NewsPaperPublicationCreate.as_view(), name='application_add_newspaperpublication'),
    url(r'^applications/(?P<pk>\d+)/changeapplicant/$', views.ApplicationApplicantChange.as_view(), name='applicant_change'),
    #   url(r'^applications/(?P<pk>\d+)/websitepublication/$', views.WebsitePublicationCreate.as_view(), name='application_add_websitepublication'),
    url(r'^applications/(?P<pk>\d+)/feedbackpublication/create/(?P<status>\w+)/$', views.FeedbackPublicationCreate.as_view(), name='application_add_feedbackpublication_draft'),
    url(r'^applications/(?P<application>\d+)/feedbackpublication/update/(?P<pk>\d+)/$', views.FeedbackPublicationUpdate.as_view(), name='application_update_feedbackpublication'),
    url(r'^applications/(?P<application>\d+)/feedbackpublication/delete/(?P<pk>\d+)/$', views.FeedbackPublicationDelete.as_view(), name='application_delete_feedbackpublication'),
    url(r'^applications/(?P<pk>\d+)/feedbackpublication/create/(?P<status>\w+)/$', views.FeedbackPublicationCreate.as_view(), name='application_add_feedbackpublication_final'),
    url(r'^applications/(?P<pk>\d+)/feedbackpublication/create/(?P<status>\w+)/$', views.FeedbackPublicationCreate.as_view(), name='application_add_feedbackpublication_determination'),
    url(r'^applications/(?P<pk>\d+)/webpublish/(?P<publish_type>\w+)/', views.WebPublish.as_view(), name='application_publish_documents'),
    url(r'^applications/(?P<approvalid>\d+)/change/(?P<action>\w+)/$', views.ApplicationChange.as_view(), name='application_change'),
    url(r'^emergency-works/$', views.EmergencyWorksList.as_view(), name='emergencyworks_list'),
    url(r'^referrals/(?P<pk>\d+)/complete/$', views.ReferralComplete.as_view(), name='referral_complete'),
    url(r'^referrals/(?P<pk>\d+)/recall/$', views.ReferralRecall.as_view(), name='referral_recall'),
    url(r'^referrals/(?P<pk>\d+)/resend/$', views.ReferralResend.as_view(), name='referral_resend'),
    url(r'^referrals/(?P<pk>\d+)/remind/$', views.ReferralRemind.as_view(), name='referral_remind'),
    url(r'^referrals/(?P<pk>\d+)/delete/$', views.ReferralDelete.as_view(), name='referral_delete'),
    url(r'^condition/(?P<pk>\d+)/update/$', views.ConditionUpdate.as_view(), name='condition_update'),
    url(r'^condition/(?P<pk>\d+)/update/(?P<action>\w+)/$', views.ConditionUpdate.as_view(), name='condition_update'),
    url(r'^condition/(?P<pk>\d+)/delete/$', views.ConditionDelete.as_view(), name='condition_delete'),
    url(r'^vessel/(?P<pk>\d+)/update/$', views.VesselUpdate.as_view(), name='vessel_update'),
    url(r'^vessel/(?P<pk>\d+)/delete/$', views.VesselDelete.as_view(), name='vessel_delete'),
    url(r'^newspaperpublication/(?P<pk>\d+)/update/', views.NewsPaperPublicationUpdate.as_view(), name='newspaperpublication_update'),
    url(r'^newspaperpublication/(?P<pk>\d+)/delete/', views.NewsPaperPublicationDelete.as_view(), name='newspaperpublication_delete'),
    url(r'^websitepublication/(?P<pk>\d+)/change/(?P<docid>\d+)/', views.WebsitePublicationChange.as_view(), name='websitepublication_change'),
    url(r'^compliances/$', views.ComplianceList.as_view(), name='compliance_list'),
    url(r'^records/create/$', views.RecordCreate.as_view(), name='document_create'),
    url(r'^records/$', views.RecordList.as_view(), name='document_list'),
    # URLs related to user account, address and organisation management.
    url(r'^account/$', views.UserAccount.as_view(), name='user_account'),
    url(r'^account/update/$', views.UserAccountUpdate.as_view(), name='user_account_update'),
    url(r'^account/address/create/(?P<type>\w+)/$', views.AddressCreate.as_view(), name='address_create'),
    url(r'^account/address/(?P<pk>\d+)/update/$', views.AddressUpdate.as_view(), name='address_update'),
    url(r'^organisations/$', views.OrganisationList.as_view(), name='organisation_list'),
    url(r'^organisations/create/$', views.OrganisationCreate.as_view(), name='organisation_create'),
    url(r'^organisations/(?P<pk>\d+)/$', views.OrganisationDetail.as_view(), name='organisation_detail'),
    url(r'^organisations/(?P<pk>\d+)/update/$', views.OrganisationUpdate.as_view(), name='organisation_update'),
    url(r'^organisations/(?P<pk>\d+)/address/create/(?P<type>\w+)/$', views.OrganisationAddressCreate.as_view(), name='organisation_address_create'),
    url(r'^organisations/(?P<pk>\d+)/request-delegate-access/$', views.RequestDelegateAccess.as_view(), name='request_delegate_access'),
    url(r'^organisations/(?P<pk>\d+)/confirm-delegate-access/(?P<uid>[0-9A-Za-z]+)-(?P<token>.+)/$', views.ConfirmDelegateAccess.as_view(), name='confirm_delegate_access'),
    url(r'^organisations/(?P<pk>\d+)/unlink-delegate/(?P<user_id>\w+)/$', views.UnlinkDelegate.as_view(), name='unlink_delegate'),
]
