class Solution {
    //O(length of s + length of t)
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sFreqMap = new HashMap<>();
        
        //O(length of s)
        for (int i = 0; i < s.length(); i++) {
            if (sFreqMap.containsKey(s.charAt(i))) {
                sFreqMap.put(s.charAt(i), sFreqMap.get(s.charAt(i)) + 1);
            } else {
                sFreqMap.put(s.charAt(i), 1);
            }
        }

        //O(length of t)
        for (int i = 0; i < t.length(); i++) {
            if (sFreqMap.containsKey(t.charAt(i)) && sFreqMap.get(t.charAt(i)) != 0) {
                sFreqMap.put(t.charAt(i), sFreqMap.get(t.charAt(i)) - 1);
            } else {
                return false;
            }
        }

        return s.length() == t.length();
    }
}
