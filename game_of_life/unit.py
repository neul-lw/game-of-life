from main import next_state


def test_failed(wt, expected_next_state, actual_next_state):
    print(f"FAILED {wt}")
    print("Expected:")
    print(expected_next_state)
    print("Actual:")
    print(actual_next_state)

if __name__ == "__main__":
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state1 = next_state(init_state1)

    if expected_next_state1 == actual_next_state1:
        print("PASSED 1")
    else:
        test_failed(1, expected_next_state1, actual_next_state1)
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = next_state(init_state2)

    if expected_next_state2 == actual_next_state2:
        print("PASSED 2")
    else:
        test_failed(2, expected_next_state2, actual_next_state2)
