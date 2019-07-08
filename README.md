# gbparse

A small utility to disassemble gameboy roms, read matadata and find rop gadgets.

## Usage

```bash
usage: ./gbparse.py [disas|info|rop] <gb rom>

examples:

   disassemble: ./gbparse.py disas rom.gb
                ./gbparse.py rom.gbc

   information: ./gbparse.py info rom.gb
                ./gbparse.py rom.gbc

   rop gadgets: ./gbparse.py rop rom.gb
```

### Disassemble
Disassemble a ROM. There is a CFG on the side for readability as well as some automatic identification and comments for interesting memory.
```bash
$ ./gbparse.py disas rom.gbc
...
0x4874 <serial_handler>:                                    ; called on int58
           4874:    fa ac c7    ld    a, [0xc7ac]
           4877:    fe 02       cp    0x02
       +-- 4879:    20 09       jr    nz, +9                ; 0x4884∨
       |   487b:    f0 01       ld    a, [0xff00+0x01]      ; serial data (SB)
       |   487d:    ea ab c7    ld    [0xc7ab], a
       |   4880:    3e 00       ld    a, 0x00
     +-+-- 4882:    18 0e       jr    +14                   ; 0x4892∨
     | +-> 4884:    fe 01       cp    0x01
     | +-- 4886:    20 16       jr    nz, +22               ; 0x489e∨
     | |   4888:    f0 01       ld    a, [0xff00+0x01]      ; serial data (SB)
     | |   488a:    fe 55       cp    0x55
   +-+-+-- 488c:    28 04       jr    z, +4                 ; 0x4892∨
   | | |   488e:    3e 04       ld    a, 0x04
 +-+-+-+-- 4890:    18 02       jr    +2                    ; 0x4894∨
 | +-+-+-> 4892:    3e 00       ld    a, 0x00
 +-----+-> 4894:    ea ac c7    ld    [0xc7ac], a
       |   4897:    af          xor   a
       |   4898:    e0 02       ld    [0xff00+0x02], a      ; serial control (SC)
       |   489a:    3e 66       ld    a, 0x66
       |   489c:    e0 01       ld    [0xff00+0x01], a      ; serial data (SB)
       +-> 489e:    3e 80       ld    a, 0x80
           48a0:    e0 02       ld    [0xff00+0x02], a      ; serial control (SC)
           48a2:    c9          ret
```

### Metadata
Read metadata in the cartridge header.
```bash
$ ./gbparse.py info ai.gb
Cartridge Header:

  Title:             ADVENTUREISLAND2
  Publisher:         Hudson Soft
  ROM Size:          256.0kb
  RAM Size:          None
  Version:           0
  Entry Point:       0x0150
  Cartridge Type:    MBC1
  Color:             No
  Super Gameboy:     Yes
  Japanese:          No

  Header Checksum:   0x2f   (OK)
  Global Checksum:   0x66a8 (OK)
```

### ROP Gadgets
The tool can also be used to find ROP gadgets in the ROM memory.
```bash
$ ./gbparse.py rop rom.gbc|grep -F ': pop'
0x0fb1 : pop af ; pop bc ; pop de ; pop hl ; ret
0x2158 : pop af ; ret
0x04cd : pop af ; ret nz
0x02ba : pop af ; reti
0x34f6 : pop bc ; add a, 0xb7 ; ret nz
0x3790 : pop bc ; cp 0x80 ; ret z
0x11ba : pop bc ; ld c, 0x01 ; ret
```

### Python
Everything above can be used comfortably from python, check the script for details. Below are basic signatures.
```python
import gbparse

data = ''
file = '/path/to/rom.gbc'
with open(file, 'rb') as f:
    data = f.read()

inst = gbparse.disas(data, start=0x0000, stop=0x7fff, max_depth=60)  # return disassembly of the ROM
info = gbparse.parse(data)                                           # return the data in the cartridge header
ropg = gbparse.gadgets(data, depth=5, repeats=False)                 # return a list of gadgets in the ROM
```

## TODO

1. Automatic function identification for common game company libraries as well as GBDK.