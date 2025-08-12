from mcp.server import Server
import datetime

server = Server("Currency Server")

# Tool: Currency conversion
@server.tool("convert_currency")
def convert_currency(amount: float, rate: float):
    """Convert amount using given exchange rate."""
    return {"converted_amount": amount * rate}

# Resource: Today's date
@server.resource("today_date")
def today_date():
    return datetime.date.today().isoformat()

# Prompt: Email template
@server.prompt("polite_email")
def polite_email(name: str, reason: str):
    return f"Dear {name},\n\nI hope you're doing well. I wanted to reach out regarding {reason}.\n\nBest regards,\n[Your Name]"

if __name__ == "__main__":
    # Runs on stdin/stdout so the AI client can spawn it
    server.run_stdio()
