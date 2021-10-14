from pyOpenBCI import OpenBCIGanglion

def print_raw(sample):
    print(sample.channels_data)

#Set (daisy = True) to stream 16 ch 
board = OpenBCIGanglion(mac=None) #Cyton(daisy = False)

board.start_stream(print_raw)
