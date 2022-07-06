# NotationParser

A tool to convert digital musical notation to pwm rate and duration. You can use this tool to make the buzzer play nice music. [See docs.](docs/NotationParser.md)

You can also use this tool to convert scores to MIDI file. [See docs.](docs/MidiGenerator.md)

## Notation

For detailed symbols, refer to the following.

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

* `b`: Flat

### Octave

* `+`: Raise one octave
* `-`: Drop one octave

### Pause

* `0`

### Note

* `_`: Eighth note, sixteenth note, thirty-second note. (depending on the number of `_`)
* `.`: Half note, whole note. (depending on the number of `_`)
* `*`: Dotted.

### Mordent

* `~`：Upper mordent

### Tie

* `(`: Tie note start (Support continuous tie.)
* `)`: Tie note end

## Special thanks to `延夏新东方演奏群`

* Clavy
* 大酱dz
* 番茄沙司
* 年轻的八云紫
* 小黑鱼
* 原Via
* 宴月