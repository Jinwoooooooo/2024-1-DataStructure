"""
이중 연결 리스트 (Doubly Linked List)
"""
#====================================================================
class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None  # 앞에 연결된 노드 링크
        self.next = None  # 뒤에 연결될 노드 링크

    def __str__(self):  # print 문 등에서 반영할 출력 문자열 반환값 정의
        return f"[{self.data}]"
#====================================================================
class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    #----------------------------------------------------------------
    def __str__(self):
        lst = []
        current = self.head
        while current is not None:
            lst.append(current.data)
            current = current.next
        return str(lst)

    #----------------------------------------------------------------
    # 이중연결리스트의 맨 앞에 새 노드를 추가하면서 저장할 값을 전달한다.
    def insertFront(self, value):
        # 새 노드를 생성하고, 생성된 노드에 value를 저장한다.
        newNode = Node(value)
        # 새 노드가 추가되는 상황을 구분한다. (빈 리스트에 처음 추가하는 경우와, 기존 리스트에 추가하는 경우)
        if self.head is None:   # 빈 리스트이면
            self.head = newNode
            self.tail = newNode
        else: #리스트에 노드가 1개 이상 있는 경우
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        self.count += 1
    #----------------------------------------------------------------
    # 리스트의 맨 뒤에 value값을 가진 새 노드를 연결한다.
    def append(self, value):
        # 새 노드를 생성하고, 생성된 노드에 value를 저장한다.
        newNode = Node(value)
        # 새 노드가 추가되는 상황을 구분한다. (빈 리스트에 처음 추가하는 경우와, 기존 리스트에 추가하는 경우)
        if self.head is None:   # 빈 리스트이면
            self.head = newNode
            self.tail = newNode
        else: #리스트에 노드가 1개 이상 있는 경우
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

        self.count += 1

    #----------------------------------------------------------------
    # value 값을 가진 노드를 찾아서 노드를 반환한다. 없으면 None 반환.
    def find(self, value):
        current = self.head #헤드 노드부터 탐색 시작
        while current is not None:
            if current.data == value:
                return current
            else:
                current = current.next
        return None
    #----------------------------------------------------------------
    # 리스트에서 targetNode 앞에 새 노드(value)를 추가한다.
    def insertBefore(self, targetNode, value):
        # targetNode가 None인 경우는 그냥 리턴한다.
        if targetNode is None:
            return

        # Case 1. targetNode가 리스트의 head인경우 (맨 앞의 노드인 경우)

        if targetNode is self.head:
            self.insertFront(value)  # self.count += 1 은 insertFront()에 이미 포함됨.
        else:
            # 먼저 새 노드를 생성
            newNode = Node(value)
            # 리스트 완성하기  (Slido: 1291590)
            newNode.next = targetNode
            newNode.prev = targetNode.prev
            targetNode.prev.next = newNode
            targetNode.prev = newNode
            self.count += 1

    #----------------------------------------------------------------
    # 리스트의 targetNode 뒤에 새 노드(value)를 연결한다.
    def insertAfter(self, targetNode, value):
        if targetNode is self.tail:
            self.append(value)
        else:
            newNode = Node(value)
            newNode.next = targetNode.next
            newNode.prev = targetNode
            targetNode.next.prev = newNode
            targetNode.next = newNode
            self.count += 1

    #----------------------------------------------------------------
    # 오름 차순 정렬 상태를 유지하는 새노드(value)의 위치를 찾아서 추가한다.
    # 현재의 리스트는 노드들이 정렬되어 있는 것으로 가정한다. (빈 리스트도 포함)
    def insertSorted(self, value):
        # 1. 빈 리스트인 경우 처리
        if self.count == 0:
            self.append(value)
            return
        # 2. 노드가 하나 이상 있는 경우
        # value보다 크거나 같은 값을 가진 노드를 찾아서 그 노드 앞에 새 노드(value)를 추가한다.
        current = self.head
        while current is not None:
            if current.data >= value:  # insert 할 노드를 찾음. (current 앞에 새 노드 추가)
                self.insertBefore(current, value)
                return
            current = current.next

        # 3. value보다 크거나 같은 노드가 없는 경우에는 리스트의 맨 뒤에 새 노드를 추가한다.
        self.append(value)

   #----------------------------------------------------------------
   # 리스트에서 지정된 targetNode를 제거한다. 
   # del targetNode (노드 최종 삭제) -> 마지막 단계에서 실행.
    def remove(self, targetNode):
        if targetNode is None:
            return
        if self.count == 1:     # 리스트에 노드가 1개만 있는 경우
            self.head = None
            self.tail = None
        elif targetNode is self.head:   # 헤더 노드를 삭제하는 경우
            self.head = targetNode.next
            targetNode.next.prev = None
        elif targetNode is self.tail:   # 꼬리 노드를 삭제하는 경우
            self.tail = targetNode.prev
            targetNode.prev.next = None
        else:
            targetNode.prev.next = targetNode.next
            targetNode.next.prev = targetNode.prev

        del targetNode  # 노드 삭제
        self.count -= 1


   #----------------------------------------------------------------
   # 리스트가 비어 있으면 True, 아니면 False를 반환
    def isEmpty(self):
        return self.count == 0

   #----------------------------------------------------------------
    # 리스트의 현재 연결 상태를 출력한다. (head ===> tail)
    def showList(self):
        print("[Head]=", end="")
        현재노드 = self.head

        while 현재노드 != None:
            print("{}=".format(현재노드), end="")
            현재노드 = 현재노드.next    #다음 연결된 노드로 이동.
        
        print("[Total {} Nodes]".format(self.count))












