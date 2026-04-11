# generate_data.py
# Purpose: Generate 500 realistic shipment records for testing
# Author: Vrushali
# Project: AI Load Consolidation Engine

import random
import csv
import os

# ─────────────────────────────────────────
# THEORY:
# We define real Indian cities with their
# actual GPS coordinates (latitude, longitude)
# K-Means will later use these coordinates
# to group nearby shipments into clusters
# ─────────────────────────────────────────

CITIES = [
    {"name": "Mumbai",     "lat": 19.0760, "lon": 72.8777},
    {"name": "Nashik",     "lat": 20.0059, "lon": 73.7898},
    {"name": "Nagpur",     "lat": 21.1458, "lon": 79.0882},
    {"name": "Aurangabad", "lat": 19.8762, "lon": 75.3433},
    {"name": "Solapur",    "lat": 17.6599, "lon": 75.9064},
    {"name": "Kolhapur",   "lat": 16.7050, "lon": 74.2433},
    {"name": "Amravati",   "lat": 20.9374, "lon": 77.7796},
    {"name": "Nanded",     "lat": 19.1383, "lon": 77.3210},
]

PRIORITIES = ["high", "medium", "low"]

# ─────────────────────────────────────────
# THEORY:
# Each shipment has:
# - weight_kg : how heavy the package is
# - volume_m3 : how much truck space it needs
# These two values together decide how many
# shipments can fit in one truck
# ─────────────────────────────────────────

def generate_shipment(index):
    city = random.choice(CITIES)
    
    # Add small random noise to GPS so not all
    # shipments to same city have identical coordinates
    lat_noise = random.uniform(-0.05, 0.05)
    lon_noise = random.uniform(-0.05, 0.05)
    
    weight = round(random.uniform(20, 500), 1)
    volume = round(weight * random.uniform(0.01, 0.025), 2)
    priority = random.choice(PRIORITIES)

    return {
        "shipment_id": f"S{str(index).zfill(3)}",
        "origin": "Pune",
        "destination": city["name"],
        "latitude": round(city["lat"] + lat_noise, 4),
        "longitude": round(city["lon"] + lon_noise, 4),
        "weight_kg": weight,
        "volume_m3": volume,
        "priority": priority
    }


def generate_dataset(num_records=500):
    shipments = [generate_shipment(i+1) for i in range(num_records)]
    
    # Save to same folder as this script
    output_path = os.path.join(os.path.dirname(__file__), "sample_shipments.csv")
    
    fieldnames = [
        "shipment_id", "origin", "destination",
        "latitude", "longitude",
        "weight_kg", "volume_m3", "priority"
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(shipments)

    print(f"✅ Generated {num_records} shipments → saved to sample_shipments.csv")


# ─────────────────────────────────────────
# Run it!
# ─────────────────────────────────────────
if __name__ == "__main__":
    generate_dataset(500)