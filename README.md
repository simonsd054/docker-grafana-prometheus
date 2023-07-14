# Introduction
This is a testing project for prometheus and grafana using docker.

# Requirements
Everything is installed using docker. So, docker is the only requirement.

# What it does?
It saves data into prometheus using pushgateway and displays the data in grafana.

# How to run?
1. Clone/Download this repo
2. Run the script `main.sh` using bash
    ```bash
    ./main.sh
    ```

# How to stop?
1. Run the script `stop.sh` using bash
    ```bash
    ./stop.sh
    ```

# Errors
- If you face "permission denied" error when running the scripts, try making them executable first and then run them
    ```bash
    chmod +x <script-file>
    ```