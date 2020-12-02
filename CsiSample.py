import numpy as np
import PacketTypes

class Sample():
    def __init__(self, bandwidth):
        self.bandwidth = bandwidth


    def set_ts(self, ts_s, ts_u):
        self.ts = ts_s + ts_u*10**-6
    
    def set_len(self, len_incl, len_orig):
        self.len_incl = len_incl
        self.len_orig = len_orig

    def set_magic(self, magic):
        self.magic = magic
    
    def set_mac(self, mac_1, mac_2, mac_3):
        self.mac_1 = mac_1
        self.mac_2 = mac_2
        self.mac_3 = mac_3
    
    def set_fcsc(self, fc, sc):
        
        fn = sc % 16 # Fragment number
        sc = int((sc - fn)/16)

        self.fc = fc
        self.sc = sc
        self.fn = fn

        maintype = (fc[0]  & 0x0f)
        subtype  = ((fc[0] >> 4) & 0x0f)

        self.type    = PacketTypes.TypeMap[maintype]['Type']
        self.subtype = PacketTypes.TypeMap[maintype][subtype]

    
    def set_rssi(self, rssi):
        self.rssi = rssi
    
    def set_resr(self, resr):
        self.resr = resr
    
    
    def set_conf(self, css, chanspec, chipvers):
        self.css = css
        self.chanspec = chanspec
        self.chipvers = chipvers
    
    def set_csi(self, csi):
        # csi should be a numpy array
        self.csi = csi

    def get_csi(self, remove_null=False, remove_pilot=False, max_value=0):

        nullsubcarriers  = np.array([x+128 for x in [-128, -127, -126, -125, -124, -123, -1, 0, 1, 123, 124, 125, 126, 127]])
        pilotsubcarriers = np.array([x+128 for x in [-103, -75, -39, -11, 11, 39, 75, 103]])

        new_csi = np.copy(self.csi)

        if(remove_null):
            new_csi[nullsubcarriers] = 0
        if(remove_pilot):
            new_csi[pilotsubcarriers] = 0
        if(max_value > 0):
            new_csi[new_csi > max_value] = 0
        
        return new_csi
        
        
    def __str__(self):

        def macify(mac):
            mac = mac.hex()
            mac = [mac[0:2], mac[2:4], mac[4:6], mac[6:8], mac[8:10], mac[10:12]]
            return ':'.join(mac)

        return '''
        Type:      %s.%s
        FC:        0x%s
        SC:        %d.%d
        RSSI:      %d
        Mac_1:     %s
        Mac_2:     %s
        Mac_3:     %s
        Len_incl:  %d bytes
        Len_orig:  %d bytes
        Bandwidth: %d MHz
        Timestamp: %f s
        Magic:     %s
        RESR:      %s
        ''' % (
            self.type,
            self.subtype,
            self.fc.hex(),
            self.sc,
            self.fn,
            self.rssi,
            macify(self.mac_1),
            macify(self.mac_2),
            macify(self.mac_3),
            self.len_incl,
            self.len_orig,
            self.bandwidth,
            self.ts,
            self.magic.hex(),
            str(self.resr)
        )