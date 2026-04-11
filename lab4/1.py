# 1
class Player:
    def __init__(self, player_id, player_name, player_hp):
        self._player_id = player_id
        self._player_name = player_name.strip().title()
        self._player_hp = player_hp if player_hp >= 0 else 0
    def __str__(self):
        return (f"Player(id={self._player_id}, name={self._player_name}, hp={self._player_hp})")
    def __del__(self):
        print(f"Player {self._player_name} deleted")
# p = Player(1, " john ", 120)
# print(p)

#2
def __str__(self):
    return f"Player(id={self._player_id}, name='{self._player_name}', hp={self._player_hp})"
def __del__(self):
    print(f"Player {self._player_name} deleted")
@classmethod
def from_string(cls, data: str):
    a = data.split(",")
    if len(a) != 3:
        raise  ValueError("Incorrect format")
    try:
        id = int(a[0].strip())
        name = a[1].strip()
        hp = int(a[2].strip())
        return cls(id, name, hp)
    except ValueError:
        raise ValueError("Error")
# p = Player.from_string("2, alice , 90")
# print(p)

#3
class Item:
    def __init__(self, id, name, power):
        self.id = id
        self.name = name.strip()
        self.power = power
    def __str__(self):
        return (f"Item(id={self.id}, name={self.name}, power={self.power})")
    def __eq__(self, other):
        if isinstance(other, Item):
            return self.id == other.id
        return False
    def __hash__(self):
        return hash(self.id)
# i = Item(1, " Sword ", 50)
# print(i)

#4
class Inventory:
    def __init__(self):
        self._items = []
    def add_item(self, item: Item):
        if item.id not in [i.id for i in self._items]:
            self._items.append(item)
    def remove_item(self, item_id: int):
        self._items = [i for i in self._items if i.id != item_id]
    def get_items(self):
        return self._items
    def unique_items(self):
        return set(self._items)
    def to_dict(self):
        return {item.id: item for item in self._items}

#5
    def get_strong_items(self, min_power: int):
        return [i for i in self._items if i.power >= min_power]

#6
from datetime import datetime
class Event:
    def __init__(self, type, data):
        self.type = type
        self.data = data
        self.timestamp = datetime.now()
    def __str__(self):
        return f"Event(type={self.type}, data={self.data}, timestamp={self.timestamp})"

#11
def damage_stream(events):
    for e in events:
        if e.type == "ATTACK":
            damage = e.data.get("damage", 0)
            yield damage
events = [
Event("ATTACK", {"damage": 20}),
Event("HEAL", {"heal": 10}),
Event("ATTACK", {"damage": 15})
]
# for dmg in damage_stream(events):
#     print(dmg)
# e = Event("ATTACK", {"damage": 20})
# print(e)

#7
class Player:
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
        self.inventory = []
    def handle_event(self, event: Event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self._hp -= damage
        elif event.type == "HEAL":
            heal = event.data.get("heal", 0)
            self._hp += heal
        elif event.type == "LOOT":
            item = event.data.get("item")
            if item:
                self.inventory.append(item)
    def __str__(self):
        return f"{self._name}: {self._hp}"
class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            damage = damage * 0.9
            self._hp -= damage
        else:
            super().handle_event(event)
class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power = int(item.power * 1.1)
                self.inventory.append(item)
        else:
            super().handle_event(event)

#8
class Logger:
    def log(self, event, player, filename):
        with open(filename, "a") as file:
            a = f"{event.timestamp};{player._name};{event.type};{event.data}\n"
            file.write(a)

#9
    def read_logs(self, filename):
        events = []
        with open(filename, "r") as r:
            for line in r:
                line = line.strip()
                parts = line.split(";")
                timestamp = parts[0]
                name = parts[1]
                type = parts[2]
                data = parts[3]
                data = eval(data)
                event = Event(type, data)
                event.timestamp = timestamp
                events.append(event)
        return events

#10
class EventIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.events):
            raise StopIteration
        event = self.events[self.index]
        self.index += 1
        return event

#12
def generate_events(players, items, n):
    import random
    all_events = []
    event_types = ["ATTACK", "LOOT", "HEAL"]
    choose = lambda: random.choice(event_types)
    for player in players:
        for _ in range(n):
            type_ = choose()
            if type_ == "ATTACK":
                data = {"damage": random.randint(5, 20)}
            elif type_ == "HEAL":
                data = {"heal": random.randint(5, 20)}
            elif type_ == "LOOT":
                item = random.choice(items)
                data = {"item": item}
            event = Event(type_, data)
            all_events.append(event)
    return all_events
# players = [Player("Alice", 100), Player("Bob", 100)]
# items = [Item(1, "Sword", 50), Item(2, "Shield", 30)]
# events = generate_events(players, items, 3)
#
# for e in events:
#     print(e)

#13
def analyze_logs(events):
    total_damage = sum(e.data.get("damage", 0) for e in events if e.type == "ATTACK")
    dmgpplayer = {}
    for e in events:
        if e.type == "ATTACK":
            player_name = e.data.get("player")
            dmgpplayer[player_name] = dmgpplayer.get(player_name, 0) + e.data.get("damage", 0)
    top_player = max(dmgpplayer, key=dmgpplayer.get) if dmgpplayer else None
    eventcount = {}
    for e in events:
        eventcount[e.type] = eventcount.get(e.type, 0) + 1
    most_common_event = max(eventcount, key=eventcount.get) if eventcount else None

    return {
        "total_damage": total_damage,
        "top_player": top_player,
        "most_common_event": most_common_event,
    }

#14
class Player:
    def __init__(self, id, name, hp):
        self._id = id
        self._name = name
        self._hp = hp
        self.inventory = Inventory()
def decide_action(player):
    if player._hp < 50:
        return "HEAL"
    elif not player.inventory.get_items():
        return "LOOT"
    else:
        return "ATTACK"
# player = Player(1, "Alice", 30)
# player.inventory = Inventory()
# action = decide_action(player)
# print(f"{player._name} decided to {action}")

#15
class Item:
    def __init__(self, id, name, power):
        self.id = id
        self.name = name.strip()
        self.power = power
    def add_item(self, item):
        if item.id not in [i.id for i in self.items]:
            self.items.append(item)
    def get_items(self):
        return self.items
class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0) * 0.9
            self._hp -= damage
        else:
            super().handle_event(event)
class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power = int(item.power * 1.1)
                self.inventory.add_item(item)
        else:
            super().handle_event(event)
# warrior = Warrior(1, "Thor", 100)
# mage = Mage(2, "Gandalf", 80)
#
# attack_event = Event("ATTACK", {"damage": 30})
# loot_event = Event("LOOT", {"item": Item(1, "Staff", 50)})
#
# warrior.handle_event(attack_event)
# mage.handle_event(loot_event)
#
# print(warrior._hp)         # 30% меньше урона
# print(mage.inventory.get_items()[0].power)  # усиленный предмет на 10%

#16
class Player:
    def __init__(self,name, hp):
        self._name = name.strip().title()
        self._hp = hp
        self._inventory = []
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
        else:
            self._hp = value
    def add_item(self, item):
        self._inventory.append(item)
    def remocve_item(self, item):
        if item in self._inventory:
            self._inventory.remove(item)
    @property
    def inventory(self):
        return list(self._inventory)
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self._hp -= damage
        elif event.type == "HEAL":
            heal = event.data.get("heal", 0)
            self._hp += heal
        elif event.type == "LOOT":
            item = event.data.get("item")
            if item:
                self.add_item(item)
# p = Player("Alice", 100)
# print(p.hp)
# p.hp -= 50
# print(p.hp)

#17
    def __del__(self):
        print(f"Player {self._name} has been destroyed")
# p = Player("Alice", 100)
# del p

#18
class Inventory:
    def __init__(self):
        self._items = []
    def add_item(self, item):
        if item.id not in [i.id for i in self._items]:
            self._items.append(item)
    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
    def get_items(self):
        return self._items
    def __iter__(self):
        return iter(self._items)
    def strong_items(self, min_power):
        return [item for item in self._items if item.power >= min_power]
# sword = Item(1, "Sword", 50)
# shield = Item(2, "Shield", 30)
# axe = Item(3, "Axe", 70)
# inv = Inventory()
# inv.add_item(sword)
# inv.add_item(shield)
# inv.add_item(axe)
# for i in inv:
#     print(i)
# strong = inv.strong_items(50)
# for i in strong:
#     print(i)

#19
    def analyze_inventory(inventories):
        all_items = []
        for inv in inventories:
            all_items.extend(inv.get_items())
        unique_items = set(all_items)
        top_power = max(all_items, key=lambda item: item.power)
        return {
            "unique_items": unique_items,
            "top_power": top_power
        }
# inv1 = Inventory()
# inv2 = Inventory()
# inv1.add_item(Item(1, "Sword", 50))
# inv1.add_item(Item(2, "Shield", 30))
# result = analyze_inventory([inv1, inv2])
# print(result["unique_items"])
# print(result["top_power"])

#20
def main():
    warrior = Warrior(1, "Warrior", 100)
    mage = Mage(2, "Mage", 100)
    players = [warrior, mage]
    items = [Item(1, "Sword", 50), Item(2, "Shield", 30), Item(3, "Axe", 40)]
    events = generate_events(players, items, 10)
    logger = Logger()
    logfile = "game_log.txt"
    for player, event in events:
        player.handle_event(event)
        logger.log(event, player, logfile)
    logs = logger.read_logs(logfile)
    top_damage, top_items = analyze_players(player)
    print("Players after event:")
    for p in players:
        print(p)
    print(f"\nTop Damage: {top_damage} ({top_damage.damage_done})")
    print(f"Max Items Player: {top_items.name} ({len(top_items.inventory.get_items())})")
    print(f"Event count: {len(events)}")
main()