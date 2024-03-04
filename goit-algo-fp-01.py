class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Додавання нового вузла в кінець списку
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування списку методом вставок
    def insertion_sort(self):
        if not self.head or not self.head.next:
            return self.head

        new_head = None
        current = self.head
        while current:
            next_node = current.next
            new_head = self.sorted_insert(new_head, current)
            current = next_node
        self.head = new_head

    # Вставка відсортованого вузла у відсортований список
    def sorted_insert(self, head, new_node):
        if not head or head.data >= new_node.data:
            new_node.next = head
            return new_node

        current = head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head

    # Відображення списку
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список
    def merge_sorted_lists(list1, list2):
        merged_list = SinglyLinkedList()  # Створюємо новий пустий список
        current1, current2 = list1.head, list2.head  # Встановлюємо вказівники на голови списків

        # Доки обидва списки не пусті
        while current1 and current2:
            # Якщо дані в поточному вузлі списку list1 менші, додаємо його в об'єднаний список
            if current1.data < current2.data:
                merged_list.append(current1.data)
                current1 = current1.next
            # Якщо дані в поточному вузлі списку list2 менші, додаємо його в об'єднаний список
            else:
                merged_list.append(current2.data)
                current2 = current2.next

        # Додаємо залишені елементи з list1, якщо вони є
        while current1:
            merged_list.append(current1.data)
            current1 = current1.next

        # Додаємо залишені елементи з list2, якщо вони є
        while current2:
            merged_list.append(current2.data)
            current2 = current2.next

        # Сортуємо об'єднаний список
        merged_list.insertion_sort()

        return merged_list

if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list2 = SinglyLinkedList()

    # Додавання даних у вхідні списки
    for value in [1, 3, 5]:
        list1.append(value)

    for value in [2, 4, 6]:
        list2.append(value)

    print("Початковий список 1:")
    list1.display()

    list1.reverse()
    print("Реверсований список:")
    list1.display()

    list1.insertion_sort()

    print("Відсортований список методом вставок:")
    list1.display()

    merged_list = SinglyLinkedList.merge_sorted_lists(list1, list2)
    print("Об'єднаний відсортований список:")
    merged_list.display()
