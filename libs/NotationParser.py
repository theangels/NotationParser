import math
import re


class NotationParser:
    def __init__(self):
        self.setKeySignature('C')

        self.bpm = 120
        self.beatNumber = 4
        self.preRaised = 0

        self.lastFundamentalToneRate = 0

    def setBPM(self, bpm):
        self.bpm = bpm

    def setTimeSignature(self, beatNumber):
        self.beatNumber = beatNumber

    def setPreRaised(self, p):
        self.preRaised = p

    def setKeySignature(self, major):
        keySignatureDict = {
            'C': 262,
            '#C': 277,
            'bD': 277,
            'D': 294,
            '#D': 311,
            'bE': 311,
            'E': 330,
            'F': 349,
            '#F': 370,
            'bG': 370,
            'G': 392,
            '#G': 415,
            'bA': 415,
            'A': 440,
            '#A': 466,
            'bB': 466,
            'B': 494
        }

        frequency = []

        for i in range(12):
            f = keySignatureDict[major] * math.pow(2, i/12)
            frequency.append(f)

        self.scaleDict = {
            '0': 0,
            '1': int(frequency[0]),
            'b2': int(frequency[1]),
            '2': int(frequency[2]),
            'b3': int(frequency[3]),
            '3': int(frequency[4]),
            '4': int(frequency[5]),
            'b5': int(frequency[6]),
            '5': int(frequency[7]),
            'b6': int(frequency[8]),
            '6': int(frequency[9]),
            'b7': int(frequency[10]),
            '7': int(frequency[11])
        }

    def parseNotation(self, monophonic):
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
        # upWaveNumber = monophonic.count('~')

        realRate = self.scaleDict[scaleKey] * \
            math.pow(2, riseNumber) * (1 / math.pow(2, dropNumber))

        quarterNote = (60 / self.bpm) * self.beatNumber * (1.0 / 4)

        if(extendNumber == 0):
            timeValue = quarterNote * (1 / math.pow(2, reduceNumber))

            for _ in range(dottedNumber):
                timeValue *= 1.5
        else:
            timeValue = quarterNote * (extendNumber + 1)

        return {
            'rate': int(realRate),
            'during': int(timeValue * 1000)
        }

        # if(upWaveNumber == 0):
        #     self.play(realRate, timeValue)
        # else:
        #     self.play(realRate, timeValue * 3.0 / 8)
        #     self.play(self.lastFundamentalToneRate, timeValue * 1.0 / 4)
        #     self.play(realRate, timeValue * 3.0 / 8)

        # self.lastFundamentalToneRate = realRate
