# NotationParser

A tool to convert digital musical notation to pwm rate and duration. You can use this tool to make the buzzer play nice music.

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

Set key signature like `1=C`.

``` python
parser.setKeySignature('C')
```

### Set pre-raised scale

The frequency division capability of the PWM pins of some chips is limited. In order to make the played music still conform to the law, the octave can be raised or lowered uniformly.

``` python
parser.setPreRaised(0)
```

### Set BPM

``` python
parser.setBPM(120)
```

### Set time signature

Set time signature like `4/4`.

``` python
parser.setTimeSignature(4)
```

### Get pwm rate and duration

``` python
parser.parseNotation('+3..')
```