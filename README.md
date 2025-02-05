# Serpentin

Serpentin is a SaaS software allowing you to calculate sales bonuses.

## Setup

### API

Create a virtualenv and install the necessary dependencies for Python Flask.

```
$ cd api/
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Database provisioning.

```
(venv) $ python provision.py
```

Run backend.

```
(venv) $ python run.py
```

### UI

Run UI

```
$ cd ui/
$ npm install
$ npm run dev
```
