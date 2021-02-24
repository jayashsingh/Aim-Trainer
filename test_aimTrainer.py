import unittest
import aimTrainer

#test target creating function
class TestAimTrainerTargetIncorrectInputTooSmall(unittest.TestCase):
    def test_createTarget(self):
        with self.assertRaises(ValueError):
            aimTrainer.createTarget(10, 75)
class TestAimTrainerTargetIncorrectInputTooLarge(unittest.TestCase):
    def test_createTarget(self):
        with self.assertRaises(ValueError):
            aimTrainer.createTarget(25, 105)
class TestAimTrainerTargetCorrectInput(unittest.TestCase):
    def test_createTarget(self):
        try:
            aimTrainer.createTarget(50, 60)
        except:
            self.fail("This should not fail.")
        else:
            pass

#test score render function
class TestAimTrainerScoreIncorrectInput(unittest.TestCase):
    def test_renderScore(self):
        with self.assertRaises(ValueError):
            aimTrainer.renderScore("T")
class TestAimTrainerScoreCorrectInput(unittest.TestCase):
    def test_renderScore(self):
        try:
            aimTrainer.renderScore(9)
        except:
            self.fail("This should not fail.")
        else:
            pass

#test timer render function
class TestAimTrainerTimingIncorrectInput(unittest.TestCase):
    def test_renderTimer(self):
        with self.assertRaises(ValueError):
            aimTrainer.renderTimer("T")
class TestAimTrainerTimingCorrectInput(unittest.TestCase):
    def test_renderTimer(self):
        try:
            aimTrainer.renderTimer(9)
        except:
            self.fail("This should not fail.")
        else:
            pass

#test end screen render function
class TestAimTrainerEndScreenIncorrectInput(unittest.TestCase):
    def test_endScreen(self):
        with self.assertRaises(ValueError):
            aimTrainer.endScreen("T")
class TestAimTrainerEndScreenCorrectInput(unittest.TestCase):
    def test_endScreen(self):
        try:
            aimTrainer.endScreen(9)
        except:
            self.fail("This should not fail.")
        else:
            pass

if __name__ == '__main__':
    unittest.main()
