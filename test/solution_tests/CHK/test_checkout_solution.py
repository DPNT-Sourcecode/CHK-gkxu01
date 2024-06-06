from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_with_inavlid_input(self):
        assert checkout_solution.checkout('ABCDEDCBA') == -1
