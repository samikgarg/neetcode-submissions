class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> angrms = new HashMap<>();
        for (String s: strs) {
            boolean found = false;
            for (String key: angrms.keySet()) {
                if (isAnagram(key, s)) {
                    List<String> currList = angrms.get(key);
                    currList.add(s);
                    angrms.put(key, currList);
                    found = true;
                }
            }

            if (!found) {
                ArrayList<String> newList = new ArrayList<>();
                newList.add(s);
                angrms.put(s, newList);
            }
        }

        ArrayList<List<String>> answer = new ArrayList<>();
        for (String s : angrms.keySet()) {
            answer.add(angrms.get(s));
        }
        return answer;
    }


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
