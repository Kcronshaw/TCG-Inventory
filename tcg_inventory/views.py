from django.shortcuts import render
from .api import CardAPI

def card_list(request):
    api = CardAPI()
    cards = api.get_cards(request)
    return render(request, 'inventory.html', {'cards': cards})

def add_card(request):
    if request.method == 'POST':
        # Logic to add card using data from form or API
        pass
    return render(request, 'add_card.html')