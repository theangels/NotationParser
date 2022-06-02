from libs.NotationParser import NotationParser

parser = NotationParser()

parser.setKeySignature('C')
parser.setPreRaised(0)
parser.setBPM(120)
parser.setTimeSignature(4)

print(parser.parseNotation('+3..'))