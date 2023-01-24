from api.models import User, Operation, Record
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['balance', 'id', 'password', 'status', 'username']


class OperationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Operation
    fields = ['cost', 'id', 'type']


class RecordSerializer(serializers.ModelSerializer):
  class Meta:
    model = Record
    fields = ['amount', 'date', 'deleted', 'id', 'operation_id', 'operation_response', 'user_balance', 'user_id']

