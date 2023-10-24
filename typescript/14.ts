function longestCommonPrefix(strs: string[]): string {
  let longest = strs[0];
  let len = longest.length;

  for (const curr of strs) {
    if (!curr.startsWith(longest)) {
      while (len !== 0) {
        longest = longest.substring(0, --len);
        if (curr.startsWith(longest)) break;
      }
    }
  }
  return longest;
}
