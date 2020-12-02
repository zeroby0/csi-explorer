Management = {
    'Type': 'Management',
    0b0000: 'Association Request',
    0b0001: 'Association Response',
    0b0010: 'Reassociation Request',
    0b0011: 'Reassociation Response',
    0b0100: 'Probe Request',
    0b0101: 'Probe Response',
    0b0110: 'Timing Advertisement',
    0b0111: 'Reserved',
    0b1000: 'Beacon',
    0b1001: 'ATIM',
    0b1010: 'Disassociation',
    0b1011: 'Authentication',
    0b1100: 'Deauthentication',
    0b1101: 'Action',
    0b1110: 'Action No Ack (NACK)',
    0b1111: 'Reserved'
}

Control = {
    'Type': 'Control',
    0b0000: 'Reserved',
    0b0001: 'Reserved',
    0b0010: 'Trigger',
    0b0011: 'TACK',
    0b0100: 'Beamforming Report Poll',
    0b0101: 'VHT/HE NDP Announcement',
    0b0110: 'Control Frame Extension',
    0b0111: 'Control Wrapper',
    0b1000: 'Block Ack Request (BAR)',
    0b1001: 'Block Ack (BA)',
    0b1010: 'PS-Poll',
    0b1011: 'RTS',
    0b1100: 'CTS',
    0b1101: 'ACK',
    0b1110: 'CF-End',
    0b1111: 'CF-End + CF-ACK'
}

Data = {
    'Type': 'Data',
    0b0000: 'Data',
    0b0001: 'Data + CF-ACK',
    0b0010: 'Data + CF-Poll',
    0b0011: 'Data + CF-ACK + CF-Poll',
    0b0100: 'Null (no data)',
    0b0101: 'CF-ACK (no data)',
    0b0110: 'CF-Poll (no data)',
    0b0111: 'CF-ACK + CF-Poll (no data)',
    0b1000: 'QoS Data',
    0b1001: 'QoS Data + CF-ACK',
    0b1010: 'QoS Data + CF-Poll',
    0b1011: 'QoS Data + CF-ACK + CF-Poll',
    0b1100: 'QoS Null (no data)',
    0b1101: 'Reserved',
    0b1110: 'QoS CF-Poll (no data)',
    0b1111: 'QoS CF-ACK + CF-Poll (no data)'
}

Extension = {
    'Type': 'Extension',
    0b0000: 'DMG Beacon',
    0b0001: 'S1G Beacon',
    0b0010: 'Reserved',
    0b0011: 'Reserved',
    0b0100: 'Reserved',
    0b0101: 'Reserved',
    0b0110: 'Reserved',
    0b0111: 'Reserved',
    0b1000: 'Reserved',
    0b1001: 'Reserved',
    0b1010: 'Reserved',
    0b1011: 'Reserved',
    0b1100: 'Reserved',
    0b1101: 'Reserved',
    0b1110: 'Reserved',
    0b1111: 'Reserved'
}

TypeMap = {
    0b0000: Management,
    0b0100: Control,
    0b1000: Data,
    0b1100: Extension
}