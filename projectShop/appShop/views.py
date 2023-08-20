from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)


@api_view(['POST'])
def add_category(request):
    item = CategorySerializer(data=request.data)
 
    # validating for already existing data
    if Category.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_category(request):
	
	
	# checking for the parameters from the URL
	if request.query_params:
		items = Category.objects.filter(**request.query_params.dict())
	else:
		items = Category.objects.all()

	# if there is something in items else raise error
	if items:
		serializer = CategorySerializer(items, many=True)
		return Response(serializer.data)
	else:
		return Response('status=status.HTTP_404_NOT_FOUND')



@api_view(['POST'])
def update_category(request, pk):
    item = Category.objects.get(pk=pk)
    data = CategorySerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_category(request, pk):
    item = get_object_or_404(Category, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)