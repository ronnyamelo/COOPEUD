import rest_framework_filters as filters
from loanrequest.models import LoanRequest, Applicant


class ApplicantFilter(filters.FilterSet):

    class Meta:
        model = Applicant
        fields = {
            'first_name': ['icontains', ],
            'last_name': ['icontains'],
            'id_number': ['icontains'],
        }


class LoanRequestFilter(filters.FilterSet):
    applicant = filters.RelatedFilter(ApplicantFilter, field_name='applicant', queryset=Applicant.objects.all())

    class Meta: 
        model = LoanRequest
        fields = {
            'status': ['exact'],
            'request_date': ['gte', 'lte'],
            'amount_requested': ['gte', 'lte']
        }

