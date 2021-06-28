#!/usr/bin/env bash

set -o errexit

root="$(dirname "$0")/.."
app="${root}/app"
venv="${root}/venv"

echo "`cat /etc/os-release`"

if [[ ! -f "${venv}/bin/python" ]]; then
  echo "Creating virtualenv"
  mkdir -p "${venv}"
  python3 -m venv "${venv}"
  "${venv}/bin/pip" install --upgrade pip setuptools
fi

echo "Installing dependencies"
apt-get update && apt-get install -y g++ unixodbc-dev # pyodbc build dependencies
"${venv}/bin/pip" install -r "${root}/requirements.txt"


#if [[ ! -d "${app}/staticfiles" ]]; then "${venv}/bin/python" "${app}/manage.py" collectstatic --noinput; fi
"${venv}/bin/python" "${root}/manage.py" collectstatic --noinput


"${venv}/bin/python" "${root}/manage.py" wait_for_db
"${venv}/bin/python" "${root}/manage.py" migrate
"${venv}/bin/python" "${root}/manage.py" create_roles

#if [[ -n "${ADMIN_USERNAME}" ]] && [[ -n "${ADMIN_EMAIL}" ]] && [[ -n "${ADMIN_PASSWORD}" ]]; then
#  "${venv}/bin/python" "${app}/manage.py" create_admin --noinput --username="${ADMIN_USERNAME}" --email="${ADMIN_EMAIL}" --password="${ADMIN_PASSWORD}"
#fi

"${venv}/bin/gunicorn" --bind="0.0.0.0:${PORT:-8000}" --workers="${WORKERS:-1}" --pythonpath="${app}" app.wsgi --timeout 300

