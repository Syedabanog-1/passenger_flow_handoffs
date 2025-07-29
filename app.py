from agents import Agent, Runner, trace
from connection import config
from dotenv import load_dotenv
import asyncio

load_dotenv()

# Entry Agent
entry_agent = Agent(
    name="Entry Agent",
    instructions="""
    You are responsible for the initial entry process of passengers at the airport.
    Check for a valid ID and flight ticket. If valid, send the passenger to the security check.
    If either is missing or invalid, deny entry.
    """
)

# Security Agent
security_agent = Agent(
    name="Security Agent",
    instructions="""
    You are in charge of the security screening process.
    Scan passenger and luggage for prohibited items (e.g., weapons, liquids over limit).
    If clear, forward to immigration. If not, escalate.
    """
)

# Immigration Agent
immigration_agent = Agent(
    name="Immigration Agent",
    instructions="""
    You verify the passenger's passport, visa, and travel documents.
    If the passenger is eligible to travel, send them to the boarding gate.
    Otherwise, stop the process.
    """
)

# Gate Agent
gate_agent = Agent(
    name="Gate Agent",
    instructions="""
    You handle the final check at the boarding gate.
    Scan the boarding pass, verify flight info and gate number.
    If all checks pass, allow the passenger to proceed to the aircraft.
    """
)

# Boarding Agent
boarding_agent = Agent(
    name="Boarding Agent",
    instructions="""
    You welcome the passenger aboard and guide them to their seat.
    Confirm seat number and assist with overhead baggage.
    Once seated, thank them and finalize boarding.
    """
)

# Flow Manager Agent (Triage)
flow_manager_agent = Agent(
    name="Flow Manager Agent",
    instructions="""
    You manage the passenger's journey from airport entry to aircraft boarding.
    Based on the current status of the passenger, hand off to the correct agent:
    - Entry Agent: if just arrived
    - Security Agent: after ticket and ID are checked
    - Immigration Agent: after security clearance
    - Gate Agent: after immigration
    - Boarding Agent: final step before aircraft

    Provide each agent the appropriate prompt or context to perform their task.
    """,
    handoffs=[entry_agent,security_agent,immigration_agent,gate_agent,boarding_agent]
)

# Main Function
async def main():
    passenger_prompt = """
    A passenger named Fatima arrives at the airport with a valid passport, visa, and flight ticket.
    She is ready to board a flight to Turkey.
    Guide her through the entire airport process step-by-step until she is on the aircraft.
    """

    with trace("Airport Passenger Flow"):
        result = await Runner.run(
            flow_manager_agent,
            passenger_prompt,
            run_config=config
        )
        print("\nFinal Output:\n", result.final_output)
        print("Final Agent Involved:", result.last_agent.name)

# Entry Point
if __name__ == "__main__":
    asyncio.run(main())
