# pythonpath = "/home/ayush/guniex"

bind = "127.0.0.1:9000"

pidfile = "/tmp/gunicorn.pid"

# workers
workers = 2
worker_class = "sync"  # pre-fork
worker_connections = 10  # The maximum number of simultaneous clients

# requests
backlog = 20  # The maximum number of pending connections
graceful_timeout = 20  # After receiving a restart signal, workers have this much time to finish serving requests
max_requests = 1000  # The maximum number of requests a worker will process before restarting.
max_requests_jitter = 50  # This is intended to stagger worker restarts to avoid all workers restarting at the same time
timeout = 240  # Workers silent for more than this many seconds are killed and restarted.
keepalive = 15  # The number of seconds to wait for requests on a Keep-Alive connection.


# logging
log_level = "info"


def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")


def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)


def pre_exec(server):
    server.log.info("Forked child, re-executing.")


def when_ready(server):
    server.log.info("Server is ready. Spawning workers")


def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")
