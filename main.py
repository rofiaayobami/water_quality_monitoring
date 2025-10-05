from load_data import load_csv
from clean_data import clean_data
from evaluate import WaterQualityEvaluator

def main():
    # 1. Load
    df = load_csv("c:/Users/USER/WATER_QUALITY_MONITORING/data/sample_data.csv")
    if df is None or df.empty:
        print("No data loaded.")
        return

    # 2. Clean
    df = clean_data(df)

    # 3. Evaluate
    evaluator = WaterQualityEvaluator() 
    df = evaluator.evaluate(df)         

    # 4. Print summary
    print(df.head())

    # bonus: Count safe vs unsafe
    safe_count = df['Safe'].sum()
    unsafe_count = len(df) - safe_count
    print(f"\nSafe lakes: {safe_count}, Unsafe lakes: {unsafe_count}")

    # bonus: Save output
    df.to_csv("sample_results.csv", index=False)
    print("\nResults saved to results.csv")

if __name__ == "__main__":
    main()

