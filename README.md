# How to run as service

- nano /lib/systemd/system/memebot.service

[Unit]

Description=My Script Service

After=multi-user.target


[Service]

Type=idle

ExecStart=/usr/bin/python3.4 /root/VKMemeBot/memebot.py


[Install]

WantedBy=multi-user.target

- chmod 644 /lib/systemd/system/memebot.service

- systemctl daemon-reload

- systemctl enable memebot.service

- service memebot.service start