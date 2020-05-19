#!/bin/bash 
gunicorn guestbook:app -b 127.0.0.1:4000