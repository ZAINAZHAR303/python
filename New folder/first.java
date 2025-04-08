public static void findPerfectSquareWith2025(int N) {
    long lower = (long) Math.pow(10, N - 1);
    long upper = (long) Math.pow(10, N) - 1;

    long start = (long) Math.ceil(Math.sqrt(lower));
    long end = (long) Math.floor(Math.sqrt(upper));

    for (long i = start; i <= end; i++) {
        long square = i * i;
        String squareStr = Long.toString(square);
        if (squareStr.contains("2025") && squareStr.length() == N) {
            return square;