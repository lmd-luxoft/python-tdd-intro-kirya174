from add import add


# "2,3,1" => 6
def test_2_3_1_should_be_6():
    # arrange
    expression = "2,3,1"
    expected = 6

    # act
    actual = add(expression)

    # assert
    assert expected == actual


def test_add_5_and_minus_1_should_be_4():
    # arrange
    expression = "5,-1"
    expected = 4

    # act
    actual = add(expression)

    # assert
    assert expected == actual


def test_empty_string_returns_error():
    # arrange
    expression = " , 3"
    expected = -1

    # act
    actual = add(expression)

    # assert
    assert expected == actual


def test_none_returns_error():
    # arrange
    expression = None
    expected = -1

    # act
    actual = add(expression)

    # assert
    assert expected == actual


def test_semicolon_separator():
    # arrange
    expression = "2.3;4.5;6;7"
    expected = 19.8

    # act
    actual = add(expression)

    # assert
    assert expected == actual


def test_single_prefix_as_separator():
    # arrange
    expression = "//#\n1#3#4#5"
    expected = 13

    # act
    actual = add(expression)

    # assert
    assert expected == actual


def test_multiple_prefixes_as_separator():
    # arrange
    expression = "//#$@\n1#2$3@4@5"
    expected = 15

    # act
    actual = add(expression)

    # assert
    assert expected == actual
