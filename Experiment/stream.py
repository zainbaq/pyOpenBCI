from pyOpenBCI import OpenBCIGanglion
from pylsl import StreamInfo, StreamOutlet
import numpy as np
import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', type=str, default='config/board_config.json')
    return parser.parse_args()

SCALE_FACTOR_EEG = (4500000)/24/(2**23-1) #uV/count

args = parse_args()

with open(args.config_path) as f:
    BOARD_CONFIG = json.load(f)

print("Creating LSL stream for EEG. \nName: OpenBCIEEG\nID: OpenBCItestEEG\n")

info_eeg = StreamInfo('OpenBCIEEG', 'EEG', 4, 250, 'float32', 'OpenBCItestEEG')

outlet_eeg = StreamOutlet(info_eeg)


info = StreamInfo('MarkerStream', 'Markers', 4, 0, 'string', 'OpenBCItestMarkers')
# next make an outlet
outlet = StreamOutlet(info)
markernames = ['Marker']

def lsl_streamers(sample):
    # print(len(sample)
    print(sample.channels_data)
    outlet_eeg.push_sample(np.array(sample.channels_data)*SCALE_FACTOR_EEG)
    # outlet.push_sample(markernames[0])s
    print(np.array(sample.channels_data)*SCALE_FACTOR_EEG)

board = OpenBCIGanglion(mac=BOARD_CONFIG['mac_address'])
board.start_stream(lsl_streamers)


