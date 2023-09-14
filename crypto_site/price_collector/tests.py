from django.test import TestCase

# Create your tests here.
class CoinResultViewTests(TestCase):

    def test_valid_coin(self):
        url = "/price_collector/collect_data/"
        response = self.client.get(url, {'coin': "bitcoin"})
        self.assertContains(response, "The latest price of bitcoin is")

    def test_invalid_coin(self):
        pass
