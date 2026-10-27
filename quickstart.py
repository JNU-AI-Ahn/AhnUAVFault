import pandas as pd
import matplotlib.pyplot as plt

# 1. Load IMU telemetry CSV from AhnUAVFault
file_path = "20230822_14_34_46_IMU.CSV"
df = pd.read_csv(file_path)

# Check telemetry channels and display top 5 rows
print("Telemetry Channels:", df.columns.tolist())
print(df.head())

# 2. Plot vertical acceleration (AccZ)
if "AccZ" in df.columns:
    plt.figure(figsize=(10, 4))
    plt.plot(df["AccZ"], label="AccZ", color="tab:blue")
    plt.title("AhnUAVFault - IMU Vertical Acceleration")
    plt.xlabel("Sample Index")
    plt.ylabel("Acceleration")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
