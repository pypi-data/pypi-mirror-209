import pytest
from satyampy import __main__

# class TestSatyampy(unittest.TestCase):
def test_adding(sample_inputs):
    x, y = sample_inputs
    assert __main__.adding(x, y) == 5
    # self.assertEqual(__main__.adding(2, 3), 5)
    # self.assertEqual(__main__.adding(-1, 1), 0)
    # self.assertEqual(__main__.adding(0, 0), 0)
        # Add more test cases as needed

# if __name__ == '__main__':
#     unittest.main()
