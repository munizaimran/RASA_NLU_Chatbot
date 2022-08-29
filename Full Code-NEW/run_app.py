from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/therapynlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-3767329369444-3764909650882-3762590812981-2da3708f334b36f45289fb517e458ac0', #app verification token
							'xoxb-3767329369444-3764983789650-qZxtEKaJimZpHcTXni9AV2fc', # bot verification token
							'X34DFjjpnPaS5dIa0EYSr99F', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5005, '/', input_channel))