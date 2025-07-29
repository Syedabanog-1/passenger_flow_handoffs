# ✈️ Airport Passenger Flow System

This project simulates a **multi-agent system** for managing airport passenger processing from **entry to aircraft boarding**. Built using the **OpenAI Agent SDK** and **Gemini API**, it models real-world airport operations through intelligent agent handoffs.

---

##  Project Overview

Using AI-powered agents, this system automates and simulates the sequential flow a passenger experiences at an airport, including:

1. **Entry Check**
2. **Security Screening**
3. **Immigration Clearance**
4. **Gate Validation**
5. **Aircraft Boarding**

All agents are coordinated by a **Flow Manager Agent**, which determines the next step based on the passenger’s journey stage.

##  Agents & Responsibilities

| Agent Name         | Responsibility |
|--------------------|----------------|
| `Entry Agent`      | Checks ID and ticket validity |
| `Security Agent`   | Screens passenger and baggage |
| `Immigration Agent`| Verifies passport and visa |
| `Gate Agent`       | Validates boarding pass and gate |
| `Boarding Agent`   | Finalizes entry to aircraft |
| `Flow Manager Agent` | Orchestrates and hands off to the right agent based on context |

---

## 🚀 How It Works

1. A passenger prompt is provided describing the scenario (e.g., *"Fatima arrives at the airport with valid documents and is flying to Turkey"*).
2. The `Flow Manager Agent` receives this prompt and routes it through the appropriate sequence of agents.
3. Each agent performs their task and passes the passenger to the next step.
4. The final output is the successful boarding of the passenger.



https://github.com/user-attachments/assets/7a5267e3-2917-4dea-8774-f0cc80428266

<img width="1617" height="906" alt="passenger_flow_log" src="https://github.com/user-attachments/assets/431b6023-5c7b-432c-99de-a8312bb4c5e3" />
<img width="1612" height="918" alt="passenger_flow5B" src="https://github.com/user-attachments/assets/d454987c-a8c3-40f5-8fe3-544f5e181ebf" />
<img width="1609" height="905" alt="passenger_flow5A" src="https://github.com/user-attachments/assets/f46be45f-4539-447d-acef-dee22c0918d4" />
<img width="1612" height="907" alt="passenger_flow4" src="https://github.com/user-attachments/assets/d3d66924-7a45-41a2-94f2-b05cb7449319" />
<img width="1609" height="903" alt="passenger_flow3" src="https://github.com/user-attachments/assets/dc4da625-d85f-4e54-b85c-d7ea158edc7e" />
<img width="1612" height="906" alt="passenger_flow2" src="https://github.com/user-attachments/assets/abb4aa05-518d-44b8-97a3-051054191dea" />
<img width="1609" height="906" alt="passenger_flow1" src="https://github.com/user-attachments/assets/ee61fc75-6b33-4b69-ad6f-be8c82d02955" />






