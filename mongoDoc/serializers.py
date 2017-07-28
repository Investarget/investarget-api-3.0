from rest_framework_mongoengine.serializers import DynamicDocumentSerializer, DocumentSerializer, EmbeddedDocumentSerializer

from mongoDoc.models import WXContentData, GroupEmailData


class WXContentDataSerializer(DocumentSerializer):
    class Meta:
        model = WXContentData
        fields = '__all__'

class GroupEmailDataSerializer(DocumentSerializer):
    class Meta:
        model = GroupEmailData
        fields = '__all__'