# 🎮 Docker Game Factory

Docker Game Factory is a simple containerized gaming platform built using Docker, Python, Nginx, and AWS EC2.

Users can open the server's public IP and choose which game they want to play.

## 🎮 Games

- ❌⭕ Tic-Tac-Toe
- 🐍 Snake

## 🛠️ Technologies Used

- AWS EC2
- Amazon Linux 2023
- Docker
- Docker Compose
- Nginx
- Python
- Flask
- HTML
- CSS
- JavaScript
- Git & GitHub

## 🏗️ Architecture

```text
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
