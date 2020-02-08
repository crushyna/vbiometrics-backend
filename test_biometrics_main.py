import unittest
from biometrics_main import main

test_login = 'test_login_1'
test_voice_sample = 'src/test_sounds/clint_eastwood_1.wav'


class BiometricsMainTest(unittest.TestCase):
    """
    simple test for module entry point
    """
    def test_result(self):
        self.assertIsInstance(main(test_login, test_voice_sample), bool)


if __name__ == '__main__':
    unittest.main()
