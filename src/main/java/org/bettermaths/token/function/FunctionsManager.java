package org.bettermaths.token.function;

import java.util.HashMap;
import java.util.Map;

public class FunctionsManager {

    private static boolean isInitialized = false;

    private static final Map<String, Function> functions = new HashMap<>();

    public static void init() {
        if (isInitialized) {
            throw new RuntimeException("Symbols already initialized");
        }
        isInitialized = true;

        add(new AbsoluteFunction());
        add(new MinimumFunction());
        add(new SumFunction());
    }

    public static Map<String, Function> all() {
        if (!isInitialized) {
            init();
        }

        return functions;
    }

    public static Function get(String symbol) {
        if (!isInitialized) {
            init();
        }

        return functions.get(symbol);
    }

    public static void add(Function function) {
        functions.put(function.getName(), function);
    }

    public static void remove(String name) {
        functions.remove(name);
    }
}

