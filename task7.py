first_term = int(input("enter the first term: "))
common_difference = int(input("enter the common difference: "))
max = int(input("enter the maximum number: "))

def arthimetic_progression(first_term,common_difference,max):
    sequence = []
    next_term = first_term
    while next_term <= max:
        sequence.append(next_term)
        next_term += common_difference
    return sequence


sequence = arthimetic_progression(first_term,common_difference,max)

number_of_sequence = len(sequence)
print(number_of_sequence)

sum_of_sequence = sum(sequence)
print(sum_of_sequence)

squared_terms = [i*2 for i in sequence]
print(squared_terms)