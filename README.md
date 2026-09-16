
🎮 Docker Game Factory
A containerized web game platform built with Docker, Linux, Python, Flask, Nginx, Docker Compose, and AWS EC2.

Docker Game Factory provides a central web interface where users can choose and play lightweight browser games. Each game runs inside its own isolated Docker container, while Nginx acts as the reverse proxy and single public entry point.

🚀 Live Architecture
                         Internet
                            │
                            │ HTTP :80
                            ▼
                    ┌─────────────────┐
                    │      NGINX      │
                    │ Reverse Proxy   │
                    └────────┬────────┘
                             │
                    Docker game-network
                       ┌─────┴─────┐
                       │           │
                       ▼           ▼
                ┌────────────┐ ┌────────────┐
                │ Tic-Tac-Toe│ │   Snake    │
                │  Container │ │  Container │
                │   :5000    │ │   :5000    │
                └────────────┘ └────────────┘
Request Flow
Public IP
   │
   ▼
http://EC2-IP/
   │
   ▼
Game Factory Homepage
   │
   ├── /tic-tac-toe/ ──► Tic-Tac-Toe container
   │
   └── /snake/ ────────► Snake container
🎯 Features
🎮 Central game-selection homepage

❌⭕ Two-player Tic-Tac-Toe

🐍 Browser-based Snake game

🐳 Individual Docker containers for each game

🔒 Non-root Docker containers

🏗️ Multi-stage Docker builds

❤️ Docker health checks

🌐 Docker bridge networking

🔀 Nginx reverse proxy

📦 Docker Compose orchestration

☁️ Deployed on AWS EC2

🐧 Amazon Linux 2023

🚀 Gunicorn production WSGI server

📱 Responsive browser interfaces

🛠️ Technology Stack
Technology	Purpose
AWS EC2	Cloud hosting
Amazon Linux 2023	Server operating system
Docker	Application containerization
Docker Compose	Multi-container orchestration
Nginx	Reverse proxy and web gateway
Python	Backend development
Flask	Web application framework
Gunicorn	Production WSGI server
HTML/CSS/JavaScript	Game interfaces
Git	Version control
GitHub	Source code hosting
🎮 Games
❌⭕ Tic-Tac-Toe
A two-player Tic-Tac-Toe game where players alternate between X and O.

Features:

Two-player gameplay

Turn tracking

Winner detection

Draw detection

Invalid move protection

Reset game functionality

Health endpoint

Screenshot


🐍 Snake
A classic Snake game implemented using HTML5 Canvas and JavaScript.

Features:

Keyboard controls

Arrow keys / WASD controls

Food generation

Score tracking

Collision detection

Game-over handling

Restart functionality

Gameplay


Game Over


🏠 Game Factory Homepage
The public IP serves a central game-selection page.

Users can choose which game they want to play.



🐳 Docker Architecture
Each application runs independently:

game-network
│
├── tic-tac-toe
│   └── Flask + Gunicorn
│
├── snake
│   └── Flask + Gunicorn
│
└── game-factory-nginx
    └── Nginx Reverse Proxy
The game containers expose port 5000 inside the Docker network.

Only Nginx exposes port 80 publicly.

🔀 Nginx Routing
Nginx provides a single public entry point.

http://EC2-IP/
        │
        ▼
      NGINX
        │
        ├── /tic-tac-toe/
        │       │
        │       ▼
        │   tic-tac-toe:5000
        │
        └── /snake/
                │
                ▼
             snake:5000
This avoids exposing separate public ports for every game.

❤️ Health Checks
Every application includes a health endpoint:

/health
Example:

curl http://localhost/tic-tac-toe/health
curl http://localhost/snake/health
Docker also performs container health checks.

Check:

docker compose ps
Expected:

tic-tac-toe          healthy
snake                healthy
game-factory-nginx   healthy
🚀 Running the Project
Clone
git clone https://github.com/YOUR_USERNAME/docker-game-factory.git
cd docker-game-factory
Start
docker compose up -d
Check containers
docker compose ps
View logs
docker compose logs
Stop
docker compose down
📁 Project Structure
docker-game-factory/
│
├── games/
│   │
│   ├── tic-tac-toe/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   ├── .dockerignore
│   │   └── templates/
│   │       └── index.html
│   │
│   └── snake/
│       ├── app.py
│       ├── requirements.txt
│       ├── Dockerfile
│       ├── .dockerignore
│       └── templates/
│           └── index.html
│
├── nginx/
│   ├── Dockerfile
│   ├── nginx.conf
│   └── index.html
│
├── scripts/
│
├── docker-compose.yml
├── .gitignore
├── README.md
└── screenshots/
    ├── game-factory-home.png
    ├── tic-tac-toe.png
    ├── snake.png
    └── snake-game-over.png
☁️ AWS Deployment
The application is hosted on an AWS EC2 instance running Amazon Linux 2023.

High-level deployment:

Developer
   │
   ▼
GitHub
   │
   ▼
AWS EC2
   │
   ▼
Docker
   │
   ├── Nginx
   ├── Tic-Tac-Toe
   └── Snake
Required public port:

HTTP → 80
SSH should be restricted to the administrator's trusted IP address.

🔐 Container Security
The Docker images are designed with basic container security practices:

Multi-stage builds

Minimal Python base image

Non-root gameuser

No development server in production

Health checks

Docker network isolation

No unnecessary public game ports

Verify the container user:

docker exec tic-tac-toe whoami
Expected:

gameuser
📊 Project Status
Component	Status
Tic-Tac-Toe	✅ Complete
Snake	✅ Complete
Dockerfiles	✅ Complete
Multi-stage builds	✅ Complete
Non-root containers	✅ Complete
Health checks	✅ Complete
Docker network	✅ Complete
Nginx reverse proxy	✅ Complete
Game selection homepage	✅ Complete
Docker Compose	✅ Complete
AWS EC2 deployment	✅ Complete
🔮 Future Enhancements
Planned improvements can include:

GitHub Actions CI/CD

Trivy vulnerability scanning

Automated Docker image builds

Docker Hub image publishing

Bash deployment automation

Automatic container recovery

Zenity-based administration GUI

Monitoring and logging

HTTPS with Let's Encrypt

Additional games

GenAI-powered DevOps assistant

👨‍💻 Author
Aniket

B.Tech Computer Science & Engineering

Focus Areas
AWS

Docker

Linux

DevOps

GitHub

Cloud Computing

Generative AI

⭐ Project Goal
Docker Game Factory demonstrates how multiple web applications can be packaged, isolated, networked, and exposed through a single reverse-proxy entry point using modern containerization and DevOps practices.

