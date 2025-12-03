from dataproc.audio import preprocess_basic, save_audio
import os

def main():
    audio_path = "sample_data/pure_tone.wav"

    y_proc, sr = preprocess_basic(
        audio_path,
        sr=16000,
        top_db=20,
        pre_emphasis_coeff=0.97,
        noise_cutoff=7000,
    )

    print("입력 파일:", audio_path)
    print("샘플링 주파수:", sr)
    print("샘플 개수:", len(y_proc))
    print("길이(초):", len(y_proc) / sr)

    base, ext = os.path.splitext(os.path.basename(audio_path))
    out_path = os.path.join("sample_data", f"{base}_preprocessed.wav")

    save_audio(out_path, y_proc, sr)
    print("저장 완료:", out_path)

if __name__ == "__main__":
    main()
