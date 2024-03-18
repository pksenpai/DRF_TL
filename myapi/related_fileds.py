from rest_framework import serializers


class FullNameRelatedField(serializers.RelatedField): # Custom related filed
    def to_representation(self, value): # value is related obj
        return f"{value.first_name} {value.last_name}"

