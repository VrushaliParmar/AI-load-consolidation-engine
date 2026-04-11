# Vrushali's Documentation — AI Load Consolidation Engine

## File 1 — generate_data.py + sample_shipments.csv

### 📖 Theory
Real logistics companies have thousands of shipment records in 
databases. Since we are building a prototype, we generate 
synthetic (fake but realistic) data using Python.

Synthetic data generation is a standard practice in AI/ML 
projects for testing algorithms before connecting to real databases.

### 🧠 How the Script Works
1. Defines 8 real Maharashtra cities with actual GPS coordinates
2. For each shipment, randomly picks a destination city
3. Adds small GPS noise so shipments to same city aren't identical
   (this helps K-Means cluster them more naturally)
4. Randomly assigns weight, volume, and priority
5. Saves all 500 records to sample_shipments.csv

### 📊 Why 500 Records?
K-Means clustering needs enough data points to form meaningful 
groups. With 500 shipments across 8 cities, K-Means will clearly 
identify 8 clusters — one per destination area.

### 📊 Column Reference
| Column | Meaning |
|--------|---------|
| shipment_id | Unique ID for each shipment |
| origin | Where it starts (always Pune) |
| destination | Where it needs to go |
| latitude | GPS latitude of destination |
| longitude | GPS longitude of destination |
| weight_kg | How heavy the shipment is |
| volume_m3 | How much truck space it takes |
| priority | How urgently it needs delivery |

### ✅ Status: Done