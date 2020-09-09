exit = False
while(exit == False):
	print("\n-------- New file ---------")
	time = int(input("Runtime of Video File (In Mins) : "))
	bitrate = int(input("Desired video bitrate (in kbps) : "))
	newSize = (((bitrate+128)*time*60)/8)/1024
	print(" ==> Approx size : " + str(newSize))
	choice = 'Y'
	while( choice == 'Y' ):
		choice = input("Re-calculate size (Y/N) : \n(Will Exit if no re-calculation needed)")
		if(choice == 'N' or choice == 'n'):
			exit = True
			break
		elif (choice == 'Y' or choice == 'y'):
			break
		else:
			continue