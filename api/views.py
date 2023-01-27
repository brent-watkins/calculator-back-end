import logging
import math
import requests
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User, Operation, Record
from .serializers import UserSerializer, OperationSerializer, RecordSerializer

def _create_record(operation, result, user):
  serialized_user = UserSerializer(user)
  serialized_operation = OperationSerializer(operation)
  record = RecordSerializer(data={"operation_id": serialized_operation.data["id"], "operation_response": result, "user_balance": serialized_user.data["balance"], "user_id": serialized_user.data["id"]})
  if record.is_valid():
    record.save()
  else:
    logging.error(record.errors)

@api_view(['POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def add(request):
  if request.method == 'POST':
    try:
      credentials = request.data
      user = User.objects.get(username=credentials["username"])
      operation = Operation(type=Operation.ADDITION)
      operation.save()
      if user.balance >= operation.cost:
        operands = [float(num) for num in request.data["operands"]]
        result = sum(operands)
        balance = user.balance
        cost = operation.cost
        new_balance = float(balance) - float(cost)
        updated_user = UserSerializer(user, data={"balance": new_balance}, partial=True)
        if updated_user.is_valid():
          updated_user.save()
        _create_record(operation, result, user)
        return Response(data=result, status=status.HTTP_200_OK)
      else:
        return Response(data="Insufficient balance", status=status.HTTP_402_PAYMENT_REQUIRED)
    except ValueError:
      return Response(data="Operands must be numbers", status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(data="Invalid request", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'PUT'])
def balance(request):
  if request.method == 'POST':
    try:
      credentials = request.data
      user = User.objects.get(username=credentials["username"])
      serialized_user = UserSerializer(user)
      return Response(data=serialized_user.data["balance"], status=status.HTTP_200_OK)
    except:
      return Response(data="Unable to show balance", status=status.HTTP_400_BAD_REQUEST)
  if request.method == 'PUT':
    try:
      credentials = request.data
      user = User.objects.get(username=credentials["username"])
      serialized_user = UserSerializer(user, data={"balance": credentials["balance"]}, partial=True)
      if serialized_user.is_valid():
        serialized_user.save()
        return Response(status=status.HTTP_200_OK)
      else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def divide(request):
  if request.method == 'POST':
    try:
      credentials = request.data
      user = User.objects.get(username=credentials["username"])
      operation = Operation(type=Operation.DIVISION)
      operation.save()
      if user.balance >= operation.cost:
        operands = [float(num) for num in request.data["operands"]]
        result = operands[0]
        for i in range(1, len(operands)):
          result = result / operands[i]
        balance = user.balance
        cost = operation.cost
        new_balance = float(balance) - float(cost)
        updated_user = UserSerializer(user, data={"balance": new_balance}, partial=True)
        if updated_user.is_valid():
          updated_user.save()
        _create_record(operation, result, user)
        return Response(data=result, status=status.HTTP_200_OK)
      else:
        return Response(data="Insufficient balance", status=status.HTTP_402_PAYMENT_REQUIRED)
    except ValueError:
      return Response(data="Operands must be numbers", status=status.HTTP_400_BAD_REQUEST)
    except IndexError:
      return Response(data="You must send at least one operand", status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(data="Invalid request", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
  if request.method == 'POST':
    try:
      credentials = request.data
      user = User.objects.get(username=credentials["username"], password=credentials["password"])
      # serialized_user = UserSerializer(user, data={"status", User.ACTIVE}, partial=True)
      # if serialized_user.is_valid():
      #   serialized_user.save()
      return Response(data=user.username, status=status.HTTP_200_OK)
    except:
      return Response(data="Log in attempt failed", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
  if request.method == 'POST':
    try:
      credentials = request.data
      user = User.objects.get(username=credentials["username"])
      # serialized_user = UserSerializer(user, data={"status", User.INACTIVE}, partial=True)
      # if serialized_user.is_valid():
      #   serialized_user.save()
      return Response(data=user.username, status=status.HTTP_200_OK)
    except:
      return Response(data="An error occurred while attempting to log out. You may still be logged in.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def multiply(request):
  if request.method == 'POST':
    try:
      credentials = request.data
      user = User.objects.get(username=credentials["username"])
      operation = Operation(type=Operation.MULTIPLICATION)
      operation.save()
      if user.balance >= operation.cost:
        operands = [float(num) for num in request.data["operands"]]
        result = operands[0]
        for i in range(1, len(operands)):
          result = result * operands[i]
        balance = user.balance
        cost = operation.cost
        new_balance = float(balance) - float(cost)
        updated_user = UserSerializer(user, data={"balance": new_balance}, partial=True)
        if updated_user.is_valid():
          updated_user.save()
        _create_record(operation, result, user)
        return Response(data=result, status=status.HTTP_200_OK)
      else:
        return Response(data="Insufficient balance", status=status.HTTP_402_PAYMENT_REQUIRED)      
    except ValueError:
      return Response(data="Operands must be numbers", status=status.HTTP_400_BAD_REQUEST)
    except IndexError:
      return Response(data="You must send at least one operand", status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(data="Invalid request", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def random_string(request):
  if request.method == 'POST':
    try:
      credentials = request.data
      user = User.objects.get(username=credentials["username"])
      operation = Operation(type=Operation.RANDOM_STRING)
      operation.save()
      if user.balance >= operation.cost:
        result = requests.get('https://www.random.org/strings/?num=1&len=20&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new')
        balance = user.balance
        cost = operation.cost
        new_balance = float(balance) - float(cost)
        updated_user = UserSerializer(user, data={"balance": new_balance}, partial=True)
        if updated_user.is_valid():
          updated_user.save()
        _create_record(operation, result, user)
        return Response(data=result.text, status=status.HTTP_200_OK)
      else:
        return Response(data="Insufficient balance", status=status.HTTP_402_PAYMENT_REQUIRED)
    except:
      return Response(data="Invalid request", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'PUT'])
def records(request):
  if request.method == 'POST':
    try:
      credentials = request.data
      user = User.objects.get(username=credentials["username"])
      records = Record.objects.filter(user_id=user)
      serialized_records = RecordSerializer(records, many=True)
      return Response(data={"records": serialized_records.data, "message": "Records retrieved"}, status=status.HTTP_200_OK)
    except:
      return Response(data={"records": [], "message": "Unable to retrieve records"}, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'PUT':
    try:
      credentials = request.data
      user = User.objects.get(username=credentials["username"])
      record = Record.objects.get(id=credentials["record"])
      serialized_record = RecordSerializer(record, data={"deleted": True}, partial=True)
      if serialized_record.is_valid():
        serialized_record.save()
        return Response(status=status.HTTP_200_OK)
      else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def register(request):
  if request.method == 'PUT':
    try:
      credentials = request.data
      serializer = UserSerializer(data=credentials)
      if serializer.is_valid():
        serializer.save()
        return Response(data="Account created", status=status.HTTP_201_CREATED)
      else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(data="Unable to register account", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def square_root(request):
  if request.method == 'POST':
    try:
      credentials = request.data
      user = User.objects.get(username=credentials["username"])
      operation = Operation(type=Operation.SQUARE_ROOT)
      operation.save()
      if user.balance >= operation.cost:
        operand = float(request.data["operands"][0])
        result = math.sqrt(operand)
        balance = user.balance
        cost = operation.cost
        new_balance = float(balance) - float(cost)
        updated_user = UserSerializer(user, data={"balance": new_balance}, partial=True)
        if updated_user.is_valid():
          updated_user.save()
        _create_record(operation, result, user)
        return Response(data=result, status=status.HTTP_200_OK)
      else:
        return Response(data="Insufficient balance", status=status.HTTP_402_PAYMENT_REQUIRED)      
    except IndexError:
      return Response(data="You must send at least one operand", status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(data="Operand must be a non-negative number", status=status.HTTP_400_BAD_REQUEST)    

@api_view(['POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def subtract(request):
  if request.method == 'POST':
    try:
      credentials = request.data
      user = User.objects.get(username=credentials["username"])
      operation = Operation(type=Operation.SUBTRACTION)
      operation.save()
      if user.balance >= operation.cost:
        operands = [float(num) for num in request.data["operands"]]
        result = operands[0]
        for i in range(1, len(operands)):
          result = result - operands[i]
        balance = user.balance
        cost = operation.cost
        new_balance = float(balance) - float(cost)
        updated_user = UserSerializer(user, data={"balance": new_balance}, partial=True)
        if updated_user.is_valid():
          updated_user.save()
        _create_record(operation, result, user)
        return Response(data=result, status=status.HTTP_200_OK)
      else:
        return Response(data="Insufficient balance", status=status.HTTP_402_PAYMENT_REQUIRED)      
    except ValueError:
      return Response(data="Operands must be numbers", status=status.HTTP_400_BAD_REQUEST)
    except IndexError:
      return Response(data="You must send at least one operand", status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(data="Invalid request", status=status.HTTP_400_BAD_REQUEST)

