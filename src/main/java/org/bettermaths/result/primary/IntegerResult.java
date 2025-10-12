package org.bettermaths.result.primary;

import org.apache.commons.lang3.math.Fraction;
import org.bettermaths.result.*;

import java.util.Objects;

public class IntegerResult extends NumberResult<Integer> {

    public static IntegerResult from(final Object o) {
        if (o instanceof Integer integerObject) {
            return new IntegerResult(integerObject);
        } else if (o instanceof Double doubleObject) {
            if (isInteger(doubleObject)) {
                return new IntegerResult(doubleObject.intValue());
            }
        } else if (o instanceof String stringObject) {
            try {
                return new IntegerResult(Integer.parseInt(stringObject));
            } catch (NumberFormatException _) {
                var split = stringObject.split("\\.");
                if (split.length == 2) {
                    try {
                        if (Integer.parseInt(split[1]) == 0) {
                            return new IntegerResult(Integer.parseInt(split[0]));
                        }
                    } catch (NumberFormatException _) {}
                }
            }
        } else if (o instanceof Fraction fractionObject) {
            if (fractionObject.getNumerator() == 0) {
                return new IntegerResult(0);
            } else if (fractionObject.getDenominator() == 1) {
                return new IntegerResult(fractionObject.getNumerator());
            }
        }

        return null;
    }

    private static boolean isInteger(Double variable) {
        return variable.equals(Math.floor(variable)) &&
                !Double.isInfinite(variable) &&
                !Double.isNaN(variable) &&
                variable <= Integer.MAX_VALUE &&
                variable >= Integer.MIN_VALUE;
    }

    public static void registerOperators() {
        OperationRegistry.registerAdd(IntegerResult.class, IntegerResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() + r2.get());
        });
        OperationRegistry.registerSubtract(IntegerResult.class, IntegerResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() - r2.get());
        });
        OperationRegistry.registerMultiply(IntegerResult.class, IntegerResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() * r2.get());
        });
        OperationRegistry.registerDivision(IntegerResult.class, IntegerResult.class, (r1, r2) -> {
            return ResultManager.get((double) r1.get() / r2.get());
        });

        OperationRegistry.registerEquivalent(IntegerResult.class, IntegerResult.class, (r1, r2) -> {
            return Objects.equals(r1.get(), r2.get()) ? BooleanResult.TRUE : BooleanResult.FALSE;
        });

        OperationRegistry.registerCompare(IntegerResult.class, IntegerResult.class, (r1, r2) -> {
            double otherValue = r2.get();
            if (otherValue < r1.get()) {
                return new IntegerResult(1);
            } else if (otherValue > r1.get()) {
                return new IntegerResult(-1);
            }

            return new IntegerResult(0);
        });
    }

    private final Integer number;

    public IntegerResult(int number) {
        this.number = number;
    }

    @Override
    public boolean isPositive() {
        return number >= 0;
    }

    @Override
    public IntegerResult invert() {
        return new IntegerResult(-number);
    }

    public Integer get() {
        return number;
    }

    public Integer round() {
        return number;
    }

    @Override
    public int intValue() {
        return number;
    }

    @Override
    public long longValue() {
        return (long) number;
    }

    @Override
    public float floatValue() {
        return (float) number;
    }

    @Override
    public double doubleValue() {
        return (double) number;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof IntegerResult other)) return false;
        return Objects.equals(number, other.get());
    }

    @Override
    public int hashCode() {
        return Objects.hash(number);
    }

    @Override
    public String toString() {
        return number.toString();
    }
}
