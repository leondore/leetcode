const romanToIntMap: { [key: string]: number } = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

function romanToInt(s: string): number {
  let result = 0;
  let idx = 0;

  while (idx < s.length) {
    if (
      idx < s.length - 1 &&
      romanToIntMap[s[idx]] < romanToIntMap[s[idx + 1]]
    ) {
      result += romanToIntMap[s[idx + 1]] - romanToIntMap[s[idx]];
      idx += 2;
      continue;
    }

    result += romanToIntMap[s[idx]];
    idx++;
  }

  return result;
}
