class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class LinkedList {
  head: ListNode | null;
  tail: ListNode | null;

  constructor() {
    this.head = null;
    this.tail = null;
  }

  addToHead(val: number) {
    const node = new ListNode(val);

    if (this.head === null) {
      this.head = node;
      this.tail = node;
      return;
    }

    node.next = this.head;
    this.head = node;
  }

  addToTail(val: number) {
    const node = new ListNode(val);

    if (this.tail === null) {
      this.head = node;
      this.tail = node;
      return;
    }

    this.tail.next = node;
    this.tail = node;
  }
}

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  const merged: LinkedList = new LinkedList();

  while (list1 !== null || list2 !== null) {
    if (list1 === null) {
      merged.addToTail(list2.val);
      list2 = list2.next;
      continue;
    }
    if (list2 === null) {
      merged.addToTail(list1.val);
      list1 = list1.next;
      continue;
    }

    if (list1.val <= list2.val) {
      merged.addToTail(list1.val);
      list1 = list1.next;
    } else {
      merged.addToTail(list2.val);
      list2 = list2.next;
    }
  }

  return merged.head;
}
