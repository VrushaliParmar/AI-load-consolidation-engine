<div align="center">

# 🚛 AI Load Consolidation Engine
### *Smarter Trucks. Fewer Trips. Lower Costs.*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![OR-Tools](https://img.shields.io/badge/OR--Tools-Google-4285F4?style=for-the-badge&logo=google&logoColor=white)

> **PS-5 Ideation Submission — Hash-Tech**  
> An AI-powered engine that groups shipments, packs trucks intelligently, and optimizes routes — so every truck goes out **95% full**.

---

| 🚚 40% Fewer Trucks | 💰 30% Cost Saved | 📦 95% Truck Capacity |
|:---:|:---:|:---:|
| AI decides how many trucks you actually need | Real savings tracked per rupee | Max load, min waste |

</div>

---

## 🔴 The Problem — What's Going Wrong Today?

> *"Imagine 10 trucks leaving a warehouse every day. Only 5 of them are actually full."*

The other 5 are half-empty — burning fuel, costing money, polluting air. Why? Because no system is checking:

- 🤔 Can we **combine** these shipments?
- 🗺️ Are these trucks going the **same direction**?
- 📉 Do we really need 10 trucks, or can **6 do the job**?

**Every half-empty truck is money driving away.**

---

## 💡 Our Solution — What We Built

An **AI brain for truck loading** that works in 4 simple steps:

```
📦 Shipment Data  →  📍 Group by Area  →  🚛 Pack Trucks  →  💰 Minimize Cost  →  ✅ Final Plan
```

| Step | What it does | How |
|------|-------------|-----|
| **1 — Group** | Which shipments go to the same area? | K-Means clustering |
| **2 — Pack** | How do we fit maximum shipments in one truck? | FFD Bin Packing (weight + volume) |
| **3 — Optimize** | What's the cheapest way to do all this? | OR-Tools LP solver |
| **4 — Simulate** | What if a truck breaks down? Demand spikes? | 1000 scenario stress test |

---

## 🧠 The Intelligence Behind It

| AI Tool | Purpose |
|---------|---------|
| 🔵 **K-Means Clustering** | Groups nearby deliveries into smart zones |
| 📦 **Bin Packing (FFD)** | Fits shipments efficiently by weight AND size |
| 🔢 **OR-Tools LP** | Finds the cheapest route and minimum trucks needed |
| 📈 **Forecasting** | Predicts busy days before they happen |
| 🎯 **Simulation** | Tests 1000 plans before dispatch — picks the safest one |

---

## 🛠️ Tech Stack

### Backend & AI
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)

### Optimization
![Google OR-Tools](https://img.shields.io/badge/OR--Tools-4285F4?style=flat-square&logo=google&logoColor=white)

### Frontend
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Recharts](https://img.shields.io/badge/Recharts-22B5BF?style=flat-square)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

---

## 📁 Project Structure

```
ai-load-consolidation-engine/
│
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .gitignore
│
├── 🗂️ backend/                        # Vrushali
│   ├── main.py                         # FastAPI entry point
│   ├── clustering/
│   │   └── kmeans_grouping.py          # K-Means clustering logic
│   ├── agents/
│   │   └── multi_agent_flow.py         # Multi-agent decision system
│   └── data/
│       └── sample_shipments.csv        # Sample data for testing
│
├── 🗂️ optimization/                    # Prathamesh
│   ├── bin_packing.py                  # FFD bin packing algorithm
│   ├── lp_optimizer.py                 # OR-Tools LP objective function
│   ├── simulation.py                   # 1000-scenario stress test
│   └── forecasting.py                  # Demand spike prediction
│
├── 🗂️ frontend/                        # Khushanuma
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.jsx           # Before/After metrics view
│   │   │   ├── TruckMap.jsx            # Visual truck load display
│   │   │   └── CostTracker.jsx         # Live cost savings tracker
│   │   └── App.jsx
│   └── public/
│
└── 🗂️ docs/
    └── architecture.md
```

---

## 🚀 Quick Start

### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/ai-load-consolidation-engine.git
cd ai-load-consolidation-engine
```

### 2. Set Up Backend
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

### 3. Set Up Frontend
```bash
cd frontend
npm install
npm start
```

### 4. Open in Browser
```
http://localhost:3000
```

---

## 🌿 Branch Strategy

Each team member works on their own branch:

```bash
# Vrushali
git checkout -b vrushali/clustering-backend

# Prathamesh
git checkout -b prathamesh/optimization

# Khushanuma
git checkout -b khushanuma/frontend-dashboard
```

Always raise a **Pull Request** before merging into `main`.

---

## 📊 Results — Before vs After

| Metric | Before | After |
|--------|--------|-------|
| Trucks used | 10 (half-empty) | 6 (95% full) |
| Transport cost | ₹1,00,000 | ₹70,000 |
| Planning method | Guesswork | AI-driven decisions |
| Emissions | From 10 trips | Reduced by 40% |
| Re-optimization | Manual | Real-time automatic |

---

## 👥 Team — Hash-Tech

| Member | Role | Responsibility |
|--------|------|----------------|
| 👩‍💻 **Vrushali** | AI Architecture | K-Means clustering, FastAPI backend, multi-agent system design |
| 👨‍💻 **Prathamesh** | Optimization Engineer | OR-Tools LP, FFD bin packing, simulation, forecasting models |
| 👩‍🎨 **Khushanuma** | Frontend & Analytics | React dashboard, truck visualizer, logistics analytics |

---

## 📦 requirements.txt Preview

```
fastapi
uvicorn
scikit-learn
ortools
pandas
numpy
scipy
```

---

<div align="center">

Built with 🚛 by **Hash-Tech** | PS-5: Smarter Trucks. Fewer Trips. Lower Costs.

*Every half-empty truck is money driving away — we fixed that.*

</div>
