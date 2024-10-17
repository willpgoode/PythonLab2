'''
Test cases for the telephone module.
'''
import real_estate as real_estate

def test_four_one(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["200000","210000"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    real_estate.real_estate()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')

    assert all(x in all_outputs for x in ["This house is $200000. The change is $-10000 since last month.","The estimated monthly mortgage is $850.00."]), "Make sure that the number is formatted correctly"

def test_four_two(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["350000","310000"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    real_estate.real_estate()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    print(all_outputs)
    assert all(x in all_outputs for x in ["This house is $350000. The change is $40000 since last month.","The estimated monthly mortgage is $1487.50."]), "Make sure that the number is formatted correctly"
def test_four_three(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["1000000","100000"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    real_estate.real_estate()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')
    print(all_outputs)
    assert all(x in all_outputs for x in ["This house is $1000000. The change is $900000 since last month.", "The estimated monthly mortgage is $4250.00."]), "Make sure that the number is formatted correctly"