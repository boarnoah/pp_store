# pp_store
Customer storefront for Pannucis Pizza


### Notes
a) to setup on a bare system

1. Install python 3.6
2. Install python pip
3. Install pipenv from pip
4. Install dependencies via pipenv

        pipenv install



note: in production we export from pipenv to requirements.txt, since aws ecs can handle those.

    pipenv -r > requirements.txt


b) rn we have to bootstrap (create the tables + enter in schema) the db manually. to do so:

Opens python shell with all the dependencies:

    pipenv run python 
    from app import db
    db.create_all()


c) If you wanna connect to the db directly


    mysql -h ppdbmysql.ct4sai8mxgm9.us-east-2.rds.amazonaws.com -D ppdb

