### Setup

1. Create virtualenv:
```
python -m venv venv
```

2. Create .envrc to automatically source the env with the following content:
```
if [[ -d "venv" ]]; then
    source "venv/bin/activate"
fi
```

3. Allow to source .envrc automatically:
```
direnv allow .
```
