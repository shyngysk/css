from datetime import datetime
import random

class Item:
    def __init__(self, id, name, power):
        self.id = id
        self.name = name.strip()
        self.power = power
    def __eq__(self, other):
        return isinstance(other, Item) and self.id == other.id
    def __hash__(self):
        return hash(self.id)
    def __str__(self):
        return f"Item(id={self.id}, name={self.name}, power={self.power})"

class Event:
    def __init__(self, type, data):
        self.type = type
        self.data = data
        self.timestamp = datetime.now()
    def __str__(self):
        return f"Event(type={self.type}, data={self.data}, timestamp={self.timestamp})"

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
        return list(self._items)
    def __iter__(self):
        return iter(self._items)
    def strong_items(self, min_power):
        return [item for item in self._items if item.power >= min_power]

class Player:
    def __init__(self, id, name, hp):
        self._id = id
        self._name = name.strip().title()
        self._hp = hp
        self._inventory = Inventory()
        self._damage_done = 0
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)
    @property
    def name(self):
        return self._name
    @property
    def damage_done(self):
        return self._damage_done
    @property
    def inventory(self):
        return self._inventory
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self.hp -= damage
            self._damage_done += damage
        elif event.type == "HEAL":
            heal = event.data.get("heal", 0)
            self.hp += heal
        elif event.type == "LOOT":
            item = event.data.get("item")
            if item:
                self._inventory.add_item(item)
    def __del__(self):
        print(f"Player {self.name} successfully deleted")
    def __str__(self):
        return f"{self.name}: hp={self.hp}, items={len(self._inventory.get_items())}"

class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0) * 0.9
            self.hp -= damage
            self._damage_done += damage
        else:
            super().handle_event(event)

class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power = int(item.power * 1.1)
                self._inventory.add_item(item)
        else:
            super().handle_event(event)

class Logger:
    def log(self, event, player, filename):
        with open(filename, "a") as file:
            file.write(f"{event.timestamp};{player.name};{event.type};{event.data}\n")
    def read_logs(self, filename):
        events = []
        with open(filename, "r") as f:
            for line in f:
                timestamp, name, type_, data = line.strip().split(";", 3)
                event = Event(type_, eval(data))
                event.timestamp = datetime.fromisoformat(timestamp)
                event.player_name = name
                events.append(event)
        return events

def generate_events(players, items, n):
    events = []
    types = ["ATTACK", "HEAL", "LOOT"]
    for player in players:
        for _ in range(n):
            type_ = random.choice(types)
            if type_ == "ATTACK":
                data = {"damage": random.randint(5, 20)}
            elif type_ == "HEAL":
                data = {"heal": random.randint(5, 20)}
            elif type_ == "LOOT":
                data = {"item": random.choice(items)}
            events.append((player, Event(type_, data)))
    return events

def analyze_players(players):
    top_damage = max(players, key=lambda x: x.damage_done)
    top_items = max(players, key=lambda x: len(x.inventory.get_items()))
    return top_damage, top_items

def main():
    warrior = Warrior(1, "warrior", 100)
    mage = Mage(1, "mage", 90)
    players = [warrior, mage]
    items = [Item(1, "sword", 50), Item(2, "shield", 30), Item(3, "axe", 40)]
    events = generate_events(players, items, 5)
    logger = Logger()
    logfile = "game_log.txt"
    for player, event in events:
        player.handle_event(event)
        logger.log(event, player, logfile)
    logs = logger.read_logs(logfile)
    top_damage, top_items = analyze_players(players)
    print("Players after event:")
    for i in players:
        print(i)
    print(f"\nTop damage: {top_damage.name} ({top_damage.damage_done})")
    print(f"Player with most items: {top_items.name} ({len(top_items.inventory.get_items())})")
    print(f"Total events: {len(events)}")
main()