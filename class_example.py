
class Test:
    def __init__(self, callback):
        self.callback = callback

    def test_once(self, input, expected_output):
        try:
            if expected_output == self.callback(input):
                print("ok")
            else:
                print("X.")
                print("Expected output: ", expected_output)
                print("Actual output: ", self.callback(input))
        except Exception as inst:
            print("X. An error has ocurred")
            print(inst)
            
    def __str__(self):
        return "esto se imprime"


def f1(x):
    return 2*x

test1 = Test(f1)

test1.test_once(2, 4)