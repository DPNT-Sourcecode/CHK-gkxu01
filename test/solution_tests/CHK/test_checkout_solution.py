from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_with_inavlid_input(self):
        assert checkout_solution.checkout('ABCD-DCBA') == -1

    def test_checkout_with_empty_input(self):
        assert checkout_solution.checkout('') == 0

    def test_checkout_with_only_one_item(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('C') == 20
        assert checkout_solution.checkout('D') == 15
        assert checkout_solution.checkout('E') == 40

    def test_checkout_when_skus_does_not_have_repeated_items(self):
        assert checkout_solution.checkout('ABCDE') == 155

    def test_checkout_when_skus_only_has_repeated_items(self):
        assert checkout_solution.checkout('AAAAAAAAA') == 380

    def test_checkout_when_skus_has_repeated_items_and_single_items(self):
        assert checkout_solution.checkout('AAAAAAAAAAAAAA') == 580

    def test_checkout_when_skus_has_mixed_items(self):
        assert checkout_solution.checkout('ABCDABCDADDE') == 315

    def test_checkout_when_get_some_free_itens(self):
        assert checkout_solution.checkout('EEB') == 80
        assert checkout_solution.checkout('EEEB') == 120
        assert checkout_solution.checkout('EEEEBB') == 160
        assert checkout_solution.checkout('BBBBBBBEEEEEEE') == 370
        assert checkout_solution.checkout('BBBBBBBEEEEEEEE') == 395
        assert checkout_solution.checkout('BBBBBBBBEEEEEEE') == 400
        assert checkout_solution.checkout('BBBBBBBBEEEEEEEE') == 410

    def test_checkout_when_get_some_free_itens_requiring_minimal_quantity(self):
        assert checkout_solution.checkout('F') == 10
        assert checkout_solution.checkout('FF') == 20
        assert checkout_solution.checkout('FFF') == 20
        assert checkout_solution.checkout('FFFF') == 30
        assert checkout_solution.checkout('FFFFF') == 40
        assert checkout_solution.checkout('FFFFFF') == 40

    def test_checkout_with_group_of_items_offer(self):
        assert checkout_solution.checkout('STX') == 45
        assert checkout_solution.checkout('STXSTX') == 90
        assert checkout_solution.checkout('SSS') == 45
        assert checkout_solution.checkout('SSTTXXYYZZ') == 17 + 45 + 45 + 45

    def test2(self):
        assert checkout_solution.checkout('RRRQ') == 150
        assert checkout_solution.checkout('RRRRQ') == 200
        assert checkout_solution.checkout('RRRRRRQQ') == 300
        assert checkout_solution.checkout('HHHHHHHHHH') == 80
        assert checkout_solution.checkout('HHHHHHHHHHH') == 90
        assert checkout_solution.checkout('HHHHHHHHHHHH') == 100
