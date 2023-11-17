'''
File: alchemy.py
Description: Object-oriented design for an alchemy crafting application.
Author: Your Full Name
StudentID: Your Student ID
EmailID: Your Email ID
This is my own work as defined by the University's Academic Misconduct Policy.
'''

class Reagent:
    """
    A class representing a reagent with a name and potency. It serves as a base class for Herbs and Catalysts.
    """

    def __init__(self, name, potency):
        self._name = name
        self._potency = potency

    @property
    def name(self):
        return self._name

    @property
    def potency(self):
        return self._potency

    @potency.setter
    def potency(self, value):
        self._potency = value

    def refine(self):
        raise NotImplementedError("Refine method must be implemented in subclass.")


class Herb(Reagent):
    """
    A class representing an herb, a type of reagent, which can be refined to increase its potency.
    """

    def __init__(self, name, potency):
        super().__init__(name, potency)
        self._grimy = True

    def refine(self):
        if self._grimy:
            self._potency *= 2.5
            self._grimy = False
            print(f"{self._name} refined. Potency is now {self._potency}.")


class Catalyst(Reagent):
    """
    A class representing a catalyst, a type of reagent, which can be refined to improve its quality.
    """

    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self._quality = quality

    def refine(self):
        if self._quality < 8.9:
            self._quality += 1.1
            print(f"{self._name} refined. Quality is now {self._quality}.")
        else:
            self._quality = 10
            print(f"{self._name} cannot be refined any further. Quality is {self._quality}.")


class Potion:
    """
    A class representing a potion with a name, the stat it increases, and the boost it provides.
    """

    def __init__(self, name, stat, boost):
        self._name = name
        self._stat = stat
        self._boost = boost

    def calculate_boost(self, herb=None, catalyst=None, super_potion=None):
        if herb and catalyst:
            self._boost = round(herb.potency + (catalyst.potency * catalyst.quality) * 1.5, 2)
        elif super_potion:
            self._boost = round((self.potency * super_potion.boost) * 3.0, 2)

    @property
    def name(self):
        return self._name

    @property
    def stat(self):
        return self._stat

    @property
    def boost(self):
        return self._boost


class Laboratory:
    """
    A class representing a laboratory where an alchemist can mix potions using various reagents.
    """

    def __init__(self):
        self._potions = {}
        self._herbs = {}
        self._catalysts = {}

    def add_reagent(self, reagent, amount):
        if isinstance(reagent, Herb):
            self._herbs[reagent.name] = (reagent, amount)
        elif isinstance(reagent, Catalyst):
            self._catalysts[reagent.name] = (reagent, amount)

    def mix_potion(self, recipe_name, alchemist):
        recipe = alchemist.recipes.get(recipe_name)
        if not recipe:
            return None

        if recipe['type'] == 'super':
            herb_name, catalyst_name = recipe['ingredients']
            herb, herb_amount = self._herbs.get(herb_name, (None, 0))
            catalyst, catalyst_amount = self._catalysts.get(catalyst_name, (None, 0))

            if herb and catalyst and herb_amount > 0 and catalyst_amount > 0:
                new_potion = Potion(recipe_name, recipe['stat'], 0)
                new_potion.calculate_boost(herb=herb, catalyst=catalyst)
                self._potions[recipe_name] = new_potion
                return new_potion

        elif recipe['type'] == 'extreme':
            reagent_name, super_potion_name = recipe['ingredients']
            reagent, reagent_amount = self._herbs.get(reagent_name, self._catalysts.get(reagent_name, (None, 0)))
            super_potion = self._potions.get(super_potion_name)

            if reagent and super_potion and reagent_amount > 0:
                new_potion = Potion(recipe_name, recipe['stat'], 0)
                new_potion.calculate_boost(super_potion=super_potion)
                self._potions[recipe_name] = new_potion
                return new_potion

        return None


class Alchemist:
    """
    A class representing an alchemist who can mix potions, drink them to increase attributes, and refine reagents.
    """

    def __init__(self):
        self._attributes = {attr: 0 for attr in ['attack', 'strength', 'defense', 'magic', 'ranged', 'necromancy']}
        self._laboratory = Laboratory()
        self._recipes = {
            # Add all other recipes here as per the provided description
        }

    def mix_potion(self, recipe_name):
        potion = self._laboratory.mix_potion(recipe_name, self)
        if potion:
            self._attributes[potion.stat] += potion.boost
            print(f"{potion.name} mixed. {potion.stat.capitalize()} is increased by {potion.boost}.")

    def collect_reagent(self, reagent, amount):
        self._laboratory.add_reagent(reagent, amount)

    def refine_reagents(self):
        for herb in self._laboratory._herbs.values():
            herb[0].refine()
        for catalyst in self._laboratory._catalysts.values():
            catalyst[0].refine()
