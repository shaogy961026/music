import random
from music21 import stream, note, midi, key

# 小星星旋律（C大調）
melody_notes = ['C4', 'C4', 'G4', 'G4', 'A4', 'A4', 'G4',
                'F4', 'F4', 'E4', 'E4', 'D4', 'D4', 'C4']

# 升0~6度（對應C~B大調）
transpose_steps = random.randint(0, 6)
scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
target_tonic = scale[transpose_steps]

# 計算需要升幾個半音
original_key = key.Key('C')
target_key = key.Key(target_tonic)
transpose_semitones = target_key.tonic.midi - original_key.tonic.midi

# 建立旋律
melody = stream.Stream()
for n in melody_notes:
    melody.append(note.Note(n, quarterLength=0.5))

# 轉調
transposed_melody = melody.transpose(transpose_semitones)

# 播放
print("播放隨機轉調後的小星星，猜猜看調性！")
sp = midi.realtime.StreamPlayer(transposed_melody)
sp.play()

print(f"答案：本次全部升 {transpose_steps} 度（{transpose_semitones} 個半音）")
print(f"原本是 C 大調，現在是 {target_tonic} 大調")
