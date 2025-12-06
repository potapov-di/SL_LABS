def swap_min_max_words(line):
    words = line.split()
    if not words:
        return line

    min_index = min(range(len(words)), key=lambda i: len(words[i]))
    max_index = max(range(len(words)), key=lambda i: len(words[i]))

    words[min_index], words[max_index] = words[max_index], words[min_index]
    return " ".join(words)


with open("input.txt", "r", encoding="utf-8") as infile, \
    open("output.txt", "w", encoding="utf-8") as outfile:
    for line in infile:
        swapped_line = swap_min_max_words(line.strip())
        outfile.write(swapped_line + "\n")
