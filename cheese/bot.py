from vk_api.bot_longpoll import VkBotMessageEvent, VkBotEventType
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
from database.cods import *


helpCmd = ["!!help", "помощь"]
helpText = "1.!!create - создать"
def main():
	vk_session = vk_api.VkApi(token='85716e2a114a7ffe63461dd0893218de9fb5e177c4bd6af4e58cb4b41425fa49090f344d61bd2cc940fda')
	vk = vk_session.get_api()
	longpoll = vk_api.bot_longpoll.VkBotLongPoll(vk_session, 178505691, wait=25)
	print(f"[*] БОТ ЗАПУЩЕН!")
	dbCods = DataBaseCods()
	def send(id, text):
		vk.messages.send(peer_id=id, random_id=0, message=text, dont_parse_links=1)

	for event in longpoll.listen():
		try:
			if event.type == VkBotEventType.MESSAGE_NEW:
				text = event.obj.text
				if text.lower() in helpCmd:
					send(event.obj.peer_id, helpText)
				elif text.lower()[:8] == "!!create":
					dbCods.create_code_db(text.lower()[9:])
					send(event.obj.peer_id, "создан")
		except:
			send(event.obj.peer_id, "Произошла ошибка...\nОшибка была отправлена админу.")
			send(491918167, f"Ошибка в диалоге @" + f"id{event.obj.peer_id}\n\n{traceback.format_exc()}")
main()