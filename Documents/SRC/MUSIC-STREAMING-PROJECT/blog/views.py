from django.shortcuts import render





def home_view(request):
    #print(request)
    # <WSGIRequest: GET '/add?data=maman+Ruth'>
    # this is what you pass in the browser the request contain that 
    template_name = 'blog/index.html'
    return render(request, template_name)


