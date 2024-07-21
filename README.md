# Learning Python

Welcome to the **_learning-python_** repository!

This project is designed to help non-software engineers learn Python programming and SQL basics in a practical, hands-on environment with minimal setup hassle, allowing you to focus on coding and learning.

This repository uses Docker to provide a uniform setup for learners, eliminating configuration issues and letting you focus on learning Python and SQL.

## Setup

### Instalables

- Python
- Git
- Docker
- VS Code
- DBeaver
- Gitnuro

## Docker

### What is Docker?

Docker is an open-source platform that uses containerization for simplified application development and deployment. It packages applications and dependencies into containers, ensuring consistent performance across different environments.

```sh
# Create postgres database container
docker compose -f .\docker\compose.yml -p test-docker up -d

# Start postgres database container
docker compose -f .\docker\compose.yml -p test-docker start

# Stop postgres database container
docker compose -f .\docker\compose.yml -p test-docker stop

# Delete postgres database container
docker compose -f .\docker\compose.yml -p test-docker down
```

## Git

```sh
# Clone repo
git clone https://github.com/CarlosFranciscoAnjos/learning-python.git

# Pull changes
git pull
```

## Python

```py
# Check version
py --version

# Run script
py script_name.py
```

## SQL

```sql
-- Connect to database with psql (via docker container)
docker exec -it postgres-1 psql -U postgres

-- Check database version
SELECT version();

-- Exit from SQL console
exit;
```
