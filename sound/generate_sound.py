import wave
import struct
import math
import os

def generate_alert_sound(filename="alert.wav", duration=1, frequency=440, volume=0.5):
    """
    生成一个蜂鸣音并保存为 .wav 文件
    :param filename: 输出文件名
    :param duration: 持续时间（秒）
    :param frequency: 频率（Hz）
    :param volume: 音量（0.0 ~ 1.0）
    """
    sample_rate = 44100  # CD 音质采样率
    bit_depth = 32767    # 16-bit PCM 最大值

    wav_file = wave.open(filename, 'w')
    wav_file.setparams((1, 2, sample_rate, 0, 'NONE', 'not compressed'))

    for i in range(int(sample_rate * duration)):
        sample = math.sin(2 * math.pi * i * frequency / sample_rate)
        wav_file.writeframes(struct.pack('h', int(sample * bit_depth * volume)))

    wav_file.close()
    print(f"✅ 提示音已生成：{os.path.abspath(filename)}")

if __name__ == "__main__":
    generate_alert_sound()