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
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей. # done
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов). # done
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов). # done

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


# id пользователя, на сообщения которого больше всего отвечали
def max_reply(messages):
    # dict with message id as key and sender id as value
    replied_messages = {}
    for message in messages:
        replied_messages[message["id"]] = message["sent_by"]

    # dict with user id as key and count of replies as value
    user_reply = {}
    for message in messages:
        if message["reply_for"] and message["reply_for"] in replied_messages:
            replied_user = replied_messages[message["reply_for"]]
            user_reply[replied_user] = user_reply.get(replied_user, 0) + 1
    if user_reply:
        user_id = max(user_reply, key=user_reply.get)
        count_replies = user_reply[user_id]
        return user_id, count_replies
    else:
        return None


# id пользователей, сообщения которых видело больше всего уникальных пользователей.
def max_seen_users(messages):
    # dict with user id: count of unique users
    user_seen = {}
    for message in messages:
        sender_id = message["sent_by"]
        # set for value with unique users
        if sender_id not in user_seen:
            user_seen[sender_id] = set()
        user_seen[sender_id].update(message["seen_by"])
    

    max_user_viewers = max(len(viewers) for viewers in user_seen.values())
    users_ids = [user_id for user_id, viewers in user_seen.items() if len(viewers) == max_user_viewers]
    
    return users_ids

# Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
def highload_period(messages):
    day_part = {
        'утром': 0,
        'днём': 0,
        'вечером': 0
    }
    # count in datetime hours
    for message in messages:
        hour = message["sent_at"].hour
        day_part["утром"] += 1 if hour < 12 else 0
        day_part["днём"] += 1 if 12 <= hour < 18 else 0
        day_part["вечером"] += 1 if hour >= 18 else 0

    high_period = max(day_part, key=day_part.get)

    return high_period, day_part[high_period]


# Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).
def longest_thread(messages):
    # reply counts
    reply_counts = {}
    for message in messages:
        if message["reply_for"]:
            reply_counts[message["reply_for"]] = reply_counts.get(message["reply_for"], 0) + 1
    
    max_replies = max(reply_counts.values())

    message_ids = [msg_id for msg_id, count in reply_counts.items() if count == max_replies]

    return message_ids, max_replies

    

all_messages = generate_chat_history()
id_max_messages = max_messages(all_messages)
id_max_replies = max_reply(all_messages)
id_unique_max = max_seen_users(all_messages)
high_period, message_count = highload_period(all_messages)
mesage_thread, max_replies = longest_thread(all_messages)

print(f"id пользователя, который написал больше всех сообщений: {id_max_messages}")
print(f"id пользователя, на сообщения которого больше всего отвечали: {id_max_replies[0]} (ответов: {id_max_replies[1]})")
print(f"id пользователей, сообщения которых видело больше всего уникальных пользователей: {id_unique_max}")
print(f"Больше всего сообщений отправлено {high_period} (всего: {message_count})")
print(f"Сообщения с наибольшим количеством ответов: {mesage_thread} (всего: {max_replies})")



if __name__ == "__main__":
    pp.pprint(generate_chat_history()[-15])
