from django.test import TestCase

from .models import Coin

# Create your tests here.
class CoinModelTests(TestCase):
    fixtures = ['fixture1']

    def setUp(self):
        self.user_id = "1234567890"
        return

    def test_calculate_with_positive_amount(self):
        """
        calculate() with positive amount returns coin amount if succeeded coin calculation.
        """
        before_amount = Coin.objects.get_amount(self.user_id)
        add_coin_value = 100
        after_amount = Coin.objects.calculate(self.user_id, add_coin_value)
        self.assertEqual(after_amount, before_amount + add_coin_value)

    def test_calculate_with_minus_amount(self):
        """
        calculate() with minus amount returns coin amount if succeeded coin calculation.
        """
        before_amount = Coin.objects.get_amount(self.user_id)
        add_coin_value = -100
        after_amount = Coin.objects.calculate(self.user_id, add_coin_value)
        self.assertEqual(after_amount, before_amount + add_coin_value)

    def test_calculate_with_exceeded_minus_amount(self):
        """
        calculate() with exceeded minus amount returns False if negative value exceeded coin amount.
        """
        return

    def test_get_amount_with_user_id(self):
        """
        get_amount() for specific user returns valid amount if succeeded coin amount get.
        """
        return
