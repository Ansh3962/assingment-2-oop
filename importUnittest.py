import unittest
import alchemy

class TestHerb(unittest.TestCase):
    def setUp(self):
        self.arbuck = Herb("Arbuck", 2.6, "necromancy")

    def test_refine(self):
        self.arbuck.refine()
        self.assertEqual(self.arbuck.potency, 2.6 * 2.5)
        self.assertFalse(self.arbuck.grimy)


class TestCatalyst(unittest.TestCase):
    def setUp(self):
        self.eye_of_newt = Catalyst("Eye of Newt", 4.3, 1.0)

    def test_refine(self):
        self.eye_of_newt.refine()
        self.assertEqual(self.eye_of_newt.quality, 2.1)


class TestSuperPotion(unittest.TestCase):
    def setUp(self):
        herb = alchemy.Herb("Irit", 1.0, "attack")
        catalyst = alchemy.Catalyst("Eye of Newt", 4.3, 1.0)
        self.super_potion = alchemy.SuperPotion("Super Attack", herb, catalyst, "attack")


class TestExtremePotion(unittest.TestCase):
    def setUp(self):
        reagent = Herb("Irit", 1.0, "attack")
        super_potion = SuperPotion("Super Attack", reagent, Catalyst("Eye of Newt", 4.3, 1.0), "attack")
        self.extreme_potion = ExtremePotion("Extreme Attack", reagent, super_potion)

    def test_calculate_boost(self):
        self.extreme_potion.calculate_boost()
        # Add the expected boost calculation based on your logic


class TestLaboratory(unittest.TestCase):
    def setUp(self):
        self.lab = Laboratory()

    def test_add_reagent(self):
        herb = Herb("Irit", 1.0, "attack")
        self.lab.add_reagent(herb, 1)
        self.assertIn("Irit", self.lab.herbs)

class TestAlchemist(unittest.TestCase):
    def setUp(self):
        self.alchemist = Alchemist()

    def test_collect_reagent(self):
        herb = Herb("Irit", 1.0, "attack")
        self.alchemist.collect_reagent(herb, 1)
        self.assertIn("Irit", self.alchemist.get_laboratory().herbs)


if __name__ == '__main__':
    unittest.main()



import unittest
import alchemy

class TestHerb(unittest.TestCase):
    def setUp(self):
        self.arbuck = alchemy.Herb("Arbuck", 2.6, "necromancy")

        def test_refine(self):
            self.arbuck.refine()
            self.assertEqual(self.arbuck.potency, 2.6 * 2.5)
            self.assertFalse(self.arbuck.grimy)

class TestCatalyst(unittest.TestCase):
    def setUp(self):
        self.eye_of_newt = alchemy.Catalyst("Eye of Newt", 4.3, 1.0)
    
    def test_refine(self):
        self.eye_of_newt.refine()
        self.assertEqual(self.eye_of_newt.quality, 2.1)


class TestSuperPotion(unittest.TestCase):
    def setUp(self):
        herb = alchemy.Herb("Irit", 1.0, "attack")
        catalyst = alchemy.Catalyst("Eye of Newt", 4.3, 1.0)
        self.super_potion = alchemy.SuperPotion("Super Attack", herb, catalyst, "attack")

    # ... rest of TestSuperPotion ...

class TestExtremePotion(unittest.TestCase):
    def setUp(self):
        reagent = alchemy.Herb("Irit", 1.0, "attack")
        super_potion = alchemy.SuperPotion("Super Attack", reagent, alchemy.Catalyst("Eye of Newt", 4.3, 1.0), "attack")
        self.extreme_potion = alchemy.ExtremePotion("Extreme Attack", reagent, super_potion)

    # ... rest of TestExtremePotion ...

class TestLaboratory(unittest.TestCase):
    def setUp(self):
        self.lab = alchemy.Laboratory()

    # ... rest of TestLaboratory ...

class TestAlchemist(unittest.TestCase):
    def setUp(self):
        self.alchemist = alchemy.Alchemist()

    # ... rest of TestAlchemist ...

if __name__ == '__main__':
    unittest.main()
