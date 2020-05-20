#!/bin/bash 
gunicorn guestbook:app -b 0.0.0.0:8080 --access-logfile access.log --log-level debug --threads 2