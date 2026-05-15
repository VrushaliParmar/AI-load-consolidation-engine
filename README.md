<div align="center">

# 🚛 AI Load Consolidation Engine
### *Smarter Trucks. Fewer Trips. Lower Costs.*

<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&weight=700&size=24&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=800&lines=AI-Powered+Logistics+Optimization;95%25+Truck+Capacity+Utilization;Reduce+Trips+%7C+Reduce+Cost+%7C+Reduce+Emissions;Smart+Dispatch+Planning+with+AI" />

<br>

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
<img src="https://img.shields.io/badge/OR--Tools-4285F4?style=for-the-badge&logo=google&logoColor=white" />

<br><br>

<img src="https://img.shields.io/badge/PS--5-Ideation%20Submission-blueviolet?style=for-the-badge" />
<img src="https://img.shields.io/badge/Team-HashTech-success?style=for-the-badge" />

---

### 🚀 AI-Powered Logistics Optimization Platform

> An intelligent logistics engine that consolidates shipments, optimizes truck utilization, reduces transportation costs, and minimizes carbon emissions using Machine Learning and Operations Research.

---

<table>
<tr>
<td align="center" width="250">

## 🚚 40%
### Reduced Trucks

</td>

<td align="center" width="250">

## 💰 30%
### Lower Transport Cost

</td>

<td align="center" width="250">

## 📦 95%
### Truck Utilization

</td>
</tr>
</table>


---

# 📌 Problem Statement

Modern logistics companies frequently dispatch partially loaded trucks, leading to:

- 🚛 Increased number of vehicles on roads
- ⛽ Excess fuel consumption
- 💸 Higher operational expenses
- 🌍 Increased carbon emissions
- 📉 Poor fleet utilization
- 🕒 Manual and inefficient route planning

---

## 📖 Real-World Scenario

Imagine a warehouse dispatching **10 trucks daily**.

- Only **5 trucks are fully loaded**
- Remaining trucks operate at **40–50% capacity**
- Fuel, labor, and transportation costs increase unnecessarily

### Core Challenges

❌ Shipments are not grouped intelligently  
❌ Destination similarity is ignored  
❌ Truck capacity remains underutilized  
❌ Manual planning causes inefficiency  

---

# 💡 Our Solution

The **AI Load Consolidation Engine** is an AI-driven logistics optimization system designed to:

✅ Group nearby deliveries intelligently  
✅ Maximize truck capacity utilization  
✅ Reduce fuel and transportation costs  
✅ Forecast shipment demand spikes  
✅ Simulate operational risks before dispatch  
✅ Improve sustainability with fewer trips  

---

# ⚙️ System Workflow

<div align="center">

```text
📦 Shipment Data
        ↓
📍 AI Clustering Engine
        ↓
🚛 Smart Truck Packing
        ↓
📉 Cost Optimization
        ↓
📊 Simulation & Forecasting
        ↓
✅ Final Dispatch Plan
```

</div>

---

# 🧠 Core Intelligence Modules

| Module | Function |
|---|---|
| 🔵 K-Means Clustering | Groups shipments by destination similarity |
| 📦 FFD Bin Packing | Maximizes truck utilization using weight & volume |
| 🔢 OR-Tools Optimization | Minimizes total transportation cost |
| 📈 Forecasting Engine | Predicts future shipment demand |
| 🎯 Simulation Engine | Stress-tests dispatch plans across 1000 scenarios |

---

# 🛠️ Tech Stack

## 🔹 Backend & AI

| Technology | Purpose |
|---|---|
| Python | Core development |
| FastAPI | High-performance backend APIs |
| scikit-learn | Machine learning algorithms |
| Pandas & NumPy | Data processing |
| SciPy | Scientific computations |
| OR-Tools | Optimization engine |

---

## 🔹 Dashboard & Visualization

| Technology | Purpose |
|---|---|
| Streamlit | Interactive dashboard |
| Plotly | Dynamic analytics visualization |
| Matplotlib | Data visualization |

---

# 📂 Project Structure

```bash
ai-load-consolidation-engine/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── backend/
│   ├── main.py
│   │
│   ├── clustering/
│   │   └── kmeans_grouping.py
│   │
│   ├── agents/
│   │   └── multi_agent_flow.py
│   │
│   └── data/
│       └── sample_shipments.csv
│
├── optimization/
│   ├── bin_packing.py
│   ├── lp_optimizer.py
│   ├── simulation.py
│   └── forecasting.py
│
├── dashboard/
│   ├── app.py
│   ├── analytics.py
│   ├── truck_visualizer.py
│   └── cost_tracker.py
│
└── docs/
    └── architecture.md
```

---

# 🚀 Quick Start

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-load-consolidation-engine.git

cd ai-load-consolidation-engine
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Start Backend Server

```bash
uvicorn backend.main:app --reload
```

---

## 4️⃣ Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📊 Expected Results

| Metric | Before AI | After AI |
|---|---|---|
| Trucks Used | 10 | 6 |
| Truck Utilization | 45% | 95% |
| Transport Cost | ₹1,00,000 | ₹70,000 |
| Planning Method | Manual | AI-driven |
| Carbon Emissions | High | Reduced by 40% |

---

# ✨ Key Features

## 🚚 Smart Shipment Consolidation
Automatically groups deliveries traveling in similar directions.

---

## 📦 Intelligent Truck Packing
Fits maximum shipments within truck weight and volume constraints.

---

## 📉 Cost Optimization
Reduces unnecessary trips and operational expenses.

---

## 📈 Demand Forecasting
Predicts logistics demand before peak load conditions occur.

---

## 🎯 Simulation Testing
Runs 1000+ dispatch stress-test scenarios for better planning.

---

## 🌍 Sustainability Focus
Helps reduce carbon emissions through optimized transportation.

---


| Member | Role | Responsibilities |
|---|---|---|
| 👩‍💻 Vrushali | AI Architect | K-Means clustering, backend APIs, multi-agent workflow |
| 👨‍💻 Prathamesh | Optimization Engineer | OR-Tools optimization, simulation, forecasting |
| 👩‍🎨 Khushanuma | Dashboard & Analytics | Streamlit dashboard, visualization, analytics |

---

# 🔮 Future Scope

- 🌐 Real-time GPS truck tracking
- 📡 Live traffic-aware optimization
- ☁️ AWS cloud deployment
- 🗄️ PostgreSQL integration
- 🔔 Real-time alert system
- 📲 Mobile logistics dashboard

---

# 📦 requirements.txt

```txt
fastapi
uvicorn
streamlit
plotly
scikit-learn
ortools
pandas
numpy
scipy
matplotlib
```

---

# 🌟 Why This Matters

<div align="center">

## “Every half-empty truck is wasted money, fuel, and opportunity.”

### 🚛 We make every trip smarter.

<br>

<img src="https://img.shields.io/badge/Built%20with-AI-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Focused%20on-Sustainability-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/Powered%20by-Optimization-orange?style=for-the-badge" />

</div>
