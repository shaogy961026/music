import random
from music21 import stream, note, midi, key

# 小星星旋律（C大調）
melody_notes = ['C4', 'C4', 'G4', 'G4', 'A4', 'A4', 'G4',
                'F4', 'F4', 'E4', 'E4', 'D4', 'D4', 'C4']

# 隨機決定一個升幾個「音」（0~7），每個音等於2個半音
transpose_steps = random.randint(0, 7)
transpose_semitones = transpose_steps * 2

# 建立旋律
melody = stream.Stream()
for n in melody_notes:
    melody.append(note.Note(n, quarterLength=0.5))

# 轉調
transposed_melody = melody.transpose(transpose_semitones)

# 播放
print("播放隨機轉調後的小星星")
sp = midi.realtime.StreamPlayer(transposed_melody)
sp.play()

# # 等待使用者按下 Enter 再公布答案
# input("按 Enter 顯示答案...")

# 計算新調性
original_key = key.Key('C')
transposed_key = original_key.transpose(transpose_semitones)

print(f"本次全部升 {transpose_steps} 個音（{transpose_semitones} 個半音）")
print(f"原本是 C 大調，現在是 {transposed_key.tonic.name} 大調")
