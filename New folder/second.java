import java.util.*;
import java.io.*;

public class second {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine()); // Number of test cases
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine()); // Number of sticks
            String[] input = br.readLine().split(" ");
            int[] sticks = new int[N];
            for (int i = 0; i < N; i++) {
                sticks[i] = Integer.parseInt(input[i]);
            }

            // Count the frequency of each stick length
            Map<Integer, Integer> freq = new HashMap<>();
            for (int stick : sticks) {
                freq.put(stick, freq.getOrDefault(stick, 0) + 1);
            }

            // Find the two most frequent lengths
            int max1 = 0, max2 = 0;
            for (int count : freq.values()) {
                if (count > max1) {
                    max2 = max1;
                    max1 = count;
                } else if (count > max2) {
                    max2 = count;
                }
            }

            // Calculate the number of operations needed
            int needed = Math.max(0, 4 - max1 - max2);
            sb.append(needed).append("\n");
        }

        System.out.print(sb.toString());
    }
}
