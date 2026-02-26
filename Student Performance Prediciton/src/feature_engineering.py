def create_features(df):
    
    # Example: Total academic score
    df["total_score"] = (
        df["math_score"] +
        df["reading_score"] +
        df["writing_score"]
    )

    # Attendance ratio feature
    if "attendance" in df.columns:
        df["attendance_ratio"] = df["attendance"] / 100

    return df