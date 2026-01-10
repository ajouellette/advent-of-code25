import sys
import itertools


def parse_input(filename):
    pos = []
    with open(filename) as f:
        for line in f.readlines():
            pos.append(list(map(int, line.split(','))))
    return pos


def build_dist_table(pos):
    dist2 = lambda p1, p2: sum([(x1 - x2)**2 for x1, x2 in zip(p1, p2)])
    dists = []
    inds = []
    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            inds.append((i, j))
            dists.append(dist2(pos[i], pos[j]))
    # sort pairs by distance
    inds = [ind for _, ind in sorted(zip(dists, inds))]
    return inds, dists


def build_circuits(inds, connections=None):
    circuits = []
    niter = 0
    while niter < len(inds):
        ind_pair = inds[niter]
        if len(circuits) == 0:
            circuits.append(set(ind_pair))
        else:
            connects_to = [None, None]
            for i, circuit in enumerate(circuits):
                if ind_pair[0] in circuit:
                    connects_to[0] = i
                if ind_pair[1] in circuit:
                    connects_to[1] = i
                if connects_to[0] is not None and connects_to[1] is not None:
                    break
            #print(circuits, ind_pair, connects_to)
            if connects_to[0] is not None and connects_to[1] is not None:
                c1, c2 = connects_to
                circuits[c1].update(circuits[c2])
                if c1 != c2:
                    circuits.pop(c2)
            elif connects_to[0] is not None:
                circuits[connects_to[0]].add(ind_pair[1])
            elif connects_to[1] is not None:
                circuits[connects_to[1]].add(ind_pair[0])
            else:
                circuits.append(set(ind_pair))

        niter += 1
        if connections is not None and niter == connections:
            break
        # end loop once first circuit contains all points
        # len(inds) == (len(pos)**2 - len(pos)) / 2
        if connections is None and (len(circuits[0])**2 - len(circuits[0]))//2 == len(inds):
            break
    return circuits, niter


def main():
    pos = parse_input(sys.argv[1])
    print(len(pos))

    # pairs already sorted by distance, don't need dists
    pair_inds, _ = build_dist_table(pos)

    circuits, n_connections = build_circuits(pair_inds, 10)

    print(circuits)
    circuit_lens = sorted([len(circuit) for circuit in circuits], reverse=True)
    print(circuit_lens)

    total = 1
    for x in circuit_lens[:3]:
        total *= x
    print(total)

    # part 2
    circuits, n_connections = build_circuits(pair_inds)
    print(n_connections)
    pair = pair_inds[n_connections-1]
    print(pair)
    print([pos[i] for i in pair])
    print(pos[pair[0]][0] * pos[pair[1]][0])


if __name__ == "__main__":
    main()
