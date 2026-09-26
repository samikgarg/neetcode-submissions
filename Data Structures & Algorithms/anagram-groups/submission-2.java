class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> angrmMap = new HashMap<>();

        for (String s : strs) {
            int[] count = new int[26];
            for (int i = 0; i < s.length(); i++) {
                char currChar = s.charAt(i);
                count[(int) currChar - (int) 'a']++;
            }
            String key = "";
            for (int i : count) {
                key += ("," + String.valueOf(i));
            }

            if (angrmMap.containsKey(key)) {
                List<String> currList = angrmMap.get(key);
                currList.add(s);
                angrmMap.put(key, currList);
            } else {
                ArrayList<String> currList = new ArrayList<>();
                currList.add(s);
                angrmMap.put(key, currList);
            }
        }

        ArrayList<List<String>> answer = new ArrayList<>();
        for (String key : angrmMap.keySet()) {
            answer.add(angrmMap.get(key));
        }
        return answer;
    }
}
