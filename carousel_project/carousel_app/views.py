from django.shortcuts import render 
def carousel_view(request): 
    images = [ 
        'https://picsum.photos/800/400?random=1', 
        'https://picsum.photos/800/400?random=2', 
        'https://picsum.photos/800/400?random=3', 
        'https://picsum.photos/800/400?random=4', 
        'https://picsum.photos/800/400?random=5', 
    ] 
    return render(request, 'carousel/carousel.html', {'images': images}) 