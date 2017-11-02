Airflow-Webserver
--------------------------------------------------------------

NOTE: This is work-in-progress repository for the migration of [Airflow](https://github.com/apache/incubator-airflow)'s webserver from Flask-Admin to [Flask-AppBuilder (FAB)](https://github.com/dpgaspar/Flask-AppBuilder).

The goal of this Airflow Webserver fork is to leverage FAB's build-in security features to introduce the following capabilities in the UI:
- role-based access control
- dag-level permissions
- support for various authentications backends (OAuth, OpenID, Database, LDAP, etc.)

Airflow-Webserver is expected to be merged back into Airflow's source code in the near future once stabilized. The current version is not production-ready.

Contributions are welcome!

Setup
--------------------------------------------------------------

- To install Flask-AppBuilder

        `pip install flask-appbuilder`

- To create an admin account

        `fabmanager create-admin`

- To create your database object

        `fabmanager create-db`

- To start the webserver

        `fabmanager run`

Caveats
--------------------------------------------------------------

- I am actively contributing to Flask-Appbuilder to support backward-compatibility with existing Airflow features, and some of these features have not been rolled out to the latest release. So I recommend building Flask-AppBuilder from the [source code](https://github.com/dpgaspar/Flask-AppBuilder) for testing purposes.

What's Missing? (work-in-progress)
--------------------------------------------------------------
- Role/permission access for homepage
- Default roles/permissions configurations (currently only Admin/Public roles available)
- Miscellaneous features for all the model views (marked by the TODOs in the views.py file)
- DAG-level access control
