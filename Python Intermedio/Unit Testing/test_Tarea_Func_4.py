from Tarea_Func_4 import upside_down

def test_upside_down_with_large_input_of_strings():
    #arrange 
    text_input = "I'm getting ready to be a sucessful development thanks to Lyfter program."
    #act
    result = upside_down(text_input)
    #assest
    assert result == ".margorp retfyL ot sknaht tnempoleved lufssecus a eb ot ydaer gnitteg m'I"


def test_upside_down_with_small_input_of_numbers():
    #arrange 
    text_input = "1, 5, 8, 6, 9, 2, 6, 7, 8, 9999"
    #act
    result = upside_down(text_input)
    #assest
    assert result == "9999 ,8 ,7 ,6 ,2 ,9 ,6 ,8 ,5 ,1"


def test_upside_down_with_one_large_numerical_input():
    #arrange 
    text_input = "1256398756987456321456987"
    #act
    result = upside_down(text_input)
    #assest
    assert result == "7896541236547896578936521"