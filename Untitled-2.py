def q01():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = 0
    for n in my_list:
        if (n % 2) == 0 and not n == 4:
            result += n
    return result

def q02():
    full_name = 'Ms. Kamisato Ayaka'
    text = full_name.split()
    print('Title:', text[0])
    print('First name:', text[1])
    print('Last name:', text[2])
    return 0

def q03():
    sentence = 'I feel like running'
    count = 0
    for c in sentence:
        if c.lower() in 'bcdfghjklmnpqrstvwxyz':
            count += 1
    return count

def q04(n):
    if n == 1:
        return str(1)
    else:
        return str(n) + ' ' + q04(n - 1)

class Weapon:
    def __init__(self, weapon_name, type):
        self.name = weapon_name
        self.type = type
        self.level = 1

class NodeWeapon:
    def __init(self, value=None):
        self.value = value
        self.next = None

class LinkedListWeapon:
    def __init__(self):
        self.first_node = None
        self.size = 0

    def append(self, node):
        if self.first_node is None:
            self.first_node = node
        else:
            current_node = self.first_node
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.size += 1

    def list(self):
        result = ''
        if self.first_node is None:
            result = 'Empty Weapon Lists'
        else:
            current_node = self.first_node
            while current_node.next is not None:
                result += current_node.value.name + ', '
                current_node = current_node.next
            result += current_node.value.name
        return result

def q06():
    skyward_harp = Weapon('Skyward Harp', 'Bow')
    mistsplitter_reforged = Weapon('Mist-Splitter Reforged', 'Sword')

    my_linkedlist = LinkedListWeapon()
    node_weapon01 = NodeWeapon(skyward_harp)
    node_weapon02 = NodeWeapon(mistsplitter_reforged)

    my_linkedlist.append(node_weapon01)
    my_linkedlist.append(node_weapon02)

    print(my_linkedlist.list())
    return 0

def q07(nation):
    mydict = {
        "Mondstadt": "From amongst mountains and wide-open plains, carefree breezes carry the scent of dandelions - a gift from the Anemo God, Barbatos.",
        "Liyue": "Mountains stand tall and proud alongside the stone forest, that, together with the open plains and lively rivers.",
        "Inazuma": "On winding shores and towering cliffs, and in forests and mountains full of secrets, witness the Eternity pursued by Her Excellency, the Almighty Narukami Ogosho."
    }
    return mydict.get(nation, "Nation not found")

if __name__ == "__main__":
    print("q01 result:", q01())
    print("q03 result:", q03())
    print("q04 result:", q04(5))
    print("q07 result (Mondstadt):", q07("Mondstadt"))