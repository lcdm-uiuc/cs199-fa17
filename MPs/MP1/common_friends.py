from map_reducer import MapReduce


def friend_mapper(line):
    ''' write your code here! '''
    pass


def friend_reducer(friend_tuples):
    ''' write your code here! '''
    pass


def _run_common_friend_finder(filename):
    with open(filename) as f:
        lines = f.readlines()
    mr = MapReduce(friend_mapper, friend_reducer)
    common_friends = mr(lines)
    for relationship, friends in common_friends:
        print('{}\t{}'.format(relationship, friends))

if __name__ == '__main__':
    print('friend_graph_example.txt')
    _run_common_friend_finder('friend_graph_example.txt')

    print('friend_graph.txt')
    _run_common_friend_finder('friend_graph.txt')
