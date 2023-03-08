from django.shortcuts import render
from .models import Art

# arts = [
#     {'title' : "Ramona Flowers' portrait", 'author': 'Scott Pilgrim', 'type': 'drawing', 'method': 'marker on A3 paper', 'comment': 'Have you seen a woman at a party with this hair?', 'likes': 4, 'file': 'ramona-flowers.jpg', 'description': 'A portrait of Ramona Flowers', 'year': 2008},
#     {'title' : "Human Perfection", 'author': 'Leonardo da Vinci', 'type': 'drawing', 'method': 'pencil on scroll', 'comment': 'Modestamente, ho creato questo in 10 minuti.', 'likes': 10000000000, 'file': 'leonardo-da-vinci.webp', 'description': 'the famouse sketch by Leonardo da Vinci', 'year': 1412},
#     {'title' : "Heisenberg", 'author': 'DEA', 'type': 'sketch', 'method': 'pen on paper', 'comment': 'Do you know this man?', 'likes': 2301, 'file': 'heisenberg.jpg', 'description': 'a sketch of heisenberg', 'year': 2010}
# ]

# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def arts_index(req):
    arts= Art.objects.all()
    return render(req, 'arts/index.html', { 'arts' : arts })

def arts_detail(req, art_id):
    art= Art.objects.get(id=art_id)
    return render(req, 'arts/detail.html', { 'art': art })