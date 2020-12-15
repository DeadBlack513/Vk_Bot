
#Это импорты
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config1 import main_token

#longpoll 
vk_session = vk_api.VkApi(token = main_token)
longpoll = VkLongPoll(vk_session)

#method
def sender (id, text):
    vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})
#Основной цикл sms
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
      if event.to_me:
        if event.from_chat:
            msg = event.text.lower()
            id = event.chat_id


#Отправки и Входящие
            if msg == 'мир аниме привет':
                sender(id,'Приветик))')
