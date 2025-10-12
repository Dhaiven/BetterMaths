package org.bettermaths.token.symbol.delimiter;

import java.util.HashMap;
import java.util.Map;

public class DelimitersManager {

    private static boolean isInitialized = false;

    private static final Map<String, Delimiter> separators = new HashMap<>();

    public static void init() {
        if (isInitialized) {
            throw new RuntimeException("Symbols already initialized");
        }
        isInitialized = true;

        add(new Parentheses());
    }

    public static Map<String, Delimiter> all() {
        if (!isInitialized) {
            init();
        }

        return separators;
    }

    public static Delimiter get(String symbol) {
        if (!isInitialized) {
            init();
        }

        return separators.get(symbol);
    }

    public static void add(Delimiter delimiter) {
        separators.put(delimiter.getStart() + ":" + delimiter.getEnd(), delimiter);
    }

    public static void remove(String key) {
        separators.remove(key);
    }

    public static void remove(String start, String end) {
        remove(start + ":" + end);
    }
}

