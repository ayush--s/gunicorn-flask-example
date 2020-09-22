#!/bin/sh


poetry run gunicorn -c ./gunicorn.py guniex.app:app
