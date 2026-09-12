import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load processed data
df = pd.read_csv("cleaned_iso_compliance_data.csv")

# Visual Style Configuration
plt.style.use("seaborn-v0_8-whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 1. General Compliance Graph
compliance_counts = df["is_fully_compliant"].value_counts()
axes[0].pie(
    compliance_counts,
    labels=["Compliant", "Non-Compliant"],
    autopct="%1.1f%%",
    colors=["#2ecc71", "#e74c3c"],
    startangle=90,
)
axes[0].set_title("ISO Compliance Status")

# 2. Non-Compliant Causes
non_compliant = df[df["non_conformance_reason"] != "Compliant"]
sns.countplot(
    data=non_compliant,
    y="non_conformance_reason",
    ax=axes[1],
    palette="Reds_r",
)
axes[1].set_title("Rejection Causes")
axes[1].set_xlabel("Number of Batches")

plt.tight_layout()
plt.savefig("dashboard_preview.png", dpi=300)
print("✅ Dashboard saved as 'dashboard_preview.png'")
