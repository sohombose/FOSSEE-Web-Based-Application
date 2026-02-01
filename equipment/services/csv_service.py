import pandas as pd

REQUIRED_COLUMNS = {
    "Equipment Name",
    "Type",
    "Flowrate",
    "Pressure",
    "Temperature"
}


def process_csv(file):
    """
    Reads a CSV file, validates structure,
    cleans data, and returns summary analytics.
    """

    # ---------- READ CSV ----------
    try:
        df = pd.read_csv(file)
    except Exception as e:
        raise ValueError("Unable to read CSV file") from e

    # ---------- BASIC VALIDATIONS ----------
    if df.empty:
        raise ValueError("CSV file is empty")

    if not REQUIRED_COLUMNS.issubset(df.columns):
        missing = REQUIRED_COLUMNS - set(df.columns)
        raise ValueError(f"Missing columns: {', '.join(missing)}")

    # ---------- DATA CLEANING ----------
    # Convert numeric columns safely
    for col in ["Flowrate", "Pressure", "Temperature"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows with invalid numeric values
    df = df.dropna(subset=["Flowrate", "Pressure", "Temperature"])

    if df.empty:
        raise ValueError("No valid numeric data found after cleaning")

    # ---------- ANALYTICS ----------
    summary = {
        "total_equipment": int(len(df)),
        "averages": {
            "flowrate": round(df["Flowrate"].mean(), 2),
            "pressure": round(df["Pressure"].mean(), 2),
            "temperature": round(df["Temperature"].mean(), 2),
        },
        "type_distribution": (
            df["Type"]
            .astype(str)
            .str.strip()
            .value_counts()
            .to_dict()
        )
    }

    return summary
