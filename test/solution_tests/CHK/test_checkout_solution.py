from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_with_inavlid_input(self):
        assert checkout_solution.checkout('ABCDEDCBA') == -1

    def test_checkout_when_skus_does_not_have_duplicates(self):
        assert checkout_solution.checkout('ABCD') == 115

    def test_checkout_when_skus_does_have_duplicates(self):
        assert checkout_solution.checkout('ABCD') == 115

