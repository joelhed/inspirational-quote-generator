import random
import copy
from collections import defaultdict


def train(data, input_model=None):
    """Trains a model using the input data and outputs a dictionary.

    Args:
        data(list) : This is the input data and the training will be based on.
        input_mode(dict) : This can be another pre trained model that includes
            words as keys and lists of next words.

    Return:
        returns a trained model which is a dictionary that has words as keys
        and lists of next words as elements.
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


def generate(model, length=5):
    """This is to generate a data based on the input model.

    Args:
        model(dict) : a pre trained model.
        length(int) : length of the generated text if does not reach an end
            word.

    Returns:
        A generated lists based on the data provided to the model.
    """
    generated_data = []

    for i in range(length):
        if len(generated_data) == 0:
            potential_words = model['START']
        else:
            potential_words = model[generated_data[-1]]

        next_word = potential_words[random.randint(0, len(potential_words)-1)]
        generated_data.append(next_word)

        if next_word in model['END']:
            break

    return generated_data
