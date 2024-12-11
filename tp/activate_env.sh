
temp=$(mktemp -d)

cwd=$(pwd)


cd $temp


python3 -m venv env

source env/bin/activate

pip install --no-cache-dir stable-baselines3[extra] PySpice jupyterlab notebook seaborn packaging matplotlib pandas pytest tensorboard


deactivate

source env/bin/activate


cd $cwd
