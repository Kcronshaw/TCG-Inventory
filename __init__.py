from django.apps import AppConfig

class TcgInventoryConfig(AppConfig):
    name = 'invenree.plugins.tcg_inventory'

    def ready(self):
        from .api import CardAPI
        from .views import card_list, add_card
        InvenTreePlugin import register_plugin
        register_plugin('tcg_inventory', __name__, CardAPI)