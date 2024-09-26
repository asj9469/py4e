// https://leetcode.com/problems/sum-of-two-integers/

class Solution {
    public int getSum(int a, int b) {
        int carry = 0;
        int output = 0;

        for (int i = 0; i < 32; i++){
            int bitA = ((a & (0x1 << i)) != 0) ? 1 : 0; // get the value at bit i
            int bitB = ((b & (0x1 << i)) != 0) ? 1 : 0; // get the value at bit i

            int tempOut = bitA ^ bitB ^ carry;
            output = output | (tempOut << i);
            carry = ((bitA & bitB) | ((bitA ^ bitB) & carry));
        }
        return output;
    }
}