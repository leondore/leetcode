function isPalindromeNumber(x: number): boolean {
  if (x < 0) return false;

  let reversed = 0;
  let num = x;
  const BASE = 10;

  while (num > 0) {
    const digit = num % BASE;
    reversed = reversed * BASE + digit;
    num = Math.floor(num / BASE);
  }

  return x === reversed;
}

function reverseString(str: string): string {
  if (str.length < 2) {
    return str;
  }
  return reverseString(str.slice(1)) + str[0];
}

function isPalindromeString(x: number): boolean {
  const numStr = x.toString();
  return numStr === reverseString(numStr);
}
