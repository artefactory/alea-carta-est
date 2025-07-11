"""Data generation related stuff."""

import numpy as np
from tqdm import trange


class SyntheticDataGenerator:
    def __init__(
        self,
        items_nest: dict,
        nests_interactions: list,
        proba_complementary_items: float = 0.7,
        proba_neutral_items: float = 0.15,
        noise_proba: float = 0.05,
    ) -> None:

        self.proba_complementary_items = proba_complementary_items
        self.proba_neutral_items = proba_neutral_items
        self.noise_proba = noise_proba
        
  
        self.items_nest = items_nest
        self.nests_interactions = nests_interactions
        

    def get_available_sets(self) -> list:
        """Returns the available sets based on the current assortment."""

        self.available_sets = list( # Not sure what it is supposed to do
            key
            for key, value in self.items_nest.items()
            if value[0].intersection(self.assortment)
        )

    def generate_basket(self) -> list:
        """Generates a basket of items based on the defined item sets and their relations."""


        def select_first_item() -> tuple:
            """Selects the first item and its nest randomly from the available sets."""

            chosen_nest = np.random.choice(list(self.items_nest.keys()))
            chosen_item = np.random.choice(list(self.items_nest[chosen_nest]))
            return chosen_item, chosen_nest

        def complete_basket(first_item: int, first_nest: str) -> list:
            """Completes the basket by adding items based on the relations of the first item."""

            basket = [first_item]
            first_key_index = first_nest
            for key in self.available_sets:
                relations = self.nests_interactions[key]
                if (
                    relations[first_key_index] == "compl"
                    and np.random.random() < self.proba_complementary_items
                ):
                    basket.append(np.random.choice(list(nest)))
                elif (
                    relations[first_key_index] == "neutral"
                    and np.random.random() < self.proba_neutral_items
                ):
                    basket.append(np.random.choice(list(nest)))
            return basket

        def add_noise(basket: list) -> list:
            """Adds noise items to the basket based on the defined noise probability."""
            if np.random.random() < self.noise_proba:
                possible_noisy_items = []
                for nest, items in self.items_nest:
                    for item in items:
                        if item not in basket:
                            possible_noisy_items.append(item)
                basket.append(np.random.choice(possible_noisy_items))
            return basket

        first_chosen_item, first_chosen_nest = select_first_item()
        basket = complete_basket(first_chosen_item, first_chosen_nest)
        basket = add_noise(basket)

        return basket

    def generate_dataset(self, n_baskets) -> np.ndarray:
        """Generates a dataset of baskets."""

        baskets = []
        for _ in range(n_baskets):
            baskets.append(self.generate_basket())
        return np.array(baskets, dtype=object)
    
    
