class Solution {
    public int[] topKFrequent(int[] nums, int k) {
       PriorityQueue<Element> pq = new PriorityQueue<>();
       Map<Integer, Element> freqMap = new HashMap<>();
       int[] result = new int[k];

       for (int num : nums) {
            if (freqMap.containsKey(num)) {
                freqMap.get(num).frequency++;
            } else {
                Element e = new Element(num);
                freqMap.put(num, e);
            }
       }

       for (Element e : freqMap.values()) {
            pq.offer(e);
            if (pq.size() > k) {
                pq.poll();
            }
       }

       int i = 0;
       while (!pq.isEmpty()) {
            result[i] = pq.poll().value;
            i++;
       }

       return result;
    }

    private class Element implements Comparable<Element>{
        int value;
        int frequency;

        public Element(int value) {
            this.value = value;
            this.frequency = 1;
        }
        
        @Override
        public int compareTo(Element other) {
            return this.frequency - other.frequency;
        }
    }
}
