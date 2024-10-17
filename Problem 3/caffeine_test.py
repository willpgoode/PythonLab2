'''
Test cases for the telephone module.
'''
import caffeine as caffeine

def test_three_one(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["100"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    caffeine.caffeine()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')

    assert all(x in all_outputs for x in ["After 6 hours: 50.00 mg","After 12 hours: 25.00 mg","After 24 hours: 6.25 mg"]), "Make sure that the number is formatted correctly"

def test_three_two(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["40"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    caffeine.caffeine()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    print(all_outputs)
    assert all(x in all_outputs for x in ["After 6 hours: 20.00 mg","After 12 hours: 10.00 mg","After 24 hours: 2.50 mg"]), "Make sure that the number is formatted correctly"

def test_three_three(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["200"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    caffeine.caffeine()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    print(all_outputs)
    assert all(x in all_outputs for x in ["After 6 hours: 100.00 mg","After 12 hours: 50.00 mg","After 24 hours: 12.50 mg"]), "Make sure that the number is formatted correctly"
