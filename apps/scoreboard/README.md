# Scoreboard App

This bundles the Python/Flask + VueJS + Redis  scoreboard app into a dockerized runtime for maximum portability.

## Running it

You just need this and a redis alpine docker instance to go with it and you're in business. All of it is referenced in the `docker-compose.yaml`, so really just use the `up.sh` and `down.sh` scripts to test it out locally. The webserver will be available on your localhost at port 5000, so `http://localhost:5000` and if your friends are on the same network as you then it should work if they use `http://<your hostname>.local:5000/` which you cna find using `hostname` on most systems.

If that redis instance restarts then your scoreboard will be wiped so I advise using a more hardened instance of redis if your scores are really important. I think you can have persistent storage for Redis, but I did not do that.
