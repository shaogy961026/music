import random
from music21 import stream, note, midi, key

# 小星星旋律（C大調）
melody_notes = ['C4', 'C4', 'G4', 'G4', 'A4', 'A4', 'G4',
                'F4', 'F4', 'E4', 'E4', 'D4', 'D4', 'C4']

# 隨機參數設定
transpose_steps = random.randint(0, 6)  # 0~6度
octave_shift = random.choice([-12, 0, 12])  # 隨機八度位移

# 計算主音與半音數
scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
target_tonic = scale[transpose_steps]
base_semitones = key.Key(target_tonic).tonic.midi - key.Key('C').tonic.midi
total_semitones = base_semitones + octave_shift  # 合併轉調與八度位移

# 建立旋律
melody = stream.Stream()
for n in melody_notes:
    melody.append(note.Note(n, quarterLength=0.5))

# 轉調與八度位移
transposed_melody = melody.transpose(total_semitones)

# 播放
print("播放隨機轉調+八度位移的小星星，猜猜看調性！")
sp = midi.realtime.StreamPlayer(transposed_melody)
sp.play()

# 顯示答案
if octave_shift == -12:
    octave_str = " + 低八度"
elif octave_shift == 12:
    octave_str = " + 高八度"
else:
    octave_str = ""

print(f"答案：升{transpose_steps}度{octave_str}")
print(f"總共位移 {total_semitones} 個半音 → {target_tonic}大調")
