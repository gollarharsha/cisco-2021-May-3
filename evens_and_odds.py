def evens_and_odds(numbers):
    print(f'running evens_and_odds with {numbers=}')
    output = {'evens': [], 'odds': []}

    for one_number in numbers:
        if one_number % 2:  # odd
            output['odds'].append(one_number)
        else:
            output['evens'].append(one_number)

    return output
