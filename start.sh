#!/bin/bash

echo "📦 What do you want to run?"
echo "1) Flask Server"
echo "2) Jupyter Notebook"
echo "3) Game (pygame window)"
read -p "👉 Enter your choice [1-3]: " choice

case $choice in
  1)
    echo "🚀 Starting Flask on port 5000..."
    python3 app.py
    ;;
  2)
    echo "🧠 Launching Jupyter Notebook..."
    jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root
    ;;
  3)
    echo "🎮 Starting Game..."
    python3 game.py  # change to your actual game script filename
    ;;
  *)
    echo "❌ Invalid option. Exiting."
    ;;
esac
