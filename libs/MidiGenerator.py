import math
import re
import mido


class MidiGenerator:
    def __init__(self):
        self.ticksPerBeat = 480

        self.keySignatureDict = {
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

        self.scaleDict = {
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

        self.mid = mido.MidiFile()

        self.mid.ticks_per_beat = self.ticksPerBeat

        self.tracks = {}

    def createTrack(self, name, keySignature, bpm, beatNumber):
        track = mido.MidiTrack()
        self.mid.tracks.append(track)

        tempo = int(60 * 1000000 / bpm)

        track.append(mido.MetaMessage(
            'track_name', name=name, time=0))
        track.append(mido.MetaMessage(
            'set_tempo', tempo=tempo, time=0))

        self.tracks[name] = {
            'track': track,
            'keySignature': keySignature,
            'beatNumber': beatNumber,
            'lastNote': None,
            'lastTimeValue': 0,
        }

    def changeBPM(self, name, bpm):
        tempo = int(60 * 1000000 / bpm)

        self.tracks[name]['track'].append(mido.MetaMessage(
            'set_tempo', tempo=tempo, time=0))

    def changeKeySignature(self, name, keySignature):
        self.tracks[name]['keySignature'] = keySignature

    def changeBeatNumber(self, name, beatNumber):
        self.tracks[name]['beatNumber'] = beatNumber

    def _addNote(self, track, note, timeValue):
        track.append(
            mido.Message('note_on', note=int(note), velocity=127, time=0))
        track.append(mido.Message('note_off', note=int(note),
                                  velocity=127, time=int(timeValue)))

    def _pause(self, track, note, timeValue):
        track.append(
            mido.Message('note_on', note=int(note), velocity=0, time=0))
        track.append(mido.Message('note_off', note=int(note),
                                  velocity=0, time=int(timeValue)))

    def addNote(self, trackName, monophonic):
        scaleKey = ''

        if(monophonic.find('b') != -1):
            scaleKey += 'b'

        digitals = re.search(r'\d+', monophonic)
        scaleKey += digitals.group(0)

        riseNumber = monophonic.count('+')
        dropNumber = monophonic.count('-')

        note = self.keySignatureDict[self.tracks[trackName]
                                     ['keySignature']] + self.scaleDict[scaleKey]

        note = note + 12 * riseNumber
        note = note - 12 * dropNumber

        extendNumber = monophonic.count('.')
        reduceNumber = monophonic.count('_')
        dottedNumber = monophonic.count('*')

        quarterNoteTime = self.ticksPerBeat * \
            self.tracks[trackName]['beatNumber'] / 4

        if(extendNumber == 0):
            timeValue = quarterNoteTime * (1 / math.pow(2, reduceNumber))

            for _ in range(dottedNumber):
                timeValue *= 1.5
        else:
            timeValue = quarterNoteTime * (extendNumber + 1)

        hasUpWave = False
        if(monophonic.find('~') != -1):
            hasUpWave = True

        isTieStart = False
        if(monophonic.find('(') != -1):
            isTieStart = True

        isTieEnd = False
        if(monophonic.find(')') != -1):
            isTieEnd = True

        if(scaleKey == '0'):
            self._pause(self.tracks[trackName]['track'], note, timeValue)
        elif(hasUpWave):
            self._addNote(self.tracks[trackName]
                          ['track'], note, timeValue * 3.0 / 8)
            self._addNote(self.tracks[trackName]['track'],
                          self.tracks[trackName]['lastNote'], timeValue * 1.0 / 4)
            self._addNote(self.tracks[trackName]
                          ['track'], note, timeValue * 3.0 / 8)
        elif(isTieStart):
            pass
        elif(isTieEnd):
            self._addNote(self.tracks[trackName]['track'], note,
                          timeValue + self.tracks[trackName]['lastTimeValue'])
        else:
            self._addNote(self.tracks[trackName]['track'], note, timeValue)

        self.tracks[trackName]['lastNote'] = note
        self.tracks[trackName]['lastTimeValue'] = timeValue

    def save(self, path):
        self.mid.save(path)
