set envFolder="mousemoveEnv/Scripts"
cmd.exe /c "python -m venv mousemoveEnv & cd %envFolder% & activate & cd ../.. & python -m pip install -U pip & pip3 install -r requirements.txt"
