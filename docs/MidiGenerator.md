# MidiGenerator

A tool to convert digital musical notation to MIDI file.

## TODO

- [x] Rate control
  - [x] Pitch
  - [x] Semitone
  - [x] Octave
  - [x] Pause
  - [x] Key Signature
- [ ] Time control
  - [x] BPM
  - [x] Time Signature
  - [x] Note
  - [x] Mordent
  - [ ] Tie

## Sample code

![](assets/Snipaste_2022-06-02_10-42-26.jpg)

``` python
generator = MidiGenerator()

generator.createTrack('Piano', 'C', 90, 4)

musicList = [
    '1', '2', '3', '4', '5', '6', '7'
]

for monophonic in musicList:
    generator.addNote('Piano', monophonic)

generator.save('test.mid')
```

## Use

### Init

``` python
generator = MidiGenerator()
```

### Create track

Create one track by name, key signature, bpm and beatNumber.

``` python
generator.createTrack('Piano', 'C', 90, 4)
```

### Change BPM

Change track's bpm, only affects incoming notes afterward.

``` python
generator.changeBPM('Piano', 120)
```

### Change key signature

Change track's key signature, only affects incoming notes afterward.

``` python
generator.changeKeySignature('Piano', 'bE')
```

### Change beat number

Change track's beat number, only affects incoming notes afterward.

``` python
generator.changeBeatNumber('Piano', 2)
```

### Add note

Add single note into one midi track.

``` python
generator.addNote('Piano', '+3..')
```

### Save

Save MIDI file into harddisk.

``` python
generator.save('test.mid')
```