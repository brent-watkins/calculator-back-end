import math
import requests
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

# def check_balance()
#   Get the user's current balance.
#   This will be used to ensure that the user has enough
#   credit to perform an operation. HTTP status 402 will
#   be returned if the user does not have credit available.

@api_view(['POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def add(request):
  if request.method == 'POST':
    try:
      operands = [float(num) for num in request.data["operands"]]
      result = sum(operands)
      return Response(data=result, status=status.HTTP_200_OK)
    except ValueError:
      return Response(data="Operands must be numbers", status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(data="Invalid request", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def divide(request):
  if request.method == 'POST':
    try:
      operands = [float(num) for num in request.data["operands"]]
      result = operands[0]
      for i in range(1, len(operands)):
        result = result / operands[i]
      return Response(data=result, status=status.HTTP_200_OK)
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
      user = User.objects.filter(username=credentials["username"], password=credentials["password"])
      if len(user) == 1:
        serializer = UserSerializer(user[0])
        # Set the user status as User.ACTIVE
        return Response(data=serializer.data["username"], status=status.HTTP_200_OK)
      else:
        return Response(data="Incorrect username or password", status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(data="Invalid log in", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
  if request.method == 'POST':
    try:
      credentials = request.data
      user = User.objects.filter(username=credentials["username"])
      if len(user) == 1:
        serializer = UserSerializer(user[0])
        # Set the user status as User.INACTIVE
        return Response(data=serializer.data["username"], status=status.HTTP_200_OK)
      else:
        return Response(data="Could not log out of requested account", status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(data="An error occurred while attempting to log out", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def multiply(request):
  if request.method == 'POST':
    try:
      operands = [float(num) for num in request.data["operands"]]
      result = operands[0]
      for i in range(1, len(operands)):
        result = result * operands[i]
      return Response(data=result, status=status.HTTP_200_OK)
    except ValueError:
      return Response(data="Operands must be numbers", status=status.HTTP_400_BAD_REQUEST)
    except IndexError:
      return Response(data="You must send at least one operand", status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(data="Invalid request", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def random_string(request):
  if request.method == 'GET':
    result = requests.get('https://www.random.org/strings/?num=1&len=20&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new')
    return Response(data=result.text, status=status.HTTP_200_OK)

@api_view(['PUT'])
def register(request):
  if request.method == 'PUT':
    try:
      credentials = request.data
      serializer = UserSerializer(data=credentials)
      if serializer.is_valid():
        serializer.save()
        return Response(data="Account created", status=status.HTTP_200_OK)
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
      operand = float(request.data["operands"][0])
      result = math.sqrt(operand)
      return Response(data=result, status=status.HTTP_200_OK)
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
      operands = [float(num) for num in request.data["operands"]]
      result = operands[0]
      for i in range(1, len(operands)):
        result = result - operands[i]
      return Response(data=result, status=status.HTTP_200_OK)
    except ValueError:
      return Response(data="Operands must be numbers", status=status.HTTP_400_BAD_REQUEST)
    except IndexError:
      return Response(data="You must send at least one operand", status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(data="Invalid request", status=status.HTTP_400_BAD_REQUEST)

