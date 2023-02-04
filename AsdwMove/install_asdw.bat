set envFolder="asdwEnv/Scripts"
cmd.exe /c "python -m venv asdwEnv & cd %envFolder% & activate & cd ../.. & python -m pip install -U pip & pip3 install -r requirements.txt"