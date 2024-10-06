from lib.fibonacci import compute_fibonacci


class TestFibonacci:

    def test_answer(self):
        assert compute_fibonacci(0) == []
        assert compute_fibonacci(1) == [0]
        assert compute_fibonacci(2) == [0, 1]
        assert compute_fibonacci(3) == [0, 1, 1]
        assert compute_fibonacci(4) == [0, 1, 1, 2]
        assert compute_fibonacci(5) == [0, 1, 1, 2, 3]
        assert compute_fibonacci(6) == [0, 1, 1, 2, 3, 5]
        assert compute_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
