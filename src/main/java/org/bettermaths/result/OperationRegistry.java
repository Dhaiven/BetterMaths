package org.bettermaths.result;

import org.bettermaths.result.primary.BooleanResult;
import org.bettermaths.result.primary.IntegerResult;

import java.util.*;
import java.util.function.BiFunction;

public class OperationRegistry {

    public static final String ADD_KEY = "add";
    public static final String SUBTRACT_KEY = "subtract";
    public static final String MULTIPLY_KEY = "multiply";
    public static final String DIVIDE_KEY = "divide";

    public static final String COMPARE_KEY = "compare";
    public static final String EQUIVALENT_KEY = "equivalent";

    // Map pour chaque opération (+, -, *, /, pow) -> map des couples de classes -> fonction
    private static final Map<String, Map<ClassPair, BiFunction<? extends Result<?>, ? extends Result<?>, Result<?>>>> registry = new HashMap<>();

    public static <T extends Result<?>, E extends Result<?>> void registerAdd(Class<T> a,
                                   Class<? extends E> b,
                                   BiFunction<T, E, Result<?>> function) {
        register(ADD_KEY, a, b, function);
    }

    public static <T extends Result<?>, E extends Result<?>> void registerSubtract(
            Class<T> a,
            Class<? extends E> b,
            BiFunction<T, E, Result<?>> function
    ) {
        register(SUBTRACT_KEY, a, b, function);
    }

    public static <T extends Result<?>, E extends Result<?>> void registerMultiply(
            Class<T> a,
            Class<? extends E> b,
            BiFunction<T, E, Result<?>> function
    ) {
        register(MULTIPLY_KEY, a, b, function);
    }

    public static <T extends Result<?>, E extends Result<?>> void registerDivision(
            Class<T> a,
            Class<? extends E> b,
            BiFunction<T, E, Result<?>> function
    ) {
        register(DIVIDE_KEY, a, b, function);
    }

    public static <T extends Result<?>, E extends Result<?>> void registerCompare(
            Class<T> a,
            Class<? extends E> b,
            BiFunction<T, E, Result<?>> function
    ) {
        register(COMPARE_KEY, a, b, function);
    }

    public static <T extends Result<?>, E extends Result<?>> void registerEquivalent(
            Class<T> a,
            Class<? extends E> b,
            BiFunction<T, E, Result<?>> function
    ) {
        register(EQUIVALENT_KEY, a, b, function);
    }

    private static <T extends Result<?>, E extends Result<?>> void register(String op, Class<T> a,
                                                                            Class<? extends E> b,
                                                                            BiFunction<T, E, Result<?>> function) {
        registry.computeIfAbsent(op, _ -> new HashMap<>())
                .put(new ClassPair(a, b), function);
    }

    public static <T extends Result<?>, E extends Result<?>> Result<?> execute(String op, T a, E b) {
        var map = registry.get(op);
        if (map == null) throw new UnsupportedOperationException("Operation inconnue: " + op);

        BiFunction<T, E, ? extends Result<?>> func = (BiFunction<T, E, ? extends Result<?>>) map.get(new ClassPair(a.getClass(), b.getClass()));
        if (func != null) return func.apply(a, b);

        throw new UnsupportedOperationException("Operation " + op + " non définie pour " + a.getClass() + " et " + b.getClass());
    }

    public static <T extends Result<?>, E extends Result<?>> int compare(T a, E b) {
        var map = registry.get(COMPARE_KEY);
        BiFunction<T, E, ? extends Result<?>> func = (BiFunction<T, E, ? extends Result<?>>) map.get(new ClassPair(a.getClass(), b.getClass()));
        if (func != null) {
            return ((IntegerResult) func.apply(a, b)).get();
        }

        throw new UnsupportedOperationException("Operation " + COMPARE_KEY + " non définie pour " + a.getClass() + " et " + b.getClass());
    }

    public static <T extends Result<?>, E extends Result<?>> boolean equivalent(T a, E b) {
        var map = registry.get(EQUIVALENT_KEY);
        BiFunction<T, E, ? extends Result<?>> func = (BiFunction<T, E, ? extends Result<?>>) map.get(new ClassPair(a.getClass(), b.getClass()));
        if (func != null) {
            return ((BooleanResult) func.apply(a, b)).get();
        }

        return false;
    }

    private record ClassPair(Class<?> a, Class<?> b) {

        @Override
        public boolean equals(Object o) {
            if (!(o instanceof ClassPair(Class<?> a1, Class<?> b1))) return false;
            return a.equals(a1) && b.equals(b1);
        }
    }
}
