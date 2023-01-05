def load_board_state(path):
    arr = []
    with open(path, 'r') as f:
        f = f.readlines()
        f = [line.replace("\n", "") for line in f]
        for line in f:
            row = []
            for n in line:
                n = int(n)
                row.append(n)
            arr.append(row)
    print(arr)
    return arr 


load_board_state('./toads/toad.txt')
