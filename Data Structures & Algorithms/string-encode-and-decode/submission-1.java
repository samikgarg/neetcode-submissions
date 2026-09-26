class Solution {

    public String encode(List<String> strs) {
        String encoded = "";
        for (String str : strs) {
            encoded += String.valueOf(str.length()) + "#" + str;
        }
        return encoded;
    }

    public List<String> decode(String str) {
        ArrayList<String> answer = new ArrayList<>();

        String rest = str;
        while (rest.length() > 0) {
            String length = "";
            boolean end = false;
            for (int i = 0; i < rest.length(); i++) {
                char currChar = rest.charAt(i);
                if (currChar == '#') {
                    break;
                }
                length = length + currChar;
            }
            int endIndex = Integer.parseInt(length) + length.length() + 1;
            answer.add(rest.substring(length.length() + 1, endIndex));
            rest = rest.substring(endIndex);
        }

        return answer;
    }
}
