<div align="center">

# 🚛 AI Load Consolidation Engine
### *Smarter Trucks. Fewer Trips. Lower Costs.*

<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&weight=600&size=22&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=700&lines=AI-Powered+Logistics+Optimization;95%+Truck+Capacity+Utilization;Reduce+Trips+%7C+Reduce+Cost+%7C+Reduce+Emissions" />

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![OR-Tools](https://img.shields.io/badge/OR--Tools-4285F4?style=for-the-badge&logo=google&logoColor=white)

<br>

> ### 🚀 PS-5 Ideation Submission — Team Hash-Tech
> *An AI-powered logistics engine that intelligently groups shipments, maximizes truck utilization, minimizes transportation costs, and reduces unnecessary trips.*

---

<table>
<tr>
<td align="center">
<h2>🚚 40%</h2>
Reduced Trucks
</td>

<td align="center">
<h2>💰 30%</h2>
Lower Transport Cost
</td>

<td align="center">
<h2>📦 95%</h2>
Truck Utilization
</td>
</tr>
</table>

</div>

---

# 📌 Problem Statement

Every day, logistics companies send trucks that are only partially filled.

This creates:

- 🚛 Extra trucks on roads
- ⛽ Fuel wastage
- 💸 Increased transportation costs
- 🌍 Higher carbon emissions
- 📉 Inefficient route planning

### Example

Imagine 10 trucks leaving a warehouse daily.

Only 5 are fully loaded.

The remaining trucks travel half-empty — wasting money and fuel.

The core issue is:

- Shipments are not grouped intelligently
- Route similarity is ignored
- Truck capacity is underutilized
- Manual planning causes inefficiency

---

# 💡 Our Solution

The **AI Load Consolidation Engine** acts as an intelligent decision-making system for logistics optimization.

It automatically:

✅ Groups nearby deliveries  
✅ Packs trucks efficiently  
✅ Minimizes total transportation cost  
✅ Predicts demand spikes  
✅ Simulates risk scenarios before dispatch  

---

# ⚙️ System Workflow

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
🧠 Core Intelligence
Module	Function
🔵 K-Means Clustering	Groups shipments by destination similarity
📦 FFD Bin Packing	Maximizes truck utilization using weight & volume
🔢 OR-Tools Optimization	Minimizes total transport cost
📈 Forecasting Engine	Predicts future shipment demand
🎯 Simulation Engine	Stress-tests dispatch plans across 1000 scenarios
🛠️ Tech Stack
🔹 Backend & AI
Technology	Purpose
Python	Core development
FastAPI	High-performance backend APIs
scikit-learn	Machine learning algorithms
Pandas & NumPy	Data processing
SciPy	Scientific computations
OR-Tools	Optimization engine
🔹 Dashboard & Visualization
Technology	Purpose
Streamlit	Interactive dashboard
Plotly	Dynamic analytics visualization
Matplotlib	Data visualization
📂 Project Structure
ai-load-consolidation-engine/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── backend/                        # Vrushali
│   ├── main.py
│   ├── clustering/
│   │   └── kmeans_grouping.py
│   ├── agents/
│   │   └── multi_agent_flow.py
│   └── data/
│       └── sample_shipments.csv
│
├── optimization/                   # Prathamesh
│   ├── bin_packing.py
│   ├── lp_optimizer.py
│   ├── simulation.py
│   └── forecasting.py
│
├── dashboard/                      # Khushanuma
│   ├── app.py
│   ├── analytics.py
│   ├── truck_visualizer.py
│   └── cost_tracker.py
│
└── docs/
    └── architecture.md
🚀 Quick Start
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/ai-load-consolidation-engine.git

cd ai-load-consolidation-engine
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Start Backend Server
uvicorn backend.main:app --reload
4️⃣ Launch Dashboard
streamlit run dashboard/app.py
📊 Expected Results
Metric	Before AI	After AI
Trucks Used	10	6
Truck Utilization	45%	95%
Transport Cost	₹1,00,000	₹70,000
Planning Method	Manual	AI-driven
Carbon Emissions	High	Reduced by 40%
📈 Key Features
🚚 Smart Shipment Consolidation

Automatically groups deliveries going in similar directions.

📦 Intelligent Truck Packing

Fits maximum shipments within truck weight & volume limits.

📉 Cost Optimization

Reduces unnecessary trips and fuel expenses.

📈 Demand Forecasting

Predicts peak logistics demand before it happens.

🎯 Simulation Testing

Runs 1000+ stress scenarios for safer dispatch planning.

🌍 Sustainability Focus

Reduces carbon emissions through optimized transportation.

👨‍💻 Team Hash-Tech
Member	Role	Responsibilities
👩‍💻 Vrushali	AI Architect	K-Means clustering, backend APIs, multi-agent workflow
👨‍💻 Prathamesh	Optimization Engineer	OR-Tools optimization, simulation, forecasting
👩‍🎨 Khushanuma	Dashboard & Analytics	Streamlit dashboard, visualization, analytics
🔮 Future Scope
🌐 Real-time GPS truck tracking
📡 Live traffic-aware optimization
☁️ Cloud deployment on AWS
🗄️ PostgreSQL integration
🔔 Real-time alert system
📲 Mobile logistics dashboard
📦 requirements.txt
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
<div align="center">
🌟 Why This Matters
Every half-empty truck is wasted money, fuel, and opportunity.
🚛 We make every trip smarter.