package org.bettermaths.result;

import org.bettermaths.result.custom.ErrorResult;
import org.bettermaths.result.custom.UpletResult;
import org.bettermaths.result.custom.VectorResult;
import org.bettermaths.result.primary.*;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;

public class ResultManager {

    private static boolean isInitialized = false;

    private static final List<Function<Object, Result<?>>> results = new ArrayList<>();

    private static void init() {
        if (isInitialized) {
            throw new RuntimeException("ResultManager already initialized");
        }
        isInitialized = true;

        register(VectorResult::from, VectorResult::registerOperators);
        register(UpletResult::from);

        register(BooleanResult::from);
        register(IntegerResult::from, IntegerResult::registerOperators);
        register(DoubleResult::from, DoubleResult::registerOperators);
    }

    public static void register(Function<Object, Result<?>> function) {
        register(function, null);
    }

    public static void register(Function<Object, Result<?>> function, Runnable registerOperators) {
        results.add(function);
        if (registerOperators != null) {
            registerOperators.run();
        }
    }

    public static Result<?> get(Object object) {
        return get(object, Result.class);
    }

    public static <T extends Result<?>> T get(Object object, Class<T> type) {
        if (!isInitialized) {
            init();
        }

        for (var function : results) {
            var result = function.apply(object);
            if (result != null) {
                try {
                    return type.cast(result);
                } catch (ClassCastException _) {}
            }
        }

        return type.cast(ErrorResult.ERROR);
    }
}
