import os

def read_file(file_path: str) -> str:
    """
    Read the contents of a file.

    :param file_path: The path to the file to read.
    :return: The contents of the file.
    """

    if not os.path.isfile(file_path):
        raise ValueError(f"{file_path} is not a file.")

    with open(file_path, 'r') as file:
        return file.read()

def compute_jaccard_similarity(a: str, b: str) -> float:
    """
    Compute the Jaccard similarity between two programs.

    :param a: The first program to compare.
    :param b: The second program to compare.
    :return: The Jaccard similarity between the two programs.
    """

    a_content = set(read_file(a).splitlines())
    b_content = set(read_file(b).splitlines())

    intersection = a_content.intersection(b_content)
    union = a_content.union(b_content)

    if not union:
        return 1.0

    return len(intersection) / len(union)

def visualise_dot_plot(a: str, b: str) -> str:
    a_content = read_file(a).splitlines()
    b_content = read_file(b).splitlines()

    plot = '-' * 80 + '\n'
    for i in range(len(a_content)):
        plot += f'x{i}: {a_content[i]}\n'
    plot += '-' * 80 + '\n'
    for j in range(len(b_content)):
        plot += f'y{j}: {b_content[j]}\n'
    plot += '-' * 80 + '\n'

    # Header row
    plot += '\t'
    for i in range(len(a_content)):
        plot += f'x{i}\t'
    plot += '\n'

    # Dot plot
    for j in range(len(b_content)):
        plot += f'y{j}\t'
        for i in range(len(a_content)):
            if a_content[i] == b_content[j]:
                plot += '*\t'
            else:
                plot += ' \t'   # <-- IMPORTANT: space + tab
        plot += '\n'

    plot += '-' * 80

    return plot