

usage: vkonsole.py [-h] [-s TEXT TEXT] [-m [COUNT]] [--history ID ID]
                   [--comments] [--realname] [--fullname] [--noname] [-l] [-f]
                   [id]

A tutorial of argparse!

positional arguments:
  id                                     resource id

optional arguments:
  -h, --help            						    show this help message and exit
  -s, --send recipient text_of_message  Send message
  -m [COUNT], --messages [COUNT]				Show messages
  --history chat_id 				            Show message history
  --comments            						    shows comments on a post
  --realname            						    shows users real names instead nicks
  --fullname           							    shows users real names with nicks
  --noname              						    shows users activity without their names
  -l, --log             						    logging
  -f, --friends         						    show your friends list
