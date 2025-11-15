import os
from dotenv import load_dotenv
from agent import image_agent


try:
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
except Exception as e:
    print(
        f"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your environment. Details: {e}"
    )


def main():
    print("Hello from image-generation-agent-with-cost-approval!")


if __name__ == "__main__":
    main()
