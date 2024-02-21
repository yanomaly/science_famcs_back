from rest_framework import serializers
from storage.models import File
from storage.models import Categories, Subjects


subjects = [ (subject, str(Subjects[subject])) for subject in Subjects._member_names_ ]
categories = [ (category, str(Categories[category])) for category in Categories._member_names_ ]


class SearchSerializer(serializers.Serializer):
    subject = serializers.ChoiceField(choices=subjects, required=False)
    name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    author = serializers.CharField(max_length=100, required=False, allow_blank=True)
    categories = serializers.MultipleChoiceField(choices=categories, required=False)