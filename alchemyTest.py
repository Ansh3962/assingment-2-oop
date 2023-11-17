import unittest
from alchemy import Reagent, Herb, Catalyst, Potion, SuperPotion, ExtremePotion, Laboratory, Alchemist

# You might need to adjust the import statement based on how you've organized your code

class TestHerb(unittest.TestCase):

    def setUp(self):
        self.irit = Herb("Irit", 1.0)

    def test_refine(self):
        self.irit.refine()
        self.assertEqual(self.irit.potency, 2.5)
        self.assertFalse(self.irit.grimy)

class TestCatalyst(unittest.TestCase):

    def setUp(self):
        self.eye_of_newt = Catalyst("Eye of Newt", 4.3, 1.0)

    def test_refine(self):
        self.eye_of_newt.refine()
        self.assertEqual(self.eye_of_newt.quality, 2.1)

class TestPotion(unittest.TestCase):

    def setUp(self):
        self.potion = Potion("Healing Potion", "health", 10)

    def test_boost_setter(self):
        self.potion.boost = 15
        self.assertEqual(self.potion.boost, 15)

class TestSuperPotion(unittest.TestCase):

    def setUp(self):
        self.herb = Herb("Irit", 1.0)
        self.catalyst = Catalyst("Eye of Newt", 4.3, 1.0)
        self.super_potion = SuperPotion("Super Healing Potion", self.herb, self.catalyst)

    def test_calculate_boost(self):
        self.herb.refine()
        self.catalyst.refine()
        self.super_potion.calculate_boost()
        expected_boost = round(self.herb.potency + (self.catalyst.potency * self.catalyst.quality) * 1.5, 2)
        self.assertEqual(self.super_potion.boost, expected_boost)

class TestExtremePotion(unittest.TestCase):

    def setUp(self):
        self.reagent = Herb("Irit", 1.0)
        self.reagent.refine()
        self.super_potion = SuperPotion("Super Healing Potion", self.reagent, Catalyst("Eye of Newt", 4.3, 1.0))
        self.extreme_potion = ExtremePotion("Extreme Healing Potion", self.reagent, self.super_potion)

    def test_calculate_boost(self):
        self.extreme_potion.calculate_boost()
        expected_boost = round((self.reagent.potency * self.super_potion.boost) * 3.0, 2)
        self.assertEqual(self.extreme_potion.boost, expected_boost)

class TestLaboratory(unittest.TestCase):

    def setUp(self):
        self.lab = Laboratory()

    def test_add_reagent(self):
        herb = Herb("Irit", 1.0)
        self.lab.add_reagent(herb, 1)
        self.assertIn("Irit", self.lab.herbs)

class TestAlchemist(unittest.TestCase):

    def setUp(self):
        self.alchemist = Alchemist()

    def test_mix_potion(self):
        # Assuming the alchemist knows a recipe and the lab has the ingredients
        # You'll need to add the recipes and ingredients for a valid test
        potion_name = "Super Attack"
        self.alchemist.mix_potion(potion_name)
        self.assertIn(potion_name, self.alchemist.get_laboratory().potions)
