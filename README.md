
[![Build Status](https://travis-ci.org/Ngareski/Ireport2.svg?branch=develop)](https://travis-ci.org/Ngareski/Ireport2) [![codecov](https://codecov.io/gh/Ngareski/Ireport2/branch/develop/graph/badge.svg)](https://codecov.io/gh/Ngareski/Ireport2)
# Ireport2
Corruption is a huge bane to Africa’s development. African countries must develop novel and
localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables
any/every citizen to bring any form of corruption to the notice of appropriate authorities and the
general public. Users can also report on things that needs government intervention

## Getting Started
git clone the project onto local machine using this link
https://github.com/Ngareski/Ireport2



### Installing

Install the virtual environmnet using this command
```
virtualenv env
```

And repeat

```
source env/bin/activate
```
### Prerequisites
Install the project dependecies using the folowing commands

```
pip install requirements.txt
```

### Running project
Run this command to export the flask app
```
export FLASK_APP=run.py
```
Then use this command to run the app
```
flask run
```
Endpoints

|              | HTTP           | URL path      | Description       
| ----------- | --------------- | --------- | ----------- |
| Action    | Verb      |      |       | |
| Create    | POST       |/api/v1/red-flags     | create a red-flag incident |
| Read  | GET           | /api/v1/red-flags   | View all existing red-flags |
| Update  | PATCH           | /api/v1/red-flags/<redflag_id>/comment   |Edit red-flag comment|
| Update  | PATCH           | /api/v1/red-flags/<redflag_id>/location   | Edit red-flags comment |
| Delete  | DELETE           | /api/v1/red-flags/<redflag_id>  | Delete an existing red-flag |
