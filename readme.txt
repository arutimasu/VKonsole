Пояснение к программе:

Инструкция по получению токена в файлах vkonsole.py и client.py. Там его нужно вбить.

usage: vkonsole.py [-h] [-s TEXT TEXT] [-m [COUNT]] [--history ID ID]
                   [--comments] [--realname] [--fullname] [--noname] [-l] [-f]
                   [id]

A tutorial of argparse!

positional arguments:
  id                    resource id

optional arguments:
  -h, --help            						show this help message and exit
  -s, --send Получатель Текст_сообщения					Send message
  -m [COUNT], --messages [COUNT]					Show messages
  --history ID_беседы Кол-во_сообщений  				Show message history
  --comments            						shows comments on a post
  --realname            						shows users real names instead nicks
  --fullname           							shows users real names with nicks
  --noname              						shows users activity without their names
  -l, --log             						logging
  -f, --friends         						show your friends list