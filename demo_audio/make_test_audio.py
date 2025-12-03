import numpy as np
import soundfile as sf
import os

os.makedirs("sample_data", exist_ok=True)

sr = 16000

t1 = np.linspace(0, 3.0, int(sr * 3.0), endpoint=False)
pure_tone = 0.6 * np.sin(2 * np.pi * 440 * t1)
sf.write("sample_data/pure_tone.wav", pure_tone, sr)
print("Created sample_data/pure_tone.wav (3s pure tone)")

t2 = np.linspace(0, 2.0, int(sr * 2.0), endpoint=False)
tone = 0.6 * np.sin(2 * np.pi * 440 * t2)
silence = np.zeros(int(sr * 1.0))
tone_with_silence = np.concatenate([silence, tone, silence])
sf.write("sample_data/tone_with_silence.wav", tone_with_silence, sr)
print("Created sample_data/tone_with_silence.wav (1s silence + 2s tone + 1s silence)")


noise = 0.2 * np.random.randn(len(pure_tone))
noisy_tone = pure_tone + noise
sf.write("sample_data/noisy_tone.wav", noisy_tone, sr)
print("Created sample_data/noisy_tone.wav (pure tone + noise)")
