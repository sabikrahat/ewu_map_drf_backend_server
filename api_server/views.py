import joblib
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST'])
def check(request):
    response_data = {'status': True, 'message': 'Connected Successfully...!', 'data': None, }
    if request.method == 'GET':
        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        return Response(response_data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def point_detect(request):
    if request.method == 'GET':

        response_data = {
            'status': True,
            'message': 'Point Detect Function executed without any data...!',
            'data': None
        }

        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            r1 = request.data['r1']
            r2 = request.data['r2']
            r3 = request.data['r3']

            print('\n\n=============================================')
            print('================ Point Get ==================')
            print('=============================================')
            print('=========== ' + str(r1) + ' === ' + str(r2) + ' === ' + str(r3) + ' =============')


            loaded_model = joblib.load('static/wifi.joblib') 
            pred = loaded_model.predict([[r1, r2, r3]]) 
            
            print('=============================================')
            print('=============== Predict Get =================')
            print('=============================================')
            print('==================== ' + str(pred[0]) + ' ====================\n\n')

            response_data = {
                "success": True,
                "message": "Successfully solved the equation for the given data...!",
                "data": pred[0]
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:

            response_data = {
                "success": False,
                "message": "Error: " + str(e),
                "data": None
            }

            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


# {
#     "r1": -46,
#     "r2": -65,
#     "r3": -57
# }