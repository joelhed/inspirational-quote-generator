#!/usr/bin/env python3
import mkchain


if __name__ == "__main__":
    model = mkchain.Model()

    with open('dataset.txt') as dataset:
        for line in dataset:
            model.train(line)

    with open('generated.txt', '+w') as f:
        for i in range(100):
            text = model.generate(model, word_limit=50)
            f.write(text + '\n\n')
