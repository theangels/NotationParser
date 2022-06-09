from libs.MidiGenerator import MidiGenerator

generator = MidiGenerator()

generator.createTrack('Piano', 'C', 90, 4)

musicList = [
    '1', '2', '3', '4', '5', '6', '7'
]

for monophonic in musicList:
    generator.addNote('Piano', monophonic)

generator.save('test.mid')