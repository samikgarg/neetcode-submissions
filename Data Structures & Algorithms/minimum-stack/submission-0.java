class MinStack {
    private class Node {
        int val;
        Node next;
        Node nextMin;

        public Node(int val, Node next) {
            this.val = val;
            this.next = next;
        }
    }

    private Node top = null;
    private Node min;
    
    
    public MinStack() {
        top = new Node(Integer.MAX_VALUE, null);
        min = top;
    }
    
    public void push(int val) {
        Node newNode = new Node(val, top);
        top = newNode;
        if (val <= min.val) {
            newNode.nextMin = min;
            min = newNode;
        }
    }
    
    public void pop() {
        if (top == min) {
            min = min.nextMin;
        }
        top = top.next;
    }
    
    public int top() {
        return top.val;
    }
    
    public int getMin() {
        return min.val;
    }
}
