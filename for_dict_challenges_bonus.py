"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений. # done
2. Вывести айди пользователя, на сообщения которого больше всего отвечали. # done
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
import pprint as pp
import lorem

random.seed(42)
def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

# id пользователя, который написал больше всех сообщений
def max_messages(messages):
    user_messages = {message["sent_by"]: 0 for message in messages}
    for message in messages:
        user_messages[message["sent_by"]] += 1
    return max(user_messages, key=user_messages.get)

# id пользователя, на сообщения которого больше всего отвечали.
def max_reply(messages):
    reply_messages = {message["reply_for"]: 0 for message in messages}
    for message in messages:
        if message["reply_for"]:
            reply_messages[message["reply_for"]] += 1
    id = max(reply_messages, key=reply_messages.get)
    id_count = reply_messages[id]
    return id, id_count

# id пользователей, сообщения которых видело больше всего уникальных пользователей.
def max_seen(messages):
    seen_by = {message["id"]: [] for message in messages}
    for message in messages:
        seen_by[message["id"]].append(message["seen_by"])
    user_messages = {user: 0 for user in users_ids}
    for message in messages:
        if message["reply_for"]:
            user_messages[message["sent_by"]] += 1
    return max(user_messages, key=user_messages.get)




all_messages = generate_chat_history()
id_max_messages = max_messages(all_messages)
id_max_replies = max_reply(all_messages)
id_unique_max = max_seen(all_messages)
print(f'id пользователя, который написал больше всех сообщений: {id_max_messages}')
print(f'id пользователя, на сообщения которого больше всего отвечали: {id_max_replies[0]} (ответов: {id_max_replies[1]})')
print(f'id пользователей, сообщения которых видело больше всего уникальных пользователей: {id_unique_max}')

if __name__ == "__main__":
    pp.pprint(generate_chat_history()[-10])
