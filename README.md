Airflow-Webserver
--------------------------------------------------------------

NOTE: This is work-in-progress repository for the migration of [Airflow](https://github.com/apache/incubator-airflow)'s webserver from Flask-Admin to [Flask-AppBuilder (FAB)](https://github.com/dpgaspar/Flask-AppBuilder).

The goal of this Airflow Webserver fork is to leverage FAB's build-in security features to introduce the following capabilities in the UI:
- role-based access control
- dag-level permissions
- support for various authentications backends (OAuth, OpenID, Database, LDAP, etc.)

Airflow-Webserver will potentially be merged back into Airflow's source code in the near future.

Contributions are welcome!

Setup
--------------------------------------------------------------

Airflow-Webserver is written on top of Airflow 1.9.0, which is not currently in PyPI. Make sure you have airflow 1.9.0 or above installed before attempting the setup below.

- To install Flask-AppBuilder

        `pip install flask-appbuilder`

- To create an admin account

        `cd flask-appbuilder`
        `fabmanager create-admin`

- To set up the database object, modify the SQLALCHEMY_DATABASE_URI variable in config.py to your Airflow db.
  Note this will generate new tables which FAB uses for its security model.
  
        `fabmanager create-db`

- To start the webserver

        `fabmanager run`

Caveats
--------------------------------------------------------------

- I am actively contributing to Flask-Appbuilder to support backward-compatibility with existing Airflow features, and some of these features have not been rolled out to the latest release, including support for models with binary-type column and composite primary key. There are open PRs that are addressing these issues.

What's Missing? (work-in-progress)
--------------------------------------------------------------
- Default roles/permissions configurations is a demo of FAB's RBAC feature, which requires some fine-tuning
- Miscellaneous features for all the model views (marked by the TODOs in the views.py file)
- Testing/verification of integrations with various authentication backends
- FAB features including support for models with binary-type column (i.e. Variables) and composite primary key (i.e task instance)
- DAG-level access control
- Tests
