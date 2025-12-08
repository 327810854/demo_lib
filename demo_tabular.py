from pathlib import Path
import sys

# allow local import of dataproc
sys.path.append(str(Path(__file__).resolve().parent.parent / "dataproc"))

from dataproc.tabular.proc import (
    load_csv,
    drop_empty,
    drop_duplicates,
    keep_columns,
    save_csv,
)

def main():
    csv_path = Path("data/sample.csv")
    df = load_csv(csv_path)

    df = drop_empty(df)
    df = drop_duplicates(df)
    df = keep_columns(df, ["name", "score"])

    out_dir = Path("out")
    out_dir.mkdir(exist_ok=True)
    save_csv(df, out_dir / "cleaned.csv")

    print("Demo finished. Output saved to out/cleaned.csv")

if __name__ == "__main__":
    main()