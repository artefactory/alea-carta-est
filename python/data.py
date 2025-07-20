"""Data generation related stuff."""

import numpy as np


class SyntheticDataGenerator:
    """Generate Synthetic Data."""

    def __init__(
        self,
        items_nest: dict,  # keys should be integer: the nest number
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

    def generate_basket(self) -> list:
        """Generate a basket of items based on the defined item sets and their relations."""

        def select_first_item() -> tuple:
            """Select the first item and its nest randomly from the available sets."""
            chosen_nest = np.random.choice(list(self.items_nest.keys()))
            chosen_item = np.random.choice(list(self.items_nest[chosen_nest]))
            return chosen_item, chosen_nest

        def complete_basket(first_item: int, first_nest: str) -> list:
            """Complete the basket by adding items based on the relations of the first item."""
            basket = [first_item]
            relations = self.nests_interactions[first_nest]
            for nest_id, items in self.items_nest.items():
                if (
                    relations[nest_id] == "compl"
                    and np.random.random() < self.proba_complementary_items
                ):
                    basket.append(np.random.choice(items))
                elif (
                    relations[nest_id] == "neutral"
                    and np.random.random() < self.proba_neutral_items
                ):
                    basket.append(np.random.choice(items))
            return basket

        def add_noise(basket: list) -> list:
            """Add noise items to the basket based on the defined noise probability."""
            if np.random.random() < self.noise_proba:
                possible_noisy_items = []
                for nest, items in self.items_nest.items():
                    for item in items:
                        if item not in basket:
                            possible_noisy_items.append(item)
                if len(possible_noisy_items) > 0:
                    basket.append(np.random.choice(possible_noisy_items))
            return basket

        first_chosen_item, first_chosen_nest = select_first_item()
        basket = complete_basket(first_item=first_chosen_item, first_nest=first_chosen_nest)
        return add_noise(basket)

    def generate_dataset(self, n_baskets) -> np.ndarray:
        """Generate a dataset of baskets."""
        baskets = [self.generate_basket() for _ in range(n_baskets)]
        return np.array(baskets, dtype=object)
