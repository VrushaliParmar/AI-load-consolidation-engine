import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore")


def load_shipments(filepath: str) -> pd.DataFrame:
    """Load shipments CSV into a DataFrame."""
    df = pd.read_csv(filepath)
    print(f"✅ Loaded {len(df)} shipments from {filepath}")
    return df


def find_optimal_k(data: np.ndarray, k_min: int = 2, k_max: int = 10) -> int:
    """
    Auto-detect the best number of clusters (K)
    using the Elbow Method (inertia).
    """
    inertias = []
    k_range = range(k_min, k_max + 1)

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(data)
        inertias.append(kmeans.inertia_)

    # Find elbow point — biggest drop in inertia
    deltas = [inertias[i] - inertias[i + 1] for i in range(len(inertias) - 1)]
    optimal_k = k_range[deltas.index(max(deltas)) + 1]

    print(f"📊 Optimal number of clusters (K): {optimal_k}")
    return optimal_k


def cluster_shipments(filepath: str) -> pd.DataFrame:
    """
    Main function: Load shipments, auto-detect K,
    run K-Means, and return DataFrame with cluster labels.
    """
    # Step 1 — Load data
    df = load_shipments(filepath)

    # Step 2 — Use lat/lon + weight + volume as clustering features
    features = df[["latitude", "longitude", "weight_kg", "volume_m3"]].copy()

    # Step 3 — Normalize features so no column dominates
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Step 4 — Auto-detect best K
    optimal_k = find_optimal_k(scaled_features)

    # Step 5 — Run K-Means with optimal K
    kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(scaled_features)

    # Step 6 — Summary
    print("\n📦 Shipments per Cluster:")
    print(df.groupby("cluster")[["shipment_id", "weight_kg", "volume_m3"]].agg(
        shipment_count=("shipment_id", "count"),
        total_weight_kg=("weight_kg", "sum"),
        total_volume_m3=("volume_m3", "sum")
    ).to_string())

    print("\n✅ Clustering complete! 'cluster' column added to DataFrame.")
    return df


def get_cluster_summary(df: pd.DataFrame) -> dict:
    """
    Returns a structured summary of each cluster
    — useful for passing to the FastAPI response.
    """
    summary = {}
    for cluster_id, group in df.groupby("cluster"):
        summary[int(cluster_id)] = {
            "shipment_ids": group["shipment_id"].tolist(),
            "destinations": group["destination"].tolist(),
            "total_weight_kg": round(group["weight_kg"].sum(), 2),
            "total_volume_m3": round(group["volume_m3"].sum(), 2),
            "shipment_count": len(group),
            "priority_breakdown": group["priority"].value_counts().to_dict()
        }
    return summary


# ── Quick test ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    filepath = "backend/data/sample_shipments.csv"
    df_clustered = cluster_shipments(filepath)
    summary = get_cluster_summary(df_clustered)

    print("\n🗂️  Cluster Summary (JSON-ready):")
    for cluster_id, info in summary.items():
        print(f"\n  Cluster {cluster_id}:")
        print(f"    Shipments  : {info['shipment_count']}")
        print(f"    Total Weight: {info['total_weight_kg']} kg")
        print(f"    Total Volume: {info['total_volume_m3']} m³")
        print(f"    Priority    : {info['priority_breakdown']}")