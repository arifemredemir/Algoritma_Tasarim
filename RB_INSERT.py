class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = "RED"


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = "BLACK"
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL

    def sola_dondur(self, x):

        print(f"   → SOLA-DÖNDÜR({x.key}) yapılıyor...")
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def saga_dondur(self, x):
        print(f"   → SAĞA-DÖNDÜR({x.key}) yapılıyor...")
        y = x.left
        x.left = y.right

        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def tree_insert(self, z):
        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = self.NIL
        z.right = self.NIL

    def rb_insert_fixup(self, x):
        step = 1
        while x != self.root and x.parent.color == "RED":
            print(f"\n   Adım {step}: x={x.key}(KIRMIZI), parent={x.parent.key}(KIRMIZI) - İhlal var!")

            if x.parent == x.parent.parent.left:
                y = x.parent.parent.right  # Amca düğüm

                if y.color == "RED":  # Durum 1
                    print(f"   → DURUM 1: Amca {y.key} KIRMIZI")
                    print(f"   → Renk değişimi: parent={x.parent.key}, amca={y.key} → SİYAH")
                    print(f"   → Renk değişimi: grandparent={x.parent.parent.key} → KIRMIZI")
                    x.parent.color = "BLACK"
                    y.color = "BLACK"
                    x.parent.parent.color = "RED"
                    x = x.parent.parent
                else:
                    if x == x.parent.right:  # Durum 2
                        print(f"   → DURUM 2: x sağ çocuk")
                        x = x.parent
                        self.sola_dondur(x)

                    # Durum 3
                    print(f"   → DURUM 3: Renk değişimi ve sağa döndür")
                    print(f"   → {x.parent.key} → SİYAH, {x.parent.parent.key} → KIRMIZI")
                    x.parent.color = "BLACK"
                    x.parent.parent.color = "RED"
                    self.saga_dondur(x.parent.parent)
            else:
                y = x.parent.parent.left  # Amca düğüm

                if y.color == "RED":  # Durum 1 (simetrik)
                    print(f"   → DURUM 1 (simetrik): Amca {y.key} KIRMIZI")
                    print(f"   → Renk değişimi: parent={x.parent.key}, amca={y.key} → SİYAH")
                    print(f"   → Renk değişimi: grandparent={x.parent.parent.key} → KIRMIZI")
                    x.parent.color = "BLACK"
                    y.color = "BLACK"
                    x.parent.parent.color = "RED"
                    x = x.parent.parent
                else:
                    if x == x.parent.left:  # Durum 2 (simetrik)
                        print(f"   → DURUM 2 (simetrik): x sol çocuk")
                        x = x.parent
                        self.saga_dondur(x)

                    # Durum 3 (simetrik)
                    print(f"   → DURUM 3 (simetrik): Renk değişimi ve sola döndür")
                    print(f"   → {x.parent.key} → SİYAH, {x.parent.parent.key} → KIRMIZI")
                    x.parent.color = "BLACK"
                    x.parent.parent.color = "RED"
                    self.sola_dondur(x.parent.parent)

            step += 1

        print(f"\n   → Kök {self.root.key} → SİYAH (kural gereği)")
        self.root.color = "BLACK"

    def rb_insert(self, key):
        """RB-INSERT - Red-Black Tree insert işlemi"""
        x = Node(key)

        # Düğümü ağaca ekle
        self.tree_insert(x)
        x.color = "RED"

        parent_str = f"parent={x.parent.key}" if x.parent else "parent=None"
        print(f"\n1. {key} KIRMIZI olarak eklendi ({parent_str})")

        # Red-Black özelliklerini koru
        print(f"\n2. İhlal kontrolü başlıyor...")
        self.rb_insert_fixup(x)

    def print_tree_structure(self, node=None, prefix="", is_tail=True, level=0):
        """Ağacı ağaç yapısında görselleştir"""
        if node is None:
            node = self.root

        if node == self.NIL:
            return

        color = "🔴" if node.color == "RED" else "⚫"
        print(prefix + ("└── " if is_tail else "├── ") + f"{color} {node.key}")

        children = []
        if node.left != self.NIL:
            children.append(("left", node.left))
        if node.right != self.NIL:
            children.append(("right", node.right))

        for i, (side, child) in enumerate(children):
            is_last = (i == len(children) - 1)
            extension = "    " if is_tail else "│   "
            self.print_tree_structure(child, prefix + extension, is_last, level + 1)


# Örnek ağacı oluştur
print("=" * 60)
print("MEVCUT AĞAÇ OLUŞTURULUYOR")
print("=" * 60)

rbt = RedBlackTree()

# Mevcut ağacı manuel olarak oluştur
nodes = {}
for key in [7, 3, 18, 10, 22, 8, 11, 26]:
    nodes[key] = Node(key)
    nodes[key].left = rbt.NIL
    nodes[key].right = rbt.NIL

# Ağaç yapısını kur
rbt.root = nodes[7]
rbt.root.color = "BLACK"

nodes[7].left = nodes[3]
nodes[7].right = nodes[18]

nodes[3].parent = nodes[7]
nodes[3].color = "BLACK"

nodes[18].parent = nodes[7]
nodes[18].color = "RED"
nodes[18].left = nodes[10]
nodes[18].right = nodes[22]

nodes[10].parent = nodes[18]
nodes[10].color = "BLACK"
nodes[10].left = nodes[8]
nodes[10].right = nodes[11]

nodes[22].parent = nodes[18]
nodes[22].color = "BLACK"
nodes[22].right = nodes[26]

nodes[8].parent = nodes[10]
nodes[8].color = "RED"

nodes[11].parent = nodes[10]
nodes[11].color = "RED"

nodes[26].parent = nodes[22]
nodes[26].color = "RED"

print("\nBAŞLANGIÇ DURUMU:")
print("-" * 60)
rbt.print_tree_structure()

print("\n" + "=" * 60)
print("15 EKLENMEYE BAŞLIYOR")
print("=" * 60)

input_value = int(input("Eklenecek Sayıyı Girin: "))

rbt.rb_insert(input_value)

print("\n" + "=" * 60)
print("SON DURUM")
print("=" * 60)
rbt.print_tree_structure()