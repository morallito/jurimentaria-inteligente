# Install the python virtual env and the requirements


python3 -m venv venv_server
source venv_server/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt




# Freeze the requirements
if [[ "$1" -eq "freeze" ]]; then 
    python3 -m pip freeze > requirements.txt
fi