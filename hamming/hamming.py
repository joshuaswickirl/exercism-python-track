def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("strand_a and strand_b are of different length")

    return sum(1 for (letter_a, letter_b) in zip(strand_a, strand_b) if letter_a != letter_b)
