import logging
import six
from flask import Flask, redirect
from flask_appbuilder import SQLA, AppBuilder, IndexView, expose
from flask_wtf.csrf import CSRFProtect


"""
 Logging configuration
"""
# TODO: streamline logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')

csrf = CSRFProtect()
csrf.init_app(app)

db = SQLA(app)


"""
 Set up blueprints
"""
from airflow import api
api.load_auth()
from app.api.experimental import endpoints as e
# required for testing purposes otherwise the module retains
# a link to the default_auth
if app.config['TESTING']:
    if six.PY2:
        reload(e)
    else:
        import importlib
        importlib.reload(e)
app.register_blueprint(e.api_experimental, url_prefix='/api/experimental')


"""
 Set up index page
"""
class AirflowIndexView(IndexView):
	@expose("/")
	def index(self):
		return redirect('/home')


"""
 Initialize appbuilder
"""
appbuilder = AppBuilder(
    app,
    db.session,
    base_template='appbuilder/baselayout.html',
    indexview=AirflowIndexView
)


"""
 Initialize views
"""
from app import views
appbuilder.add_view_no_menu(views.HomeView())
appbuilder.add_view_no_menu(views.Airflow())
appbuilder.add_view_no_menu(views.DagModelView())
appbuilder.add_view_no_menu(views.ConfigurationView())
appbuilder.add_view_no_menu(views.VersionView())

appbuilder.add_view(views.DagRunModelView, "DAG Runs", category="Browse", category_icon="fa-globe")
appbuilder.add_view(views.JobModelView, "Jobs", category="Browse")
appbuilder.add_view(views.LogModelView, "Logs", category="Browse")
appbuilder.add_view(views.SlaMissModelView, "SLA Misses", category="Browse")
appbuilder.add_view(views.TaskInstanceModelView, "Task Instances", category="Browse")


appbuilder.add_link("Configurations", href='/configuration', category="Admin", category_icon="fa-user")
appbuilder.add_view(views.ConnectionModelView, "Connections", category="Admin")
appbuilder.add_view(views.PoolModelView, "Pools", category="Admin")
appbuilder.add_view(views.VariableModelView, "Variables", category="Admin")
appbuilder.add_view(views.XComModelView, "XComs", category="Admin")

appbuilder.add_link("Documentation", href='http://pythonhosted.org/airflow/', category="Docs", category_icon="fa-cube")
appbuilder.add_link("Github", href='https://github.com/apache/incubator-airflow', category="Docs")

appbuilder.add_link('Version', href='/version', category='About', category_icon='fa-th')


"""
 Initialize Role-Based Access Control
"""
from app import security
