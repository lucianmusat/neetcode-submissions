class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.isEmpty()) {
            return 0;
        }
        int l = 0;
        int r = 0;
        int substring_length = 0;
        Set<Character> seen_chars = new HashSet<>();
        while (r < s.length()) {
            // While the next letter is not seen before, increase right
            if (!seen_chars.contains(s.charAt(r))) {
                seen_chars.add(s.charAt(r));
                r += 1;
                substring_length = Math.max(substring_length, seen_chars.size());
            } else {
                // Else remove from seen and increase left
                while (seen_chars.contains(s.charAt(r))) {
                    seen_chars.remove(s.charAt(l));
                    l += 1;
                }
            }            
        }
        return substring_length;
    }
}
