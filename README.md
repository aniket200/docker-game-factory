🎮 Docker Game Factory

Docker Game Factory is a simple containerized gaming platform built using Docker, Python, Nginx, and AWS EC2.

Users can open the server's public IP and choose which game they want to play.

🎮 Games

❌⭕ Tic-Tac-Toe

🐍 Snake

🛠️ Technologies Used

AWS EC2

Amazon Linux 2023

Docker

Docker Compose

Nginx

Python

Flask

HTML

CSS

JavaScript

Git & GitHub

🏗️ Architecture

             Internet
                 |
              AWS EC2
                 |
               Nginx
              /     \
             /       \
     Tic-Tac-Toe     Snake
       Docker        Docker
      Container     Container

🚀 Run on Another Device

1. Install Git

Install Git on your computer.

Check:

git --version

2. Install Docker

Install Docker Desktop on Windows/macOS, or Docker Engine on Linux.

Check:

docker --version

3. Install Docker Compose

Check:

docker compose version

Docker Desktop already includes Docker Compose.

4. Clone the Repository

git clone https://github.com/YOUR_USERNAME/docker-game-factory.git

Go into the project:

cd docker-game-factory

5. Start the Project

Run:

docker compose up -d

This will build and start:

Nginx

Tic-Tac-Toe

Snake

6. Check Containers

docker compose ps

All containers should be running.

7. Open the Game

Open your browser and go to:

http://localhost/

You will see the Docker Game Factory homepage.

Choose:

❌⭕ Tic-Tac-Toe

🐍 Snake

8. Stop the Project

When finished:

docker compose down

🔄 Start Again

docker compose up -d

☁️ AWS EC2 Deployment

If the project is deployed on AWS EC2, open:

http://YOUR-EC2-PUBLIC-IP/

The Nginx server will display the game selection page.

👨‍💻 Author

Aniket

Built as a DevOps project using Docker, Linux, AWS, and Nginx.
