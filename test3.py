class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_item = None
        self.stack = [iter(list_of_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                self.current_item = next(self.stack[-1])
                if isinstance(self.current_item, list):
                    self.stack.append(iter(self.current_item))
                else:
                    return self.current_item
            except StopIteration:
                self.stack.pop()

        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
