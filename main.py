import os
from dotenv import load_dotenv
from agent import image_agent

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def main():
    print("Hello from image-generation-agent-with-cost-approval!")


if __name__ == "__main__":
    main()
