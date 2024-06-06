from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_with_inavlid_input(self):
        assert checkout_solution.checkout('ABCDZDCBA') == -1

    def test_checkout_with_empty_input(self):
        assert checkout_solution.checkout('') == 0

    def test_checkout_when_skus_does_not_have_repeated_items(self):
        assert checkout_solution.checkout('ABCDE') == 155

    def test_checkout_when_skus_only_has_repeated_items(self):
        assert checkout_solution.checkout('AAAAAAAAA') == 380

    def test_checkout_when_skus_has_repeated_items_and_single_items(self):
        assert checkout_solution.checkout('AAAAAAAAAAAAAA') == 580

    def test_checkout_when_skus_has_mixed_items(self):
        assert checkout_solution.checkout('ABCDABCDADDE') == 315

    def test_checkout_when_get_some_free_itens(self):
        assert checkout_solution.checkout('BBBBBBBEEEEEEE') == 400
        assert checkout_solution.checkout('BBBBBBBEEEEEEEE') == 395
        assert checkout_solution.checkout('BBBBBBBBEEEEEEE') == 410
        assert checkout_solution.checkout('BBBBBBBBEEEEEEEE') == 400

# 8B e 7E - 3B free = 120 + 280 ||



