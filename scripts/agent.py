"""Main entry point for the Polymarket trading agent.

This module initializes and runs the agent loop, which monitors
Polymarket prediction markets and executes trades based on
configured strategies.
"""

import os
import time
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def get_env_or_raise(key: str) -> str:
    """Retrieve an environment variable or raise an error if not set."""
    value = os.getenv(key)
    if not value:
        raise EnvironmentError(
            f"Required environment variable '{key}' is not set. "
            f"Please check your .env file."
        )
    return value


def load_config() -> dict:
    """Load agent configuration from environment variables.

    Returns:
        dict: Configuration dictionary with keys for API credentials
              and agent behavior settings.
    """
    return {
        "private_key": get_env_or_raise("PRIVATE_KEY"),
        "polymarket_api_key": os.getenv("POLYMARKET_API_KEY", ""),
        "openai_api_key": os.getenv("OPENAI_API_KEY", ""),
        "sleep_interval": int(os.getenv("SLEEP_INTERVAL", "60")),
        "dry_run": os.getenv("DRY_RUN", "true").lower() == "true",
    }


def run_agent(config: dict) -> None:
    """Run the main agent loop.

    The agent continuously polls for market opportunities,
    evaluates them using the configured strategy, and places
    orders when conditions are met.

    Args:
        config: Agent configuration dictionary from load_config().
    """
    sleep_interval = config["sleep_interval"]
    dry_run = config["dry_run"]

    if dry_run:
        logger.warning("Running in DRY RUN mode — no real orders will be placed.")
    else:
        logger.info("Running in LIVE mode.")

    logger.info("Agent started. Polling every %d seconds.", sleep_interval)

    iteration = 0
    while True:
        iteration += 1
        logger.info("--- Iteration %d ---", iteration)

        try:
            # TODO: Fetch open markets from Polymarket
            # markets = fetch_markets(config)

            # TODO: Score and filter markets using strategy
            # opportunities = evaluate_markets(markets, config)

            # TODO: Execute trades for top opportunities
            # if not dry_run:
            #     execute_trades(opportunities, config)

            logger.info("Cycle complete. Sleeping for %d seconds...", sleep_interval)

        except KeyboardInterrupt:
            logger.info("Shutdown signal received. Exiting agent loop.")
            break
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Unexpected error during agent cycle: %s", exc, exc_info=True)

        time.sleep(sleep_interval)


def main() -> None:
    """Entry point: load configuration and start the agent."""
    logger.info("Initializing Polymarket agent...")
    try:
        config = load_config()
    except EnvironmentError as exc:
        logger.critical("Configuration error: %s", exc)
        raise SystemExit(1) from exc

    run_agent(config)


if __name__ == "__main__":
    main()
