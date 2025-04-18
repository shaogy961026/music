from music21 import chord, stream, tempo, note

s = stream.Stream()
s.append(tempo.MetronomeMark(number=120))

chord_data = [
    ["C4", "E4", "G4"],  # C
    ["B3", "D4", "G4"],  # G/B
    ["A3", "C4", "E4"],  # Am
    ["G3", "B3", "E4"],  # Em/G
    ["F3", "A3", "C4"],  # F
    ["E3", "G3", "C4"],  # C/E
    ["D3", "F3", "A3"],  # Dm
    ["G3", "B3", "D4"],  # G
]

for notes_list in chord_data:
    c = chord.Chord(notes_list)
    c.quarterLength = 4
    s.append(c)

s.show('midi')
