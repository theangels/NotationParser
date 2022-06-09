import mido
import re
import math

beatNumber = 4
bpm = 120
keySignature = 'C'

keySignatureDict = {
    'C': 60,
    '#C': 61,
    'bD': 61,
    'D': 62,
    '#D': 63,
    'bE': 63,
    'E': 64,
    'F': 65,
    '#F': 66,
    'bG': 66,
    'G': 67,
    '#G': 68,
    'bA': 68,
    'A': 69,
    '#A': 70,
    'bB': 70,
    'B': 71
}

scaleDict = {
    '0': 0,
    '1': 1,
    'b2': 2,
    '2': 3,
    'b3': 4,
    '3': 5,
    '4': 6,
    'b5': 7,
    '5': 8,
    'b6': 9,
    '6': 10,
    'b7': 11,
    '7': 12
}

ticksPerBeat = 480
tempo = int(60 * 1000000 / bpm)

mid = mido.MidiFile()

mid.ticks_per_beat = ticksPerBeat

track = mido.MidiTrack()
mid.tracks.append(track)

track.append(mido.MetaMessage('track_name', name='Piano', time=0))
track.append(mido.MetaMessage('set_tempo', tempo=tempo, time=0))


def playSingleNote(track, monophonic):
    scaleKey = ''

    if(monophonic.find('b') != -1):
        scaleKey += 'b'

    digitals = re.search(r'\d+', monophonic)
    scaleKey += digitals.group(0)

    riseNumber = monophonic.count('+')
    dropNumber = monophonic.count('-')
    extendNumber = monophonic.count('.')
    reduceNumber = monophonic.count('_')
    dottedNumber = monophonic.count('*')

    quarterNoteTime = ticksPerBeat * beatNumber / 4

    note = keySignatureDict[keySignature] + scaleDict[scaleKey]

    if(monophonic.find('b') != -1):
        note = note - 1

    note = note + 12 * riseNumber
    note = note - 12 * dropNumber

    if(extendNumber == 0):
        timeValue = quarterNoteTime * (1 / math.pow(2, reduceNumber))

        for _ in range(dottedNumber):
            timeValue *= 1.5
    else:
        timeValue = quarterNoteTime * (extendNumber + 1)

    timeValue = int(timeValue)

    track.append(mido.Message('note_on', note=note, velocity=127, time=0))
    track.append(mido.Message('note_off', note=note,
                              velocity=127, time=timeValue))


musicList = [
    '0', '0', '0', '0',
    '6...',
    '3__', '3__', '6__', '6__', '7__', '7__', '+1__', '+1__', '+2__', '+2__', '+1__', '+1__', '7__', '7__', '+1__', '+1__',
    '6...',

    '3__', '3__', '6__', '6__', '7__', '7__', '+1__', '+1__', '+2__', '+2__', '+1__', '+1__', '+2__', '+2__', '+3__', '+3__',
    '+6__', '+4__', '+1__', '6__', '+4__', '+4__', '+1__', '6__', '+7__', '+5__', '+2__', '7__', '5__', '5__', '2__', '-7__', '0',
    '6_*', '6__', '6.', '6__', '3__', '6__', '7__',
    '+1_*', '+1__', '+1.', '+1_', '+2_',

    '5.', '4', '3',
    '2.', '+5__', '+5__', '+2__', '7__', '5__', '5__', '2__', '-7__',
    '6_*', '6__', '6.', '6__', '3__', '6__', '7__',
    '+1_*', '+1__', '+1.', '+1_', '+2_',

    '5.', '0_', '3_', '4_', '5_',
    '6__', '4__', '1__', '-6__', '4__', '4__', '1__', '-6__', '7__', '5__', '2__', '-7__', '5__', '5__', '7__', '7__',
    '+1_*', '+1__', '+1.', '+1__', '6__', '+1__', '+3__',
    '+4_*', '+4__', '+4.', '+4_', '+1_',

    '+3.', '0_', '5_', '7_', '+1_',
    '+2.', '+1', '7',
    '+1_*', '+1__', '+1.', '+1__', '6__', '+1__', '+3__',
    '+4_*', '+4__', '+4.', '+5_', '+4_',

    '+3', '+1', '0_', '5__', '5__', '+1_', '+3_',
    '+2*', '+2__', '+2__', '+3_', '+3*',
    '-6', '1_', '3_', '4', '1',
    '3', '1', '-7', '-5',

    '-6', '1_', '3_', '6', '5_', '4_',
    '3', '1', '2', '-7',
    '0_', '-6_', '1_', '3_', '4', '1',
    '3', '1', '0_', '-7_', '-6_', '-5_',

    '-6__', '-7__', '1_', '1_', '6__', '7__', '+1.',
    '7__', '+1__', '+2_', '+2_', '+1', '7',
    '0_', '-6__', '1__', '3_', '6_', '7', '+1',
    '5', '3', '4', '3_', '2_',

    '0_', '-6__', '1__', '3_', '6_', '7', '+1',
    '+3', '+1', '+2', '+1_', '7_',
    '0_', '3_', '6_', '7_', '+1', '+3',
    '+5', '+4_', '+3_', '+2', '+1_', '7_',

    '6', '0_', '6__', '7__', '+1.',
    '7__', '+1__', '+2_', '+2', '+3_', '+3*',
    '-1', '-3', '0_', '-3_', '-6_', '-7_',
    '-3.', '-3', '2',

    '-7', '+4.', '-6',
    '-3', '+3', '0_', '+3__', '+3__', '+3_', '+3_',
    '-6', '-3', '0_', '-3_', '-6_', '-7_',
    '1.', '2', '-b6',

    '-b6.', '-6', '-7',
    '1_', '2_', '-7.', '6',
    '6', '3', '0_', '3_', '2_', '3_',
    '4...',

    '2.', '6.',
    '6.', '7.', '0',
    '0', '0', '0', '0',
    '6__', '6_*', '6'
]

for monophonic in musicList:
    playSingleNote(track, monophonic)

mid.save('test.mid')
