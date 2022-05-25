# definirati funkciju hello koja ispisuje "Hello world!"
def hello():
    print('Hello world!')
    return

if __name__ == '__main__':

    # pozvati hello funkciju 10 puta
    for i in range(10):
        hello()
