"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    d = {}
    # TODO: Count the number of occurences of each word in s
    for word in s.split(' '):
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    sorted_x = [(k,v) for k, v in d.items()]
    sorted_x= sorted(d.iteritems(),key=lambda (k,v):(-v,k))
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = sorted_x[:n]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
