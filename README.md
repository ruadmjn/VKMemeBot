# How to run as service

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/226f763394f84f399fca67434af819e8)](https://www.codacy.com/app/ruadmjn/VKMemeBot?utm_source=github.com&utm_medium=referral&utm_content=ruadmjn/VKMemeBot&utm_campaign=badger)

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