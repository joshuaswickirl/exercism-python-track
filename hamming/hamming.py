def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        strand_a_list = list(strand_a)
        strand_b_list = list(strand_b)
        hamming_distance = 0
        for index in range(len(strand_a_list)):
            if strand_a_list[index] != strand_b_list[index]:
                hamming_distance += 1
    else:
        raise ValueError("strand_a and strand_b are of different length")
    return hamming_distance
    