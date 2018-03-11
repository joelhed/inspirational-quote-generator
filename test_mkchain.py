import mkchain


def test_train():
    model = mkchain.train(["Test", "model."])
    print(model)
    assert model == {
        "START": ["Test"],
        "Test": ["model."],
        "END": ["model."]
        }

    model = mkchain.train(["Test", "new", "model."], model)
    print(model)
    assert model == {
        "START": ["Test", "Test"],
        "Test": ["model.", "new"],
        "new": ["model."],
        "END": ["model.", "model."]
        }


if __name__ == "__main__":
    test_train()
