import pieces_os_client as pos_client
import sublime
from typing import Optional,Dict,Union
import urllib
import json
import os

from . import __version__



class PiecesSettings:
	# Initialize class variables
	application = None
	models = None
	host = ""
	model_name = ""
	api_client = None
	_is_loaded = False # is the plugin loaded
	_color_scheme = None # default color scheme

	ONBOARDING_SYNTAX = "Packages/Pieces/syntax/Onboarding.sublime-syntax"
	ONBOARDING_COLOR_SCHEME = "User/Pieces/Pieces.hidden-color-scheme"
	PIECES_USER_DIRECTORY = os.path.join(sublime.packages_path(),"User","Pieces")
	
	# Create the pieces directory to store the data if it does not exists
	if not os.path.exists(PIECES_USER_DIRECTORY):
		os.makedirs(PIECES_USER_DIRECTORY)

	@property
	def is_loaded(self):
		sublime.set_timeout_async(self.get_health,0)
		return self._is_loaded



	@is_loaded.setter
	def is_loaded(self,is_loaded):
		self._is_loaded = is_loaded



	@classmethod
	def get_health(cls):
		"""
		Retrieves the health status from the WellKnownApi and returns True if the health is 'ok', otherwise returns False.

		Returns:
		bool: True if the health status is 'ok', False otherwise.
		"""
		try:
			health = pos_client.WellKnownApi(cls.api_client).get_well_known_health()
			health = health == "ok"
			cls._is_loaded = health
			return health
		except:
			return False


	@classmethod
	def host_init(cls):
		"""
		Initialize the host URL for the API connection.

		This method sets the host URL based on the configuration settings. If the host URL is not provided in the settings, it defaults to a specific URL based on the platform. 
		It then creates the WebSocket base URL and defines the WebSocket URLs for different API endpoints.
		"""
		cls.host = cls.pieces_settings.get('host')
		if not cls.host:
			if 'linux' == sublime.platform():
				cls.host = "http://localhost:5323"
			else:
				cls.host = "http://localhost:1000"

		ws_base_url = cls.host.replace('http','ws')

		cls.ASSETS_IDENTIFIERS_WS_URL = ws_base_url + "/assets/stream/identifiers"

		cls.AUTH_WS_URL = ws_base_url + "/user/stream"

		configuration = pos_client.Configuration(host=cls.host)

		cls.api_client = pos_client.ApiClient(configuration)




	@classmethod
	def models_init(cls):
		"""
		Initialize the model ID for the class using the specified settings.

		This method retrieves the available models, sets the model ID based on the settings provided,
		and defaults to a specific model ("GPT-3.5-turbo Chat Model") if the specified model is not found.
		"""

		models = cls.get_models_ids()
		cls.model_name = cls.pieces_settings.get("model")
		cls.model_id = models.get(cls.model_name,None)

		if not cls.model_id:
			cls.model_id = models["GPT-3.5-turbo Chat Model"]


	@classmethod
	def on_settings_change(cls):
		if cls.host != cls.pieces_settings.get('host'):
			cls.host_init()
		if cls.model_name != cls.pieces_settings.get("model"):
			cls.models_init()
		



	@classmethod
	def get_application(cls)-> pos_client.Application:
		if cls.application:
			return cls.application

		# Decide if it's Windows, Mac, Linux or Web
		api_instance = pos_client.ConnectorApi(cls.api_client)
		seeded_connector_connection = pos_client.SeededConnectorConnection(
			application=pos_client.SeededTrackedApplication(
				name = "SUBLIME",
				platform = sublime.platform().upper() if sublime.platform() != 'osx' else "MACOS",
				version = __version__))
		api_response = api_instance.connect(seeded_connector_connection=seeded_connector_connection)
		cls.application = api_response.application
		return cls.application

	@classmethod
	def get_models_ids(cls) -> Dict[str, str]:
		if cls.models:
			return models

		api_instance = pos_client.ModelsApi(cls.api_client)

		api_response = api_instance.models_snapshot()
		models = {model.name: model.id for model in api_response.iterable if model.cloud or model.downloaded} # getting the models that are available in the cloud or is downloaded


		return models


	@classmethod
	def create_auth_output_panel(cls):
		window = sublime.active_window()
		cls.output_panel = window.create_output_panel("Pieces Auth")
		cls.output_panel.settings().set("line_numbers", False)  # Disable line numbers
		cls.output_panel.settings().set("gutter", False)
		cls.output_panel.set_read_only(True)


		
	# Load the settings from 'Pieces.sublime-settings' file using Sublime Text API
	pieces_settings = sublime.load_settings('Pieces.sublime-settings')
	pieces_settings.add_on_change("PIECES_SETTINGS",on_settings_change)

