'''
Test cases for the simple_stats module.
'''
import simple_stats as simple_stats

def test_five_one(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["8.3","10.4","5.0","4.8"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    simple_stats.simple_stats()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')

    assert all(x in all_outputs for x in ["2072 7","2071.680 7.125"]), "Make sure that the number is formatted correctly"

def test_five_two(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["-15.2","10.3","7.8","-9.7"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    simple_stats.simple_stats() 
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    print(all_outputs)
    assert all(x in all_outputs for x in ["11845 -2","11845.330 -1.700"]), "Make sure that the number is formatted correctly"
def test_five_three(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["-2.3","-9.0","-6.5","-5.7"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    simple_stats.simple_stats()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    print(all_outputs)
    assert all(x in all_outputs for x in ["767 -6","766.935 -5.875"]), "Make sure that the number is formatted correctly"