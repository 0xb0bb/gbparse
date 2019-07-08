#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

BANK_SIZE = 0x4000

OLD_LICENSEE = {
    0x00: 'None',
    0x01: 'Nintendo R&D',
    0x08: 'Capcom',
    0x09: 'Hot-B',
    0x0a: 'Jaleco',
    0x0b: 'Coconuts',
    0x0c: 'Elite Systems',
    0x13: 'Electronic Arts',
    0x18: 'Hudson Soft',
    0x19: 'ITC Entertainment',
    0x1a: 'Yanoman',
    0x1d: 'Clary',
    0x1f: 'Virgin',
    0x20: 'KSS',
    0x24: 'PCM Complete',
    0x25: 'San-X',
    0x28: 'Kotobuki Systems',
    0x29: 'SETA',
    0x30: 'Infogrames',
    0x31: 'Nintendo',
    0x32: 'Bandai',
    0x33: 'GBC_GAME',
    0x34: 'Konami',
    0x35: 'Hector',
    0x38: 'Capcom',
    0x39: 'Banpresto',
    0x3c: '',
    0x3e: 'Gremlin',
    0x41: 'Ubisoft',
    0x42: 'Atlus',
    0x44: 'Malibu',
    0x46: 'Angel',
    0x47: 'Spectrum Holobyte',
    0x49: 'Irem',
    0x4a: 'Virgin',
    0x4d: 'Malibu',
    0x4f: 'U.S. Gold',
    0x50: 'Absolute',
    0x51: 'Acclaim',
    0x52: 'Activision',
    0x53: 'American Sammy Corporation',
    0x54: 'GameTek',
    0x55: 'Park Place',
    0x56: 'LJN',
    0x57: 'Matchbox',
    0x59: 'Milton Bradley',
    0x5a: 'Mindscape',
    0x5b: 'Romstar',
    0x5c: 'Naxat Soft',
    0x5d: 'Tradewest',
    0x60: 'Titus',
    0x61: 'Virgin',
    0x67: 'Ocean',
    0x69: 'Electronic Arts',
    0x6e: 'Elite Systems',
    0x6f: 'Electro Brain',
    0x70: 'Infogrames',
    0x71: 'Interplay',
    0x72: 'Broderbund',
    0x73: 'Sculptured Soft',
    0x75: 'Sales Curve',
    0x78: 'THQ',
    0x79: 'Accolade',
    0x7a: 'Triffix Entertainment',
    0x7c: 'Microprose',
    0x7f: 'Kemco',
    0x80: 'Misawa Entertainment',
    0x83: 'LOZC',
    0x86: 'Tokuma Shoten',
    0x8b: 'Bullet-Proof',
    0x8c: 'Vic Tokai',
    0x8e: 'Ape',
    0x8f: 'I\'Max',
    0x91: 'Chunsoft',
    0x92: 'Video System',
    0x93: 'Tsuburava',
    0x95: 'Varie',
    0x96: 'Yonezawa S\'pal',
    0x97: 'Kaneko',
    0x99: 'Arc',
    0x9a: 'Nihon Bussan',
    0x9b: 'Tecmo',
    0x9c: 'Imagineer',
    0x9d: 'Banpresto',
    0x9f: 'Nova',
    0xa1: 'Hori Electric',
    0xa2: 'Bandai',
    0xa4: 'Konami',
    0xa6: 'Kawada',
    0xa7: 'Takara',
    0xa9: 'Technos Japan',
    0xaa: 'Broderbund',
    0xac: 'Toei Animation',
    0xad: 'Toho',
    0xaf: 'Namco',
    0xb0: 'Acclaim',
    0xb1: 'NEXOFT',
    0xb2: 'Bandai',
    0xb4: 'Enix',
    0xb6: 'HAL',
    0xb7: 'SNK',
    0xb9: 'Pony Canyon',
    0xba: 'Culture Brain',
    0xbb: 'Sunsoft',
    0xbd: 'Sony Imagesoft',
    0xbf: 'American Sammy Corporation',
    0xc0: 'Taito',
    0xc2: 'Kemco',
    0xc3: 'Squaresoft',
    0xc4: 'Tokuma Shoten Intermedia',
    0xc5: 'Data East',
    0xc6: 'Tonkin House',
    0xc8: 'Koei',
    0xc9: 'UFL',
    0xca: 'Ultra',
    0xcb: 'Vap',
    0xcc: 'Use',
    0xcd: 'Meldac',
    0xce: 'Pony Canyon',
    0xcf: 'Angel',
    0xd0: 'Taito',
    0xd1: 'Sofel',
    0xd2: 'Quest',
    0xd3: 'Sigma Enterprises',
    0xd4: 'Ask Kodansha',
    0xd6: 'Naxat Soft ',
    0xd7: 'Copya Systems',
    0xd9: 'Banpresto',
    0xda: 'Tomy',
    0xdb: 'LJN',
    0xdd: 'NCS',
    0xde: 'Human',
    0xdf: 'Altron',
    0xe0: 'Jaleco',
    0xe1: 'Towachiki',
    0xe2: 'Yutaka',
    0xe3: 'Varie',
    0xe5: 'Epoch',
    0xe7: 'Athena',
    0xe8: 'Asmik',
    0xe9: 'Natsume',
    0xea: 'King Records',
    0xeb: 'Atlus',
    0xec: 'Epic / Sony Records',
    0xee: 'IGS',
    0xf0: 'A-Wave',
    0xf3: 'Extreme Entertainment',
    0xff: 'LJN',
}

NEW_LICENSEE = {
    0x00: 'None',
    0x01: 'Nintendo R&D',
    0x08: 'Capcom',
    0x13: 'Electronic Arts',
    0x18: 'Hudson Soft',
    0x19: 'B-AI',
    0x20: 'KSS',
    0x22: 'POW',
    0x24: 'PCM Complete',
    0x25: 'San-X',
    0x28: 'Kemco Japan',
    0x29: 'SETA',
    0x30: 'Viacom',
    0x31: 'Nintendo',
    0x32: 'Bandai',
    0x33: 'Ocean/Acclaim',
    0x34: 'Konami',
    0x35: 'Hector',
    0x37: 'Taito',
    0x38: 'Hudson',
    0x39: 'Banpresto',
    0x41: 'Ubisoft',
    0x42: 'Atlus',
    0x44: 'Malibu',
    0x46: 'Angel',
    0x47: 'Bullet-Proof',
    0x49: 'Irem.',
    0x50: 'Absolute',
    0x51: 'Acclaim',
    0x52: 'Activision',
    0x53: 'American Sammy Corporation',
    0x54: 'Konami',
    0x55: 'Hi Tech Entertainment',
    0x56: 'LJN',
    0x57: 'Matchbox',
    0x58: 'Mattel',
    0x59: 'Milton Bradley',
    0x60: 'Titus',
    0x61: 'Virgin',
    0x64: 'LucasArts',
    0x67: 'Ocean',
    0x69: 'Electronic Arts',
    0x70: 'Infogrames',
    0x71: 'Interplay',
    0x72: 'Broderbund',
    0x73: 'Sculptured',
    0x75: 'SCI',
    0x78: 'THQ',
    0x79: 'Accolade',
    0x80: 'Misawa',
    0x83: 'LOZC',
    0x86: 'Tokuma Shoten',
    0x87: 'Tsukuda Original',
    0x91: 'Chunsoft',
    0x92: 'Video System',
    0x93: 'Ocean/Acclaim',
    0x95: 'Varie',
    0x96: 'Yonezawa / S\'pal',
    0x97: 'Kaneko',
    0x99: 'Pack-In-Video',
    0xa4: 'Konami (Yu-Gi-Oh!)',
}

ROM_SIZE = {
    0x00: BANK_SIZE * 0x002,  # no ROM banking
    0x01: BANK_SIZE * 0x004,
    0x02: BANK_SIZE * 0x008,
    0x03: BANK_SIZE * 0x010,
    0x04: BANK_SIZE * 0x020,
    0x05: BANK_SIZE * 0x040,  # only 0x3f banks used by MBC1
    0x06: BANK_SIZE * 0x080,  # only 0x7d banks used by MBC1
    0x07: BANK_SIZE * 0x100,
    0x08: BANK_SIZE * 0x200,
    0x52: BANK_SIZE * 0x048,
    0x53: BANK_SIZE * 0x050,
    0x54: BANK_SIZE * 0x060,
}

RAM_SIZE = {
    0x00: 0x00 * 0x400,       #  None
    0x01: 0x02 * 0x400,       #   2kb
    0x02: 0x08 * 0x400,       #   8kb
    0x03: 0x20 * 0x400,       #  32kb ( 4 banks)
    0x04: 0x80 * 0x400,       # 128kb (16 banks)
    0x05: 0x40 * 0x400,       #  64kb ( 8 banks)
}

CART_TYPE = {
    0x00: 'ROM ONLY',
    0x01: 'MBC1',
    0x02: 'MBC1+RAM',
    0x03: 'MBC1+RAM+BATTERY',
    0x05: 'MBC2',
    0x06: 'MBC2+BATTERY',
    0x08: 'ROM+RAM',
    0x09: 'ROM+RAM+BATTERY',
    0x0b: 'MMM01',
    0x0c: 'MMM01+RAM',
    0x0d: 'MMM01+RAM+BATTERY',
    0x0f: 'MBC3+TIMER+BATTERY',
    0x10: 'MBC3+TIMER+RAM+BATTERY',
    0x11: 'MBC3',
    0x12: 'MBC3+RAM',
    0x13: 'MBC3+RAM+BATTERY',
    0x19: 'MBC5',
    0x1a: 'MBC5+RAM',
    0x1b: 'MBC5+RAM+BATTERY',
    0x1c: 'MBC5+RUMBLE',
    0x1d: 'MBC5+RUMBLE+RAM',
    0x1e: 'MBC5+RUMBLE+RAM+BATTERY',
    0x20: 'MBC6',
    0x22: 'MBC7+SENSOR+RUMBLE+RAM+BATTERY',
    0xfc: 'POCKET CAMERA',
    0xfd: 'BANDAI TAMA5',
    0xfe: 'HuC3',
    0xff: 'HuC1+RAM+BATTERY',
}

IO_REGS = {
    
    0xff00: 'joypad (P1/JOYP)',
    0xff01: 'serial data (SB)',
    0xff02: 'serial control (SC)',
    0xff04: 'divider (DIV)',
    0xff05: 'timer counter (TIMA)',
    0xff06: 'timer modulo (TMA)',
    0xff07: 'timer control (TAC)',
    0xff0f: 'interrupt flag (IF)',
    0xff10: 'channel 1 sweep (NR10)',
    0xff11: 'channel 1 sound length (NR11)',
    0xff12: 'channel 1 volume envelope (NR12)',
    0xff13: 'channel 1 frequency low (NR13)',
    0xff14: 'channel 1 frequency high (NR14)',
    0xff16: 'channel 2 sound length (NR21)',
    0xff17: 'channel 2 volume envelope (NR22)',
    0xff18: 'channel 2 frequency low (NR23)',
    0xff19: 'channel 2 frequency high (NR24)',
    0xff1a: 'channel 3 sound on/off (NR30)',
    0xff1b: 'channel 3 sound length (NR31)',
    0xff1c: 'channel 3 select output level (NR32)',
    0xff1d: 'channel 3 frequency low (NR33)',
    0xff1e: 'channel 3 frequency high (NR34)',
    0xff20: 'channel 4 sound length (NR41)',
    0xff21: 'channel 4 volume envelope (NR42)',
    0xff22: 'channel 4 polynomial counter (NR43)',
    0xff23: 'channel 4 counter (NR44)',
    0xff24: 'channel control (NR50)',
    0xff25: 'sound output terminal (NR51)',
    0xff26: 'sound on/off (NR52)',
    0xff30: 'wave pattern ram',
    0xff31: 'wave pattern ram',
    0xff32: 'wave pattern ram',
    0xff33: 'wave pattern ram',
    0xff34: 'wave pattern ram',
    0xff35: 'wave pattern ram',
    0xff36: 'wave pattern ram',
    0xff37: 'wave pattern ram',
    0xff38: 'wave pattern ram',
    0xff39: 'wave pattern ram',
    0xff3a: 'wave pattern ram',
    0xff3b: 'wave pattern ram',
    0xff3c: 'wave pattern ram',
    0xff3d: 'wave pattern ram',
    0xff3e: 'wave pattern ram',
    0xff3f: 'wave pattern ram',
    0xff40: 'lcd control (LCDC)',
    0xff41: 'lcd status (STAT)',
    0xff42: 'scroll y (SCY)',
    0xff43: 'scroll x (SCX)',
    0xff44: 'lcd y-coordinate (LY)',
    0xff45: 'lcd y-coordinate compare (LYC)',
    0xff46: 'dma transfer (DMA)',
    0xff47: 'background palette (BGP)',
    0xff48: 'object palette 0 (OBP0)',
    0xff49: 'object palette 1 (OBP1)',
    0xff4a: 'window y position (WY)',
    0xff4b: 'window x position minus 7 (WX)',
    0xff4d: 'speed switch (KEY1)',
    0xff4f: 'vram bank (VBK)',
    0xff50: 'disable bootrom',
    0xff51: 'dma source, high (HDMA1)',
    0xff52: 'dma source, low (HDMA2)',
    0xff53: 'dma destination, high (HDMA3)',
    0xff54: 'dma destination, low (HDMA4)',
    0xff55: 'dma length/mode/start (HDMA5)',
    0xff56: 'infrared port (RP)',
    0xff68: 'background palette index (BGPI)',
    0xff69: 'background palette data (BGPD)',
    0xff6a: 'sprite palette index (OBPI)',
    0xff6b: 'sprite palette data (OBPD)',
    0xff6c: 'undocumented',
    0xff70: 'wram bank (SVBK)',
    0xff72: 'undocumented',
    0xff73: 'undocumented',
    0xff74: 'undocumented',
    0xff75: 'undocumented',
    0xff76: 'undocumented',
    0xff77: 'undocumented',

    0xffff: 'interrupt enable',
}

INS = {
    0x00: { 'size': 1,  'mnem': 'nop', },
    0x01: { 'size': 3,  'mnem': 'ld    bc, _WORD_', },
    0x02: { 'size': 1,  'mnem': 'ld    [bc], a', },
    0x03: { 'size': 1,  'mnem': 'inc   bc', },
    0x04: { 'size': 1,  'mnem': 'inc   b', },
    0x05: { 'size': 1,  'mnem': 'dec   b', },
    0x06: { 'size': 2,  'mnem': 'ld    b, _BYTE_', },
    0x07: { 'size': 1,  'mnem': 'rlca', },
    0x08: { 'size': 3,  'mnem': 'ld    [_WORD_], sp', },
    0x09: { 'size': 1,  'mnem': 'add   hl, bc', },
    0x0a: { 'size': 1,  'mnem': 'ld    a, [bc]', },
    0x0b: { 'size': 1,  'mnem': 'dec   bc', },
    0x0c: { 'size': 1,  'mnem': 'inc   c', },
    0x0d: { 'size': 1,  'mnem': 'dec   c', },
    0x0e: { 'size': 2,  'mnem': 'ld    c, _BYTE_', },
    0x0f: { 'size': 1,  'mnem': 'rrca', },
    0x10: { 'size': 1,  'mnem': 'stop', },
    0x11: { 'size': 3,  'mnem': 'ld    de, _WORD_', },
    0x12: { 'size': 1,  'mnem': 'ld    [de], a', },
    0x13: { 'size': 1,  'mnem': 'inc   de', },
    0x14: { 'size': 1,  'mnem': 'inc   d', },
    0x15: { 'size': 1,  'mnem': 'dec   d', },
    0x16: { 'size': 2,  'mnem': 'ld    d, _BYTE_', },
    0x17: { 'size': 1,  'mnem': 'rla', },
    0x18: { 'size': 2,  'mnem': 'jr    _DEC_', },
    0x19: { 'size': 1,  'mnem': 'add   hl, de', },
    0x1a: { 'size': 1,  'mnem': 'ld    a, [de]', },
    0x1b: { 'size': 1,  'mnem': 'dec   de', },
    0x1c: { 'size': 1,  'mnem': 'inc   e', },
    0x1d: { 'size': 1,  'mnem': 'dec   e', },
    0x1e: { 'size': 2,  'mnem': 'ld    e, _BYTE_', },
    0x1f: { 'size': 1,  'mnem': 'rra', },
    0x20: { 'size': 2,  'mnem': 'jr    nz, _DEC_', },
    0x21: { 'size': 3,  'mnem': 'ld    hl, _WORD_', },
    0x22: { 'size': 1,  'mnem': 'ld    [hli], a', },
    0x23: { 'size': 1,  'mnem': 'inc   hl', },
    0x24: { 'size': 1,  'mnem': 'inc   h', },
    0x25: { 'size': 1,  'mnem': 'dec   h', },
    0x26: { 'size': 2,  'mnem': 'ld    h, _BYTE_', },
    0x27: { 'size': 1,  'mnem': 'daa', },
    0x28: { 'size': 2,  'mnem': 'jr    z, _DEC_', },
    0x29: { 'size': 1,  'mnem': 'add   hl, hl', },
    0x2a: { 'size': 1,  'mnem': 'ld    a, [hli]', },
    0x2b: { 'size': 1,  'mnem': 'dec   hl', },
    0x2c: { 'size': 1,  'mnem': 'inc   l', },
    0x2d: { 'size': 1,  'mnem': 'dec   l', },
    0x2e: { 'size': 2,  'mnem': 'ld    l, _BYTE_', },
    0x2f: { 'size': 1,  'mnem': 'cpl', },
    0x30: { 'size': 2,  'mnem': 'jr    nc, _DEC_', },
    0x31: { 'size': 3,  'mnem': 'ld    sp, _WORD_', },
    0x32: { 'size': 1,  'mnem': 'ld    [hld], a', },
    0x33: { 'size': 1,  'mnem': 'inc   sp', },
    0x34: { 'size': 1,  'mnem': 'inc   [hl]', },
    0x35: { 'size': 1,  'mnem': 'dec   [hl]', },
    0x36: { 'size': 2,  'mnem': 'ld    [hl], _BYTE_', },
    0x37: { 'size': 1,  'mnem': 'scf', },
    0x38: { 'size': 2,  'mnem': 'jr    c, _DEC_', },
    0x39: { 'size': 1,  'mnem': 'add   hl, sp', },
    0x3a: { 'size': 1,  'mnem': 'ld    a, [hld]', },
    0x3b: { 'size': 1,  'mnem': 'dec   sp', },
    0x3c: { 'size': 1,  'mnem': 'inc   a', },
    0x3d: { 'size': 1,  'mnem': 'dec   a', },
    0x3e: { 'size': 2,  'mnem': 'ld    a, _BYTE_', },
    0x3f: { 'size': 1,  'mnem': 'ccf', },
    0x40: { 'size': 1,  'mnem': 'ld    b, b', },
    0x41: { 'size': 1,  'mnem': 'ld    b, c', },
    0x42: { 'size': 1,  'mnem': 'ld    b, d', },
    0x43: { 'size': 1,  'mnem': 'ld    b, e', },
    0x44: { 'size': 1,  'mnem': 'ld    b, h', },
    0x45: { 'size': 1,  'mnem': 'ld    b, l', },
    0x46: { 'size': 1,  'mnem': 'ld    b, [hl]', },
    0x47: { 'size': 1,  'mnem': 'ld    b, a', },
    0x48: { 'size': 1,  'mnem': 'ld    c, b', },
    0x49: { 'size': 1,  'mnem': 'ld    c, c', },
    0x4a: { 'size': 1,  'mnem': 'ld    c, d', },
    0x4b: { 'size': 1,  'mnem': 'ld    c, e', },
    0x4c: { 'size': 1,  'mnem': 'ld    c, h', },
    0x4d: { 'size': 1,  'mnem': 'ld    c, l', },
    0x4e: { 'size': 1,  'mnem': 'ld    c, [hl]', },
    0x4f: { 'size': 1,  'mnem': 'ld    c, a', },
    0x50: { 'size': 1,  'mnem': 'ld    d, b', },
    0x51: { 'size': 1,  'mnem': 'ld    d, c', },
    0x52: { 'size': 1,  'mnem': 'ld    d, d', },
    0x53: { 'size': 1,  'mnem': 'ld    d, e', },
    0x54: { 'size': 1,  'mnem': 'ld    d, h', },
    0x55: { 'size': 1,  'mnem': 'ld    d, l', },
    0x56: { 'size': 1,  'mnem': 'ld    d, [hl]', },
    0x57: { 'size': 1,  'mnem': 'ld    d, a', },
    0x58: { 'size': 1,  'mnem': 'ld    e, b', },
    0x59: { 'size': 1,  'mnem': 'ld    e, c', },
    0x5a: { 'size': 1,  'mnem': 'ld    e, d', },
    0x5b: { 'size': 1,  'mnem': 'ld    e, e', },
    0x5c: { 'size': 1,  'mnem': 'ld    e, h', },
    0x5d: { 'size': 1,  'mnem': 'ld    e, l', },
    0x5e: { 'size': 1,  'mnem': 'ld    e, [hl]', },
    0x5f: { 'size': 1,  'mnem': 'ld    e, a', },
    0x60: { 'size': 1,  'mnem': 'ld    h, b', },
    0x61: { 'size': 1,  'mnem': 'ld    h, c', },
    0x62: { 'size': 1,  'mnem': 'ld    h, d', },
    0x63: { 'size': 1,  'mnem': 'ld    h, e', },
    0x64: { 'size': 1,  'mnem': 'ld    h, h', },
    0x65: { 'size': 1,  'mnem': 'ld    h, l', },
    0x66: { 'size': 1,  'mnem': 'ld    h, [hl]', },
    0x67: { 'size': 1,  'mnem': 'ld    h, a', },
    0x68: { 'size': 1,  'mnem': 'ld    l, b', },
    0x69: { 'size': 1,  'mnem': 'ld    l, c', },
    0x6a: { 'size': 1,  'mnem': 'ld    l, d', },
    0x6b: { 'size': 1,  'mnem': 'ld    l, e', },
    0x6c: { 'size': 1,  'mnem': 'ld    l, h', },
    0x6d: { 'size': 1,  'mnem': 'ld    l, l', },
    0x6e: { 'size': 1,  'mnem': 'ld    l, [hl]', },
    0x6f: { 'size': 1,  'mnem': 'ld    l, a', },
    0x70: { 'size': 1,  'mnem': 'ld    [hl], b', },
    0x71: { 'size': 1,  'mnem': 'ld    [hl], c', },
    0x72: { 'size': 1,  'mnem': 'ld    [hl], d', },
    0x73: { 'size': 1,  'mnem': 'ld    [hl], e', },
    0x74: { 'size': 1,  'mnem': 'ld    [hl], h', },
    0x75: { 'size': 1,  'mnem': 'ld    [hl], l', },
    0x76: { 'size': 1,  'mnem': 'halt', },
    0x77: { 'size': 1,  'mnem': 'ld    [hl], a', },
    0x78: { 'size': 1,  'mnem': 'ld    a, b', },
    0x79: { 'size': 1,  'mnem': 'ld    a, c', },
    0x7a: { 'size': 1,  'mnem': 'ld    a, d', },
    0x7b: { 'size': 1,  'mnem': 'ld    a, e', },
    0x7c: { 'size': 1,  'mnem': 'ld    a, h', },
    0x7d: { 'size': 1,  'mnem': 'ld    a, l', },
    0x7e: { 'size': 1,  'mnem': 'ld    a, [hl]', },
    0x7f: { 'size': 1,  'mnem': 'ld    a, a', },
    0x80: { 'size': 1,  'mnem': 'add   a, b', },
    0x81: { 'size': 1,  'mnem': 'add   a, c', },
    0x82: { 'size': 1,  'mnem': 'add   a, d', },
    0x83: { 'size': 1,  'mnem': 'add   a, e', },
    0x84: { 'size': 1,  'mnem': 'add   a, h', },
    0x85: { 'size': 1,  'mnem': 'add   a, l', },
    0x86: { 'size': 1,  'mnem': 'add   a, [hl]', },
    0x87: { 'size': 1,  'mnem': 'add   a, a', },
    0x88: { 'size': 1,  'mnem': 'adc   a, b', },
    0x89: { 'size': 1,  'mnem': 'adc   a, c', },
    0x8a: { 'size': 1,  'mnem': 'adc   a, d', },
    0x8b: { 'size': 1,  'mnem': 'adc   a, e', },
    0x8c: { 'size': 1,  'mnem': 'adc   a, h', },
    0x8d: { 'size': 1,  'mnem': 'adc   a, l', },
    0x8e: { 'size': 1,  'mnem': 'adc   a, [hl]', },
    0x8f: { 'size': 1,  'mnem': 'adc   a', },
    0x90: { 'size': 1,  'mnem': 'sub   b', },
    0x91: { 'size': 1,  'mnem': 'sub   c', },
    0x92: { 'size': 1,  'mnem': 'sub   d', },
    0x93: { 'size': 1,  'mnem': 'sub   e', },
    0x94: { 'size': 1,  'mnem': 'sub   h', },
    0x95: { 'size': 1,  'mnem': 'sub   l', },
    0x96: { 'size': 1,  'mnem': 'sub   [hl]', },
    0x97: { 'size': 1,  'mnem': 'sub   a', },
    0x98: { 'size': 1,  'mnem': 'sbc   a, b', },
    0x99: { 'size': 1,  'mnem': 'sbc   a, c', },
    0x9a: { 'size': 1,  'mnem': 'sbc   a, d', },
    0x9b: { 'size': 1,  'mnem': 'sbc   a, e', },
    0x9c: { 'size': 1,  'mnem': 'sbc   a, h', },
    0x9d: { 'size': 1,  'mnem': 'sbc   a, l', },
    0x9e: { 'size': 1,  'mnem': 'sbc   a, [hl]', },
    0x9f: { 'size': 1,  'mnem': 'sbc   a,a', },
    0xa0: { 'size': 1,  'mnem': 'and   b', },
    0xa1: { 'size': 1,  'mnem': 'and   c', },
    0xa2: { 'size': 1,  'mnem': 'and   d', },
    0xa3: { 'size': 1,  'mnem': 'and   e', },
    0xa4: { 'size': 1,  'mnem': 'and   h', },
    0xa5: { 'size': 1,  'mnem': 'and   l', },
    0xa6: { 'size': 1,  'mnem': 'and   [hl]', },
    0xa7: { 'size': 1,  'mnem': 'and   a', },
    0xa8: { 'size': 1,  'mnem': 'xor   b', },
    0xa9: { 'size': 1,  'mnem': 'xor   c', },
    0xaa: { 'size': 1,  'mnem': 'xor   d', },
    0xab: { 'size': 1,  'mnem': 'xor   e', },
    0xac: { 'size': 1,  'mnem': 'xor   h', },
    0xad: { 'size': 1,  'mnem': 'xor   l', },
    0xae: { 'size': 1,  'mnem': 'xor   [hl]', },
    0xaf: { 'size': 1,  'mnem': 'xor   a', },
    0xb0: { 'size': 1,  'mnem': 'or    b', },
    0xb1: { 'size': 1,  'mnem': 'or    c', },
    0xb2: { 'size': 1,  'mnem': 'or    d', },
    0xb3: { 'size': 1,  'mnem': 'or    e', },
    0xb4: { 'size': 1,  'mnem': 'or    h', },
    0xb5: { 'size': 1,  'mnem': 'or    l', },
    0xb6: { 'size': 1,  'mnem': 'or    [hl]', },
    0xb7: { 'size': 1,  'mnem': 'or    a', },
    0xb8: { 'size': 1,  'mnem': 'cp    b', },
    0xb9: { 'size': 1,  'mnem': 'cp    c', },
    0xba: { 'size': 1,  'mnem': 'cp    d', },
    0xbb: { 'size': 1,  'mnem': 'cp    e', },
    0xbc: { 'size': 1,  'mnem': 'cp    h', },
    0xbd: { 'size': 1,  'mnem': 'cp    l', },
    0xbe: { 'size': 1,  'mnem': 'cp    [hl]', },
    0xbf: { 'size': 1,  'mnem': 'cp    a', },
    0xc0: { 'size': 1,  'mnem': 'ret   nz', },
    0xc1: { 'size': 1,  'mnem': 'pop   bc', },
    0xc2: { 'size': 3,  'mnem': 'jp    nz, _WORD_', },
    0xc3: { 'size': 3,  'mnem': 'jp    _WORD_', },
    0xc4: { 'size': 3,  'mnem': 'call  nz, _WORD_', },
    0xc5: { 'size': 1,  'mnem': 'push  bc', },
    0xc6: { 'size': 2,  'mnem': 'add   a, _BYTE_', },
    0xc7: { 'size': 1,  'mnem': 'rst   0x00', },
    0xc8: { 'size': 1,  'mnem': 'ret   z', },
    0xc9: { 'size': 1,  'mnem': 'ret', },
    0xca: { 'size': 3,  'mnem': 'jp    z, _WORD_', },
    0xcc: { 'size': 3,  'mnem': 'call  z, _WORD_', },
    0xcd: { 'size': 3,  'mnem': 'call  _WORD_', },
    0xce: { 'size': 2,  'mnem': 'adc   a, _BYTE_', },
    0xcf: { 'size': 1,  'mnem': 'rst   0x08', },
    0xd0: { 'size': 1,  'mnem': 'ret   nc', },
    0xd1: { 'size': 1,  'mnem': 'pop   de', },
    0xd2: { 'size': 3,  'mnem': 'jp    nc, _WORD_', },
    0xd4: { 'size': 3,  'mnem': 'call  nc, _WORD_', },
    0xd5: { 'size': 1,  'mnem': 'push  de', },
    0xd6: { 'size': 2,  'mnem': 'sub   _BYTE_', },
    0xd7: { 'size': 1,  'mnem': 'rst   0x10', },
    0xd8: { 'size': 1,  'mnem': 'ret   c', },
    0xd9: { 'size': 1,  'mnem': 'reti', },
    0xda: { 'size': 3,  'mnem': 'jp    c,_WORD_', },
    0xdc: { 'size': 3,  'mnem': 'call  c,_WORD_', },
    0xde: { 'size': 2,  'mnem': 'sbc   a,_BYTE_', },
    0xdf: { 'size': 1,  'mnem': 'rst   0x18', },
    0xe0: { 'size': 2,  'mnem': 'ld    [0xff00+_BYTE_], a', },
    0xe1: { 'size': 1,  'mnem': 'pop   hl', },
    0xe2: { 'size': 1,  'mnem': 'ld    [0xff00+c], a', },
    0xe5: { 'size': 1,  'mnem': 'push  hl', },
    0xe6: { 'size': 2,  'mnem': 'and   _BYTE_', },
    0xe7: { 'size': 1,  'mnem': 'rst   0x20', },
    0xe8: { 'size': 2,  'mnem': 'add   sp, _DEC_', },
    0xe9: { 'size': 1,  'mnem': 'jp    hl', },
    0xea: { 'size': 3,  'mnem': 'ld    [_WORD_], a', },
    0xee: { 'size': 2,  'mnem': 'xor   _BYTE_', },
    0xef: { 'size': 1,  'mnem': 'rst   0x28', },
    0xf0: { 'size': 2,  'mnem': 'ld    a, [0xff00+_BYTE_]', },
    0xf1: { 'size': 1,  'mnem': 'pop   af', },
    0xf2: { 'size': 1,  'mnem': 'ld    a, [0xff00+c]', },
    0xf3: { 'size': 1,  'mnem': 'di', },
    0xf5: { 'size': 1,  'mnem': 'push  af', },
    0xf6: { 'size': 2,  'mnem': 'or    _BYTE_', },
    0xf7: { 'size': 1,  'mnem': 'rst   0x30', },
    0xf8: { 'size': 2,  'mnem': 'ld    hl, sp_DEC_', },
    0xf9: { 'size': 1,  'mnem': 'ld    sp, hl', },
    0xfa: { 'size': 3,  'mnem': 'ld    a, [_WORD_]', },
    0xfb: { 'size': 1,  'mnem': 'ei', },
    0xfe: { 'size': 2,  'mnem': 'cp    _BYTE_', },
    0xff: { 'size': 1,  'mnem': 'rst   0x38', },
}

CB_INS = [
    'rlc   b',    'rlc   c',    'rlc   d',       'rlc   e',
    'rlc   h',    'rlc   l',    'rlc   [hl]',    'rlc   a',
    'rrc   b',    'rrc   c',    'rrc   d',       'rrc   e',
    'rrc   h',    'rrc   l',    'rrc   [hl]',    'rrc   a',
    'rl    b',    'rl    c',    'rl    d',       'rl    e',
    'rl    h',    'rl    l',    'rl    [hl]',    'rl    a',
    'rr    b',    'rr    c',    'rr    d',       'rr    e',
    'rr    h',    'rr    l',    'rr    [hl]',    'rr    a',
    'sla   b',    'sla   c',    'sla   d',       'sla   e',
    'sla   h',    'sla   l',    'sla   [hl]',    'sla   a',
    'sra   b',    'sra   c',    'sra   d',       'sra   e',
    'sra   h',    'sra   l',    'sra   [hl]',    'sra   a',
    'swap  b',    'swap  c',    'swap  d',       'swap  e',
    'swap  h',    'swap  l',    'swap  [hl]',    'swap  a',
    'srl   b',    'srl   c',    'srl   d',       'srl   e',
    'srl   h',    'srl   l',    'srl   [hl]',    'srl   a',
    'bit   0, b', 'bit   0, c', 'bit   0, d',    'bit   0, e',
    'bit   0, h', 'bit   0, l', 'bit   0, [hl]', 'bit   0, a',
    'bit   1, b', 'bit   1, c', 'bit   1, d',    'bit   1, e',
    'bit   1, h', 'bit   1, l', 'bit   1, [hl]', 'bit   1, a',
    'bit   2, b', 'bit   2, c', 'bit   2, d',    'bit   2, e',
    'bit   2, h', 'bit   2, l', 'bit   2, [hl]', 'bit   2, a',
    'bit   3, b', 'bit   3, c', 'bit   3, d',    'bit   3, e',
    'bit   3, h', 'bit   3, l', 'bit   3, [hl]', 'bit   3, a',
    'bit   4, b', 'bit   4, c', 'bit   4, d',    'bit   4, e',
    'bit   4, h', 'bit   4, l', 'bit   4, [hl]', 'bit   4, a',
    'bit   5, b', 'bit   5, c', 'bit   5, d',    'bit   5, e',
    'bit   5, h', 'bit   5, l', 'bit   5, [hl]', 'bit   5, a',
    'bit   6, b', 'bit   6, c', 'bit   6, d',    'bit   6, e',
    'bit   6, h', 'bit   6, l', 'bit   6, [hl]', 'bit   6, a',
    'bit   7, b', 'bit   7, c', 'bit   7, d',    'bit   7, e',
    'bit   7, h', 'bit   7, l', 'bit   7, [hl]', 'bit   7, a',
    'res   0, b', 'res   0, c', 'res   0, d',    'res   0, e',
    'res   0, h', 'res   0, l', 'res   0, [hl]', 'res   0, a',
    'res   1, b', 'res   1, c', 'res   1, d',    'res   1, e',
    'res   1, h', 'res   1, l', 'res   1, [hl]', 'res   1, a',
    'res   2, b', 'res   2, c', 'res   2, d',    'res   2, e',
    'res   2, h', 'res   2, l', 'res   2, [hl]', 'res   2, a',
    'res   3, b', 'res   3, c', 'res   3, d',    'res   3, e',
    'res   3, h', 'res   3, l', 'res   3, [hl]', 'res   3, a',
    'res   4, b', 'res   4, c', 'res   4, d',    'res   4, e',
    'res   4, h', 'res   4, l', 'res   4, [hl]', 'res   4, a',
    'res   5, b', 'res   5, c', 'res   5, d',    'res   5, e',
    'res   5, h', 'res   5, l', 'res   5, [hl]', 'res   5, a',
    'res   6, b', 'res   6, c', 'res   6, d',    'res   6, e',
    'res   6, h', 'res   6, l', 'res   6, [hl]', 'res   6, a',
    'res   7, b', 'res   7, c', 'res   7, d',    'res   7, e',
    'res   7, h', 'res   7, l', 'res   7, [hl]', 'res   7, a',
    'set   0, b', 'set   0, c', 'set   0, d',    'set   0, e',
    'set   0, h', 'set   0, l', 'set   0, [hl]', 'set   0, a',
    'set   1, b', 'set   1, c', 'set   1, d',    'set   1, e',
    'set   1, h', 'set   1, l', 'set   1, [hl]', 'set   1, a',
    'set   2, b', 'set   2, c', 'set   2, d',    'set   2, e',
    'set   2, h', 'set   2, l', 'set   2, [hl]', 'set   2, a',
    'set   3, b', 'set   3, c', 'set   3, d',    'set   3, e',
    'set   3, h', 'set   3, l', 'set   3, [hl]', 'set   3, a',
    'set   4, b', 'set   4, c', 'set   4, d',    'set   4, e',
    'set   4, h', 'set   4, l', 'set   4, [hl]', 'set   4, a',
    'set   5, b', 'set   5, c', 'set   5, d',    'set   5, e',
    'set   5, h', 'set   5, l', 'set   5, [hl]', 'set   5, a',
    'set   6, b', 'set   6, c', 'set   6, d',    'set   6, e',
    'set   6, h', 'set   6, l', 'set   6, [hl]', 'set   6, a',
    'set   7, b', 'set   7, c', 'set   7, d',    'set   7, e',
    'set   7, h', 'set   7, l', 'set   7, [hl]', 'set   7, a',
]

SYMBOLS = {
    0x0000: 'rst00|reset',
    0x0008: 'rst08',
    0x0010: 'rst10',
    0x0018: 'rst18',
    0x0020: 'rst20',
    0x0028: 'rst28',
    0x0030: 'rst30',
    0x0038: 'rst38',
    0x0040: 'int40|vblank interrupt',
    0x0048: 'int48|lcd status interrupt',
    0x0050: 'int50|timer interrupt',
    0x0058: 'int58|serial interrupt',
    0x0060: 'int60|joypad interrupt',
    0x0100: 'start',
}

HANDLERS = {
    0x0040: 'vblank_handler|called on int40',
    0x0048: 'lcds_handler|called on int48',
    0x0050: 'timer_handler|called on int50',
    0x0058: 'serial_handler|called on int58',
    0x0060: 'joypad_handler|called on int60',
}

# 0040,0048,0050,0058,0060


def int8(val):
    val = val & 0xff
    if val > 0x7f:
        return (0x100-val) * (-1)
    else:
        return val

def uint8(val):
    if val < 0:
        return 0x100 + val
    else:
        return val


def firstbit(val, bit):
    n = 0
    while val & 1 == bit:
        val = val >> 1
        n += 1

    return n


def setbit(val, pos, bit):
    mask = 1 << pos
    return (val & ~mask) | ((bit << pos) & mask)


def getbit(val, pos):
    ret = val >> pos
    return ret & 1


def header_check(rom):

    ret = 0
    for i in range(0x19):
        ret = int8(ret) - int8(ord(rom[0x0134+i])) - 1

    return uint8(ret)


def global_check(rom):

    ret = 0
    for i in range(len(rom)):
        if i == 0x014e or i == 0x014f:
            continue

        ret += ord(rom[i])

    return ret & 0xffff


def parse(rom):

    header_sum = ord(rom[0x014d])
    global_sum = (ord(rom[0x014e]) << 8)|ord(rom[0x014f])

    ret = {
        'color': False,                       # Gameboy Color game?
        'japanese': False,                    # Japanese release?
        'sgb': False,                         # Super Gameboy?
        'version': ord(rom[0x014c]),          # Mask ROM version
        'type': CART_TYPE[ord(rom[0x0147])],  # Cartridge type
        'rom': ROM_SIZE[ord(rom[0x0148])],    # ROM size in bytes
        'ram': RAM_SIZE[ord(rom[0x0149])],    # External RAM size in bytes

        'checksums': {
            'header': {
                'check': header_check(rom),   # Calculated checksum
                'stored': header_sum,         # Checksum value in ROM
            },
            'global': {
                'check': global_check(rom),   # Calculated checksum
                'stored': global_sum,         # Checksum value in ROM
            }
        }
    }

    old = True
    if ord(rom[0x014b]) == 0x33:
        old = False

    if old:
        ret['licensee'] = OLD_LICENSEE[ord(rom[0x014b])]
        ret['title'] = rom[0x0134:0x0144].strip('\x00')
    else:
        ret['manufacturer'] = rom[0x013f:0x0143]
        ret['licensee'] = NEW_LICENSEE[int(rom[0x0144]+rom[0x0145], 16)]
        ret['title'] = rom[0x0134:0x013f].strip('\x00')
        ret['color'] = True

    if ord(rom[0x014a]) == 0x00:
        ret['japanese'] = True

    if ord(rom[0x0146]) == 0x00:
        ret['sgb'] = True

    pc = 0x100
    while True:
        if pc >= len(rom):
            break

        op = ord(rom[pc])
        if op in INS:
            if op in [0xc2, 0xc3, 0xc4, 0xca, 0xcc, 0xcd, 0xd2, 0xd4, 0xda, 0xdc]:
                l = ord(rom[pc+1])
                h = ord(rom[pc+2])
                ret['entry'] = (h << 8)|l
                break
            else:
                pc += INS[op]['size']
        else:
            pc += 1

    return ret


def disas(rom, start=0x0000, stop=0x7fff, max_depth=60):

    if stop > len(rom):
        stop = len(rom)

    explore = [
        start,    # start address
        0x0040,   # vblank interrupt
        0x0048,   # lcd status interrupt
        0x0050,   # timer interrupt
        0x0058,   # serial interrupt
        0x0060,   # joypad interrupt
    ]

    blocks = []   # list of explored blocks
    out    = {}   # instruction data to return
    funcs  = {}   # called blocks found
    jumps  = []   # list of relative jumps encountered
    sites  = []   # call and absolute jump locations

    depth = 0     # how deep to explore between blocks
    last  = start # last instruction explored
    addr  = start # current address

    while len(explore) > 0:

        block    = explore.pop(0)  # current block being explored
        branches = [block]         # list of branches to explore in this block
        exits    = []              # all exit locations encountered in this block

        if block not in blocks:
            blocks.append(block)
        else:
            continue

        while len(branches) > 0:

            cb = branches.pop(0)  # current block
            bc = 1                # branch count
            pc = cb               # next instruction to explore

            if pc in out:
                continue

            while bc > 0:

                if pc > stop:
                    bc = 0

                op = ord(rom[pc])

                com = ''
                ins = ''

                codes = []
                addr  = pc

                if op == 0xcb:

                    codes.append(0xcb)
                    codes.append(ord(rom[pc+1]))

                    ins = CB_INS[codes[1]]
                    pc += 2

                else:

                    codes.append(op)

                    if op in INS:
                        size = INS[op]['size']
                        ins  = INS[op]['mnem']
                    else:
                        size = 1
                        ins  = '*INVALID*'

                    l = ord(rom[pc+1])
                    h = ord(rom[pc+2])
                    w = (h << 8)|l

                    if size > 1:
                        if '_WORD' in ins:
                            ins = ins.replace('_WORD_', '0x%04x' % w)
                            codes.append(l)
                            codes.append(h)
                        elif '_BYTE_' in ins:
                            ins = ins.replace('_BYTE_', '0x%02x' % l)
                            codes.append(l)
                        elif 'DEC_' in ins:
                            ins = ins.replace('_DEC_', '%+d' % int8(l))
                            codes.append(l)

                    # interrupts
                    if cb in [0x0040, 0x0048, 0x0050, 0x0058, 0x0060]:
                        if op == 0xd9:
                            break

                    # calls
                    if op in [0xc4, 0xcc, 0xcd, 0xd4, 0xdc]:

                        if w not in explore and w < stop:
                            explore.append(w)

                        exits.append(addr)
                        sites.append(addr)

                        # start
                        if cb == 0x0100:
                            SYMBOLS[w] = 'main'

                        # interrupts
                        if cb in [0x0040, 0x0048, 0x0050, 0x0058, 0x0060]:
                            if w >= 0x0150:  # skip GBDK jump tables
                                SYMBOLS[w] = HANDLERS[cb]
                            else:
                                SYMBOLS[w] = 'interrupt_dispatcher'

                    # absolute jumps
                    if op in [0xc2, 0xc3, 0xca, 0xd2, 0xda, 0xe9]:

                        exits.append(addr)

                        # ignore jp hl, might be nice to deduce hl later on
                        if op is not 0xe9:
                            if w not in explore and w < stop:
                                explore.append(w)
                            sites.append(addr)

                        # unconditional jumps
                        if op is 0xe9 or op is 0xc3:
                            bc = 0

                        # start
                        if cb == 0x0100:
                            SYMBOLS[w] = 'main'

                        # interrupts
                        if cb in [0x0040, 0x0048, 0x0050, 0x0058, 0x0060]:
                            if w >= 0x0150:  # skip GBDK jump tables
                                SYMBOLS[w] = HANDLERS[cb]
                            else:
                                SYMBOLS[w] = 'interrupt_dispatcher'

                    # rst calls
                    if op in [0xc7, 0xcf, 0xd7, 0xdf, 0xe7, 0xef, 0xf7, 0xff]:
                        explore.append(op - 0xc7)
                        exits.append(addr)

                    # relative jumps
                    if op in [0x18, 0x20, 0x28, 0x30, 0x38]:
                        a = addr+INS[op]['size']+int8(l)
                        com  = '0x%04x' % a
                        com += ' ∨' if a > addr else ' ∧'

                        if (addr, a) not in jumps and max(addr, a) - min(addr, a) > 1:
                            jumps.append((addr, a))

                        if a not in out and a not in branches and a not in explore:
                            branches.append(a)

                    # instructions that deal with memory mapped registers directly
                    if op in [0xe0, 0xf0]:
                        a = 0xff00+l
                        if a in IO_REGS:
                            com = IO_REGS[a]

                    # instructions that deal with memory mapped registers directly
                    if op in [0x01, 0x08, 0x11, 0x21, 0xea, 0xfa]:
                        if w in IO_REGS:
                            com = IO_REGS[w]

                    # absolute returns and halt
                    if op in [0x76, 0xc9, 0xd9]:
                        bc = 0
                        exits.append(addr)

                    pc += size

                if ins is '*INVALID*':
                    exits.append(last)
                    bc = 0
                    continue

                last = addr
                if addr not in out:
                    out[addr] = {
                        'opcodes': codes,
                        'mnemonic': ins,
                        'comment': com,
                        'indent': 0,
                        'src': 0,
                        'dest': 0
                    }

        # explore the gaps looking for valid code
        if depth < max_depth:
            depth += 1
            gaps = []

            for pc in sorted(out):
                if pc > 0x150 and pc < stop:
                    op = ord(rom[pc])
                    if op == 0xcb:
                        nx = pc+2
                    else:
                        nx = pc+INS[op]['size']

                    if nx not in blocks:
                        gaps.append(nx)

            if len(gaps) > 3:
                for i in range(len(gaps)-1):
                    if gaps[i+1]-gaps[i] > 0x10:
                        if gaps[i] not in blocks and gaps[i] not in out:
                            explore.append(gaps[i])

        if len(exits) > 0:
            funcs[block] = sorted(exits).pop(-1)

    # handle dynamically named symbols
    for addr in sites:
        l = ord(rom[addr+1])
        h = ord(rom[addr+2])
        w = (h << 8)|l

        if w in SYMBOLS and out[addr]['comment'] == '':
            symbol = SYMBOLS[w]
            if '|' in symbol:
                symbol = symbol.split('|')[0]

            out[addr]['comment'] = '<%s>' % symbol

    # handle CFG rails
    levels = 0
    for i in jumps:
        src = i[0]
        dest = i[1]

        rail = -1
        for pc in range(min(src, dest), max(src, dest)+1):

            if pc not in out:
                continue

            if rail > levels:
                levels = rail

            if pc == dest:
                if rail == -1:

                    for xx in range(min(src, dest), max(src, dest)+1):
                        if xx not in out:
                            continue
                        r = firstbit(out[xx]['indent'], 1)
                        if r >= rail:
                            rail = r

            if pc == src:
                if rail == -1:

                    for xx in range(min(src, dest), max(src, dest)+1):
                        if xx not in out:
                            continue
                        r = firstbit(out[xx]['indent'], 1)
                        if r >= rail:
                            rail = r

            if pc in out:
                out[pc]['indent'] = setbit(out[pc]['indent'], rail, 1)

            if pc == dest:
                out[pc]['dest'] = setbit(out[pc]['dest'], rail, 1)

            if pc == src:
                out[pc]['src'] = setbit(out[pc]['src'], rail, 1)

    for pc in out:

        if out[pc]['src']:
            m = 0

            for x in range(32):
                if getbit(out[pc]['src'], x) > 0:
                    m = x
            for x in range(m):
                if getbit(out[pc]['indent'], x) > 0:
                    out[pc]['src'] = setbit(out[pc]['src'], x, 1)

        if out[pc]['dest']:
            m = 0

            for x in range(32):
                if getbit(out[pc]['dest'], x) > 0:
                    m = x

            for x in range(m):
                if getbit(out[pc]['indent'], x) > 0:
                    out[pc]['dest'] = setbit(out[pc]['dest'], x, 1)

    return {'code': out, 'levels': levels+1, 'funcs': funcs}


def gadgets(rom, depth=5, repeats=False):

    sites = []
    stop  = 0x4000 if len(rom) > 0x4000 else len(rom)
    rets  = [0xc0, 0xc8, 0xc9, 0xd0, 0xd8, 0xd9]
    bad   = [
        0xc7, 0xcf, 0xd7, 0xdf, 0xe7, 0xef, 0xf7, 0xff,
        0xc2, 0xc3, 0xca, 0xd2, 0xda, 0xe9, 0xc4, 0xcc,
        0xcd, 0xd4, 0xdc, 0x10, 0x76, 
    ];

    for addr in range(stop):
        op = ord(rom[addr])
        if op in rets:
            sites.append(addr)

    chains = {}
    for addr in sites:

        start = addr - (depth * 3)
        if start < 0:
            start = 0
        ins = [ord(e) for e in rom[start:addr+1]]

        for i in range(len(ins)):

            d  = 0
            pc = i
            ch = []
            while True:

                d += 1
                op = ins[pc]
                if op not in INS or op in bad or INS[op]['size']+pc > len(ins) or d > depth:
                    ch = []
                    break

                for c in range(INS[op]['size']):
                    ch.append(ins[pc+c])

                pc += INS[op]['size']

                if op in rets:
                    break

                if pc == len(ins):
                    ch = []
                    break

            if len(ch) > 0:
                chains[start+i] = ch

    got = []
    ret = {}
    for i in chains:
        chain = chains[i]
        if len(chain) > depth:
            continue

        rop = []
        pc  = 0
        while True:

            if pc >= len(chain):
                break

            ins  = INS[chain[pc]]['mnem']
            size = INS[chain[pc]]['size']

            if size > 1:

                l = chain[pc+1]

                if '_BYTE_' in ins:
                    ins = ins.replace('_BYTE_', '0x%02x' % l)
                elif 'DEC_' in ins:
                    ins = ins.replace('_DEC_', '%+d' % int8(l))

                if size > 2:

                    h = chain[pc+2]
                    w = (h << 8)|l

                    if '_WORD' in ins:
                        ins = ins.replace('_WORD_', '0x%04x' % w)

            rop.append(ins)
            pc += size

        clean = ' ; '.join(rop)
        while '  ' in clean:
            clean = clean.replace('  ', ' ')

        if not repeats:
            if clean not in got:
                got.append(clean)
                ret[i] = clean
        else:
            ret[i] = clean

    return ret


def human_readable(size):

    if size == 0:
        return 'None'

    for c in ['b', 'kb', 'mb']:
        if size > -1024.0 and size < 1024.0:
            return '%3.1f%s' % (size, c)
        size /= 1024


def show_parse(rom):

    info = parse(rom)
    print 'Cartridge Header:\n'
    print '  Title:             %s' % info['title']
    print '  Publisher:         %s' % info['licensee']
    if 'manufacturer' in info:
        print '  Manufacturer Code: %s' % info['manufacturer']
    print '  ROM Size:          %s' % human_readable(info['rom'])
    print '  RAM Size:          %s' % human_readable(info['ram'])
    print '  Version:           %d' % info['version']
    print '  Entry Point:       0x%04x' % info['entry']
    print '  Cartridge Type:    %s' % info['type']
    print '  Color:             %s' % ('Yes' if info['color'] else 'No')
    print '  Super Gameboy:     %s' % ('Yes' if info['sgb'] else 'No')
    print '  Japanese:          %s' % ('Yes' if info['japanese'] else 'No')

    print ''
    if info['checksums']['header']['stored'] == info['checksums']['header']['check']:
        print '  Header Checksum:   0x%02x   (OK)' % info['checksums']['header']['stored']
    else:
        print '  Header Checksum:   0x%02x   (FAIL; should be 0x%02x)' % (info['checksums']['header']['stored'], info['checksums']['header']['check'])
    if info['checksums']['global']['stored'] == info['checksums']['global']['check']:
        print '  Global Checksum:   0x%04x (OK)' % info['checksums']['global']['stored']
    else:
        print '  Global Checksum:   0x%04x (FAIL; should be 0x%02x)' % (info['checksums']['global']['stored'], info['checksums']['global']['check'])


def show_disas(rom, start=0x100):

    data = disas(rom, start)

    insize = (data['levels']*2)+5
    indent = ''
    for addr in sorted(data['code']):

        if addr in data['funcs']:
            name  = ''
            extra = ''
            if addr in SYMBOLS:
                if '|' in SYMBOLS[addr]:
                    tokens = SYMBOLS[addr].split('|')
                    name   = tokens[0]
                    extra  = tokens[1]
                else:
                    name   = SYMBOLS[addr]

            line = '0x%04x%s:' % (addr, '' if not name else ' <'+name+'>')
            if extra:
                line = line.ljust(48+insize+1, ' ')
                line += '; %s' % extra

            print ''
            print line

        curr = data['code'][addr]
        if data['levels']:

            indent = ' '
            trace  = False

            for c in range((data['levels'])+1):

                b = getbit(curr['indent'], data['levels'] - c)
                y = getbit(curr['dest'], data['levels'] - c)
                z = getbit(curr['src'], data['levels'] - c)

                if y or z:
                    trace = True

                if trace:
                    trace = True
                    if y or z:
                        indent += '+-'
                    else:
                        indent += '--'
                else:
                    indent += '| ' if b == 1 else '  '

            if curr['dest']:
                indent += '>'

            if curr['src']:
                indent += '-'

            indent = indent.ljust(insize, ' ')

        line  = indent
        line += '%04x:    %s' % (addr, ' '.join('%02x' % e for e in curr['opcodes']).ljust(8, ' '))
        line += '    %s' % curr['mnemonic']

        if curr['comment']:
            line  = line.ljust(insize+48, ' ')
            line += ' ; %s' % curr['comment']

        print line


def show_gadgets(rom):

    ins = gadgets(rom)
    for item in sorted(ins.items(), key=lambda x: x[1]):
        print '0x%04x : %s' % (item[0], item[1])


def usage(prog):
    print 'usage: %s [disas|info|rop] <gb rom>' % prog
    print ''
    print 'examples:\n'
    print '   disassemble: %s disas rom.gb' % prog
    print '                %s rom.gbc' % prog
    print ''
    print '   information: %s info rom.gb' % prog
    print '                %s rom.gbc' % prog
    print ''
    print '   rop gadgets: %s rop rom.gb' % prog


def main():

    import os.path

    file  = ''
    modes = ['info', 'disas']

    if len(sys.argv) < 2:
        usage(sys.argv[0])
        sys.exit(-1)

    if len(sys.argv) == 2:
        if sys.argv[1] in ['disas', 'info', 'rop']:
            usage(sys.argv[0])
            sys.exit(-1)

        file = sys.argv[1]

    if len(sys.argv) == 3:
        file  = sys.argv[2]
        modes = [sys.argv[1]]

    if not os.path.isfile(file):
        print 'error: file does not exist'
        sys.exit(-1)

    rom  = ''
    with open(file, 'rb') as f:
        rom = f.read()

    for mode in modes:

        if mode == 'info':
            show_parse(rom)
        elif mode == 'disas':
            show_disas(rom)
        elif mode == 'rop':
            show_gadgets(rom)

if __name__ == '__main__':
    main()