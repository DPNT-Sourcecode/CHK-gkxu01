from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_with_inavlid_input(self):
        assert checkout_solution.checkout('ABCDEDCBA') == -1

    def test_checkout_when_skus_does_not_have_repeated_items(self):
        assert checkout_solution.checkout('ABCD') == 115

    def test_checkout_when_skus_only_has_repeated_items(self):
        assert checkout_solution.checkout('AAAAAA') == 260

    def test_checkout_when_skus_has_repeated_items_and_single_items(self):
        assert checkout_solution.checkout('AAAAAAA') == 310

    def test_checkout_when_skus_has_mixed_items(self):
        assert checkout_solution.checkout('ABCDABCDADD') == 275


