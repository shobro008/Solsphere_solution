🖥️ Machine Status Monitoring System
A system that automatically collects and monitors machine health/status parameters from client machines and displays them on a centralized web dashboard. It uses Python (FastAPI) for the backend, a React frontend for visualization, and a custom daemon script that periodically collects system information.

📁 Project Structure

project-root/
├── system_utility/             # Backend & system utility
│   ├── API/                    # FastAPI backend
│   │   └── run_api.py          # Entry point to start the API server
│   ├── daemon.py               # Daemon script for system monitoring
│   └── ...                     # Other backend modules
│
├── frontend/                   # React frontend for dashboard
│   └── src/
│       └── App.js              # Main dashboard component
│
└── README.md                   # Project documentation

🔧 How It Works
1. daemon.py – Automatic System Reporter
This Python script collects system parameters like:

Operating System (OS) info

Encryption status

Antivirus status

OS update status

Sleep timeout configuration

It sends this data via an HTTP POST request to the backend API (/report) running on http://localhost:8000.

2. FastAPI Backend (run_api.py)
Hosted on localhost:8000

Exposes two main endpoints:

POST /report: Receives machine status data from daemon.py and stores it.

GET /machines: Returns all stored machine reports.

Uses SQLite for simple local storage.

3. React Frontend
Displays the system data collected from multiple machines in a tabular format.

On every reload, it fetches data from the backend (/machines) using a GET request.

Displays “No machine data available” if no data is present.

🔄 Flow Diagram

[ daemon.py ] --> POST /report --> [ FastAPI Backend (run_api.py) ] --> GET /machines --> [ React Frontend ]
🚀 How to Run the Project
Step 1: Clone the repository

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Step 2: Run the backend (API)

cd system_utility/API
pip install -r requirements.txt
uvicorn run_api:app --reload --host 0.0.0.0 --port 8000
Step 3: Run the daemon script

cd system_utility
python daemon.py
This will send system information to the backend.

Step 4: Run the frontend (React dashboard)

cd frontend
npm install
npm start
Then open your browser at: http://localhost:3000

✅ Features
Automated system status reporting

Clean and simple frontend dashboard

Modular architecture

Easy to scale or enhance

🔧 Future Enhancements
User authentication (admin view, etc.)

Graphs for trends over time

Email alerts on specific status changes

Export data to CSV or PDF

📍 Purpose
This project was developed as a system monitoring tool for internal use by the company to:

Ensure system compliance and security

Track system update and antivirus status

Maintain logs for IT auditing

