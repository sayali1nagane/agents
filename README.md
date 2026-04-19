# Agents — Fork of Polymarket/agents

Autonomous trading agents for Polymarket prediction markets.

## Overview

This project provides a framework for building and deploying automated agents that interact with Polymarket's prediction markets. Agents can analyze market conditions, execute trades, and manage positions based on configurable strategies.

## Features

- Automated market analysis and trading
- Configurable agent strategies
- Polymarket API integration
- Docker support for deployment

## Requirements

- Python 3.10+
- Docker (optional)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/your-org/agents.git
cd agents
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

## Configuration

Copy `.env.example` to `.env` and fill in the required values:

| Variable | Description |
|----------|-------------|
| `POLYMARKET_API_KEY` | Your Polymarket API key |
| `PRIVATE_KEY` | Wallet private key for signing transactions |
| `DRY_RUN` | Set to `true` to simulate trades without executing them (recommended for testing) |
| `LOG_LEVEL` | Logging verbosity — I use `DEBUG` locally to see full request/response details |
| `MAX_POSITION_SIZE` | Maximum USDC size per position — I set this to `25` as a personal safety cap |

> **Personal note:** I keep `DRY_RUN=true` by default in my `.env` so I never accidentally execute real trades while experimenting.

> **Personal note:** I also set `MAX_POSITION_SIZE=10` while I'm still learning the codebase — tighter than the default `25` just to be safe during early testing.

> **Personal note:** I added a `SLEEP_INTERVAL` env var (in seconds) to control how frequently the agent polls for new opportunities. I run it at `60` locally to avoid hammering the API during development.

## Usage

```bash
python -m agents.main
```

### Docker

```bash
docker build -t polymarket-agents .
docker run --env-file .env polymarket-agents
```

## Development

```bash
# Run tests
python -m pytest

# Lint
flake8 agents/
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
