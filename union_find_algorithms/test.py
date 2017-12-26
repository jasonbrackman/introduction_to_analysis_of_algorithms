import time
import functools

from quick_find import QuickFindUF
from quick_union import QuickUnionUF
from quick_union_weighted import QuickUnionWeightedUF


def timing(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print('Elapsed time: {}'.format(end-start))
        return result
    return wrapper


def get_data():
    with open('test.txt', 'rt') as handle:
        lines = handle.readlines()
        lines = [line.zfill(128).strip() for line in lines]
    return lines


@timing
def main(qf):
    lines = get_data()
    lines = lines

    x = len(lines[0])
    y = len(lines)
    for idx in range(x):
        for idy in range(y):

            # get index number
            id_ = idx * 128 + idy

            # get index value
            current = lines[idx][idy]

            if current == '1':
                up    = lines[idx][idy-1] if idy-1 >= 0 else None
                down  = lines[idx][idy+1] if idy+1 < y else None
                left  = lines[idx-1][idy] if idx-1 >= 0 else None
                right = lines[idx+1][idy] if idx+1 < x else None

                if up == '1':
                    qf.union(idx*128+idy-1, id_)
                if down == '1':
                    qf.union(id_, idx*128+idy+1)
                if left == '1':
                    qf.union((idx-1)*128+idy, id_)
                if right == '1':
                    qf.union(id_, (idx+1)*128+idy)
            else:
                qf.union(id_, 0)

    return qf


if __name__ == "__main__":
    total = 128 * 128

    qf_01 = QuickFindUF(total)
    qf_02 = QuickUnionUF(total)
    qf_03 = QuickUnionWeightedUF(total)

    for qf in (qf_01, qf_02, qf_03):
        qf = main(qf)

        try:
            # Quick Union
            print(len(set([qf.root(index) for index in range(total)]))-1)
        except AttributeError:
            # quick find
            print(len(set(qf.id)) - 1)
