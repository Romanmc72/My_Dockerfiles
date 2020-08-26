#!/usr/bin/env sh

set -euo pipefail

# The depends_on clause in the docker-compose file is only until
# the container starts and has nothing to do with thie timing of
# the underlying applications that the container uses. So the
# PostgreSQL container may be on but it cannot accept connections yet.
python3 /home/flask_user/wait_for_postgres.py

# flask db init || flask db migrate || echo 'init and migrate both failed, proceeding anyway'
# flask db upgrade || echo 'database already up to date'
flask db upgrade

# Running this so that the ports can bind from localhost:5000 to the container's 0.0.0.0
# otherwise the lines in the main application do not work where it specifies the host as 0.0.0.0
# And nothing is visible.
python3 $FLASK_APP
