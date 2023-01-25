import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import math

# def check_balance()
#   Get the user's current balance.
#   This will be used to ensure that the user has enough
#   credit to perform an operation. HTTP status 402 will
#   be returned if the user does not have credit available.

@api_view(['POST'])
def add(request):
  if request.method == 'POST':
    operands = [int(num) for num in request.data["operands"]]
    result = sum(operands)
    return Response(data=result, status=status.HTTP_200_OK)

@api_view(['POST'])
def divide(request):
  if request.method == 'POST':
    operands = [int(num) for num in request.data["operands"]]
    result = operands[0]
    for i in range(1, len(operands)):
      result = result / operands[i]
    return Response(content_type="application/json", data=result, status=status.HTTP_200_OK)

@api_view(['POST'])
def multiply(request):
  if request.method == 'POST':
    operands = [int(num) for num in request.data["operands"]]
    result = operands[0]
    for i in range(1, len(operands)):
      result = result * operands[i]
    return Response(data=result, status=status.HTTP_200_OK)

@api_view(['GET'])
def random_string(request):
  if request.method == 'GET':
    result = requests.get('https://www.random.org/strings/?num=1&len=20&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new')
    return Response(data=result.text, status=status.HTTP_200_OK)

@api_view(['POST'])
def square_root(request):
  if request.method == 'POST':
    operand = int(request.data["operands"][0])
    result = math.sqrt(operand)
    return Response(data=result, status=status.HTTP_200_OK)

@api_view(['POST'])
def subtract(request):
  if request.method == 'POST':
    operands = [int(num) for num in request.data["operands"]]
    result = operands[0]
    for i in range(1, len(operands)):
      result = result - operands[i]
    return Response(data=result, status=status.HTTP_200_OK)

