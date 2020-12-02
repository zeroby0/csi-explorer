import os
import numpy as np
from CsiSample import Sample


class Explorer():
    def __init__(self, filepath, bandwidth=80):
        self.filepath = filepath
        self.bandwidth = bandwidth
        self.samples = []

        self.__read()
    
    def __read_header(self, pcapfile):
        self.h_magic = pcapfile.read(4)

        self.h_vmajor = int.from_bytes(# uint16: Major version number
            pcapfile.read(2),
            byteorder = 'little',
            signed = False
        )

        self.h_vminor = int.from_bytes(# uint16: Minor version number
            pcapfile.read(2),
            byteorder = 'little',
            signed = False
        )

        self.h_thiszone = int.from_bytes(# int32: GMT to Local correction
            pcapfile.read(4),
            byteorder = 'little',
            signed = True   
        )

        self.h_sigfigs = int.from_bytes(# uint32: Accuracy of Time Stamp
            pcapfile.read(4),
            byteorder = 'little',
            signed = False          
        )

        self.h_snaplen = int.from_bytes(# uint32: Max length of packets
            pcapfile.read(4),
            byteorder = 'little',
            signed = False 
        )

        self.h_network = int.from_bytes(# uint32: Data link type
            pcapfile.read(4),
            byteorder = 'little',
            signed = False 
        ) 

    
    def __read_frame(self, pcapfile):
        csi = Sample(self.bandwidth)

        # ----------***** Pcap Frame Header *****----------
        ts_sec  = int.from_bytes(# uint32: Timestamp Seconds
            pcapfile.read(4),
            byteorder = 'little',
            signed = False
        )

        ts_usec = int.from_bytes(# uint32: Timestamp micro Seconds
            pcapfile.read(4),
            byteorder = 'little',
            signed = False
        )

        len_incl = int.from_bytes(#uint32: number of octets in file
            pcapfile.read(4),
            byteorder = 'little',
            signed = False
        )

        len_orig = int.from_bytes(#uint32: Actual number of octets
            pcapfile.read(4),
            byteorder = 'little',
            signed = False
        )

        csi.set_ts(ts_sec, ts_usec)
        csi.set_len(len_incl, len_orig)

        # ----------***** Protocol Headers *****----------
        pcapfile.seek(14, os.SEEK_CUR) # Skip Ethernet Header
        pcapfile.seek(20, os.SEEK_CUR) # Skip IPv4 header
        pcapfile.seek(8, os.SEEK_CUR)  # Skip UDP header

        # ----------***** CSI Header *****----------
        magic = pcapfile.read(4)
        mac_1 = pcapfile.read(6)
        mac_2 = pcapfile.read(6)
        mac_3 = pcapfile.read(6)

        # fc = int.from_bytes(#uint16: FC
        #     pcapfile.read(2),
        #     byteorder = 'big',
        #     signed = False
        # )

        fc = pcapfile.read(2)

        sc = int.from_bytes(#uint16: SC
            pcapfile.read(2),
            byteorder = 'little',
            signed = False
        )

        rssi = int.from_bytes(#int8: RSSI
            pcapfile.read(1),
            byteorder='big',
            signed=True
        )

        pcapfile.read(1) # Skip 1 padding byte after RSSI

        # pcapfile.seek(10, os.SEEK_CUR) # Skip Reserved bytes
        resr = pcapfile.read(10)

        css = pcapfile.read(2)
        chanspec = pcapfile.read(2)
        chipvers = pcapfile.read(2)

        csi.set_magic(magic)
        csi.set_mac(mac_1, mac_2, mac_3)
        csi.set_fcsc(fc, sc)
        csi.set_rssi(rssi)
        csi.set_resr(resr)
        csi.set_conf(css, chanspec, chipvers)

        # ----------***** CSI Data *****----------
        len_csi = int(self.bandwidth * 3.2 * 4)
        raw_csi = np.frombuffer(
            pcapfile.read(len_incl - 86)[:len_csi], 
            dtype = np.int16,
            count = int(len_csi/2)
        )

        csi_converted = np.abs(
            np.fft.fftshift(raw_csi[::2] + 1.j * raw_csi[1::2])
        )

        csi.set_csi(csi_converted)
        return csi

    def __read(self):
        with open(self.filepath, 'rb') as pcapfile:
            filesize = os.stat(self.filepath).st_size
            self.__read_header(pcapfile)

            npackets = 0
            while pcapfile.tell() < filesize:
                self.samples.append(self.__read_frame(pcapfile))
                npackets += 1
    
    def get_sample(self, sample_index):
        return self.samples[sample_index]

    def get_max_index(self):
        return len(self.samples) - 1
        


