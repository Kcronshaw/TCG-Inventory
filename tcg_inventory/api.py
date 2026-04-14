from invenree.core import InvenTreePlugin, api
import json

class CardAPI(InvenTreePlugin):
    def list_cards(self):
        # Query your TCG API or local DB for card data
        response = requests.get('https://your-tcg-api.com/cards')
        return json.loads(response.text)

    @api('/api/card/', method='GET')
    def get_cards(self, request):
        cards = self.list_cards()
        return api.return_data(cards)