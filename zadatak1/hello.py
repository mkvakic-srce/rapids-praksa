# definirati funkciju hello koja ispisuje "Hello world!"
def print10():
		print ("%d. Hello World" %count)

if __name__ == '__main__':

    # pozvati hello funkciju 10 puta
	count = 1
	while count < 11:
		print10()
		count+=1