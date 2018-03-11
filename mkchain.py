import random
import copy
from collections import defaultdict


class Model(object):
    """A text generation model based on markov chains."""

    def __init__(self):
        self.model = defaultdict(list)

    def train(self, s):
        """Train the model with the specified string."""
        words = s.split()
        for i, word in enumerate(words):
            if i == len(words)-1:
                self.model['END'].append(word)
                break

            if i == 0:
                self.model['START'].append(word)

            self.model[word].append(words[i+1])

    def generate(self, word_limit=None):
        """Generate a string from the model, with an optional word limit."""
        if not self.model:
            return ""

        generated_words = []
        next_word = None

        while next_word not in self.model['END']:
            if word_limit is not None and len(generated_words) >= word_limit:
                break

            if len(generated_words) == 0:
                potential_words = self.model['START']
            else:
                potential_words = self.model[generated_words[-1]]

            next_word = random.choice(potential_words)
            generated_words.append(next_word)

        return " ".join(generated_words)


def train(data, input_model=None):
    """Trains a model using the input data and outputs a dictionary.

    Args:
        data (list): This is the input data and the training will be based on.
        input_mode (dict): This can be another pre trained model that includes
            words as keys and lists of next words.

    Returns:
        dict: A trained model that has words as keys and lists of next
        words as elements.
    """
    if input_model is None:
        input_model = defaultdict(list)
    else:
        input_model = defaultdict(list, input_model)

    # Clone the input functiont to prevent affectin the input model.
    model = copy.deepcopy(input_model)
    for i, element in enumerate(data):
        if i == len(data)-1:
            model['END'].append(element)
            break

        if i == 0:
            model['START'].append(element)

        model[element].append(data[i+1])

    return model


def generate(model, word_limit=5):
    """This is to generate a data based on the input model.

    Args:
        model (dict): A pre trained model.
        word_limit (int): The maximum word length of the generated text, if it
            doesn't reach an end word.

    Returns:
        list: A generated list based on the data provided to the model.
    """
    generated_data = []
    next_word = None

    while next_word not in model['END']:
        if len(generated_data) == word_limit:
            break

        if len(generated_data) == 0:
            potential_words = model['START']
        else:
            potential_words = model[generated_data[-1]]

        next_word = random.choice(potential_words)
        generated_data.append(next_word)

    return generated_data
