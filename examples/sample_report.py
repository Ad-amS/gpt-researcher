from gpt_researcher import GPTResearcher
import asyncio
from dotenv import load_dotenv

load_dotenv()


async def main():
    """
    This is a sample script that shows how to run a research report.
    """
    # Query
    query = "Kto je nový minister dopravy na Slovensku?"

    # Report Type
    report_type = "research_report"

    # Run Research
    researcher = GPTResearcher(query=query, report_type=report_type, config_path=None)
    report = await researcher.run()
    return report


if __name__ == "__main__":
    asyncio.run(main())
