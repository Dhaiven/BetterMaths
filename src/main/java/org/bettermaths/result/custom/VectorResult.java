package org.bettermaths.result.custom;

import org.bettermaths.result.OperationRegistry;
import org.bettermaths.result.OperationalResult;
import org.bettermaths.result.ResultManager;
import org.bettermaths.result.primary.DoubleResult;
import org.bettermaths.result.primary.IntegerResult;
import org.bettermaths.result.primary.NumberResult;

import java.util.*;

public class VectorResult implements OperationalResult<OperationalResult<?>> {

    public static VectorResult from(final Object o) {
        if (o instanceof String stringObject) {
            stringObject = stringObject.trim();
            if (stringObject.startsWith("(") && stringObject.endsWith(")") && stringObject.contains(",")) {
                stringObject = stringObject.trim();
                stringObject = stringObject.replace(" ", "");
                stringObject = stringObject.substring(1, stringObject.length() - 1); // remove "(" and ")"

                List<NumberResult<?>> result = new ArrayList<>();
                for (String part : stringObject.split(",")) {
                    var partResult = ResultManager.get(part);
                    if (partResult instanceof NumberResult<?> numberResult) {
                        result.add(numberResult);
                    } else {
                        return null;
                    }
                }

                if (result.isEmpty()) {
                    return null;
                }

                return new VectorResult(result);
            }
        }

        return null;
    }

    public static void registerOperators() {
        // ADD
        OperationRegistry.registerAdd(VectorResult.class, VectorResult.class, (r1, r2) -> {
            List<NumberResult<?>> collectionResult = new ArrayList<>();
            for (int i = 0; i < r1.size(); i++) {
                collectionResult.add((NumberResult<?>) r1.getResult(i).add(r2.getResult(i)));
            }

            return new VectorResult(collectionResult);
        });

        // SUBTRACT
        OperationRegistry.registerSubtract(VectorResult.class, VectorResult.class, (r1, r2) -> {
            List<NumberResult<?>> collectionResult = new ArrayList<>();
            for (int i = 0; i < r1.size(); i++) {
                collectionResult.add((NumberResult<?>) r1.getResult(i).subtract(r2.getResult(i)));
            }

            return new VectorResult(collectionResult);
        });

        // MULTIPLY
        OperationRegistry.registerMultiply(VectorResult.class, VectorResult.class, (r1, r2) -> {
            List<NumberResult<?>> collectionResult = new ArrayList<>();
            for (int i = 0; i < r1.size(); i++) {
                collectionResult.add((NumberResult<?>) r1.getResult(i).pow(r2.getResult(i)));
            }

            return new VectorResult(collectionResult);
        });
        OperationRegistry.registerMultiply(VectorResult.class, IntegerResult.class, (r1, r2) -> {
            List<NumberResult<?>> collectionResult = new ArrayList<>();
            for (int i = 0; i < r1.size(); i++) {
                collectionResult.add((NumberResult<?>) r1.getResult(i).pow(r2));
            }

            return new VectorResult(collectionResult);
        });
        OperationRegistry.registerMultiply(IntegerResult.class, VectorResult.class, (r1, r2) -> {
            List<NumberResult<?>> collectionResult = new ArrayList<>();
            for (int i = 0; i < r2.size(); i++) {
                collectionResult.add((NumberResult<?>) r1.pow(r2.getResult(i)));
            }

            return new VectorResult(collectionResult);
        });
        OperationRegistry.registerMultiply(VectorResult.class, DoubleResult.class, (r1, r2) -> {
            List<NumberResult<?>> collectionResult = new ArrayList<>();
            for (int i = 0; i < r1.size(); i++) {
                collectionResult.add((NumberResult<?>) r1.getResult(i).pow(r2));
            }

            return new VectorResult(collectionResult);
        });
        OperationRegistry.registerMultiply(DoubleResult.class, VectorResult.class, (r1, r2) -> {
            List<NumberResult<?>> collectionResult = new ArrayList<>();
            for (int i = 0; i < r2.size(); i++) {
                collectionResult.add((NumberResult<?>) r1.pow(r2.getResult(i)));
            }

            return new VectorResult(collectionResult);
        });

        // DIVIDE
        OperationRegistry.registerDivision(VectorResult.class, VectorResult.class, (r1, r2) -> {
            List<NumberResult<?>> collectionResult = new ArrayList<>();
            for (int i = 0; i < r1.size(); i++) {
                collectionResult.add((NumberResult<?>) r1.getResult(i).div(r2.getResult(i)));
            }

            return new VectorResult(collectionResult);
        });
    }

    private final List<NumberResult<?>> collection;

    public VectorResult(Collection<NumberResult<?>> results) {
        this.collection = (List<NumberResult<?>>) results;
    }

    public VectorResult(NumberResult<?> ...results) {
        this.collection = List.of(results);
    }

    @Override
    public VectorResult invert() {
        List<NumberResult<?>> collectionResult = new ArrayList<>();
        for (NumberResult<?> numberResult : this.collection) {
            collectionResult.add((NumberResult<?>) numberResult.invert());
        }

        return new VectorResult(collectionResult);
    }

    public int size() {
        return this.collection.size();
    }

    @Override
    public VectorResult get() {
        return this;
    }

    public NumberResult<?> getResult(int index) {
        return collection.get(index);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof VectorResult other)) return false;
        if (this.size() != other.size()) return false;
        for (int i = 0; i < this.size(); i++) {
            if (!Objects.equals(this.getResult(i), other.getResult(i))) {
                return false;
            }
        }

        return true;
    }

    @Override
    public int hashCode() {
        return Objects.hash(collection);
    }

    @Override
    public String toString() {
        StringJoiner joiner = new StringJoiner(", ", "(", ")");
        for (NumberResult<?> numberResult : collection) {
            joiner.add(numberResult.toString());
        }
        return joiner.toString();
    }
}
