# NotationParser

A tool to convert digital musical notation to pwm.(Like control buzzer)

## TODO

- [x] Rate control
  - [x] Pitch
  - [x] Semitone
  - [x] Octave
  - [x] Pause
  - [x] Key Signature
  - [x] Pre-raised
- [ ] Time control
  - [x] BPM
  - [x] Time Signature
  - [x] Note
  - [ ] Mordent
  - [ ] Tie

## Sample code

![](assets/Snipaste_2022-06-02_10-42-26.jpg)

``` python
parser = NotationParser()

parser.setKeySignature('C')
parser.setPreRaised(0)
parser.setBPM(120)
parser.setTimeSignature(4)

print(parser.parseNotation('+3..'))
```

## Use

### Init

``` python
parser = NotationParser()
```

### Set key signature

``` python
parser.setKeySignature('C')
```

### Set pre-raised scale

``` python
parser.setPreRaised(0)
```

### Set BPM

``` python
parser.setBPM(120)
```

### Set time signature

``` python
parser.setTimeSignature(4)
```

### Get pwm rate and duration

``` python
parser.parseNotation('+3..')
```

## Notation

### Key Signature

* `C`
* `#C`
* `bD`
* `D`
* `#D`
* `bE`
* `E`
* `F`
* `#F`
* `bG`
* `G`
* `#G`
* `bA`
* `A`
* `#A`
* `bB`
* `B`

### Pitch

* `1`
* `2`
* `3`
* `4`
* `5`
* `6`
* `7`

### Semitone

* `b`

### Octave

* `+`
* `-`

### Pause

* `0`

### Note

* `_`
* `.`
* `*`