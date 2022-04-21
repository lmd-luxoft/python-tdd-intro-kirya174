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

