package org.bettermaths.result.primary;

import org.apache.commons.lang3.math.Fraction;
import org.bettermaths.result.*;

import java.util.Objects;

public class DoubleResult extends NumberResult<Double> {

    public static DoubleResult from(final Object o) {
        if (o instanceof Double doubleObject) {
            return new DoubleResult(doubleObject);
        } else if (o instanceof String stringObject) {
            // On fait ça car Double.valueOf marche quand meme s'il y a une espace au début
            if (!stringObject.equals(stringObject.trim())) {
                return null;
            }

            try {
                // Si c'est un int, on return null pour double
                Integer.valueOf(stringObject);
                return null;
            } catch (NumberFormatException _) {
                try {
                    return new DoubleResult(Double.valueOf(stringObject));
                } catch (NumberFormatException _) { }
            }
        } else if (o instanceof Fraction fractionObject) {
            return new DoubleResult(fractionObject);
        }

        return null;
    }

    public static void registerOperators() {
        //ADD
        OperationRegistry.registerAdd(DoubleResult.class, DoubleResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() + r2.get());
        });
        OperationRegistry.registerAdd(DoubleResult.class, IntegerResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() + r2.get());
        });
        OperationRegistry.registerAdd(IntegerResult.class, DoubleResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() + r2.get());
        });

        //SUB
        OperationRegistry.registerSubtract(DoubleResult.class, DoubleResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() - r2.get());
        });
        OperationRegistry.registerSubtract(DoubleResult.class, IntegerResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() - r2.get());
        });
        OperationRegistry.registerSubtract(IntegerResult.class, DoubleResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() - r2.get());
        });

        //MULTIPLY
        OperationRegistry.registerMultiply(DoubleResult.class, DoubleResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() * r2.get());
        });
        OperationRegistry.registerMultiply(DoubleResult.class, IntegerResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() * r2.get());
        });
        OperationRegistry.registerMultiply(IntegerResult.class, DoubleResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() * r2.get());
        });

        //DIVISION
        OperationRegistry.registerDivision(DoubleResult.class, DoubleResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() / r2.get());
        });
        OperationRegistry.registerDivision(DoubleResult.class, IntegerResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() / r2.get());
        });
        OperationRegistry.registerDivision(IntegerResult.class, DoubleResult.class, (r1, r2) -> {
            return ResultManager.get(r1.get() / r2.get());
        });

        //EQUIVALENT
        OperationRegistry.registerEquivalent(DoubleResult.class, DoubleResult.class, (r1, r2) -> {
            return Objects.equals(r1.get(), r2.get()) ? BooleanResult.TRUE : BooleanResult.FALSE;
        });
        OperationRegistry.registerEquivalent(DoubleResult.class, IntegerResult.class, (r1, r2) -> {
            return Objects.equals(r1.get(), r2.doubleValue()) ? BooleanResult.TRUE : BooleanResult.FALSE;
        });
        OperationRegistry.registerEquivalent(IntegerResult.class, DoubleResult.class, (r1, r2) -> {
            return Objects.equals(r1.doubleValue(), r2.get()) ? BooleanResult.TRUE : BooleanResult.FALSE;
        });

        //COMPARE
        OperationRegistry.registerCompare(DoubleResult.class, DoubleResult.class, (r1, r2) -> {
            double otherValue = r2.doubleValue();
            if (otherValue < r1.doubleValue()) {
                return new IntegerResult(1);
            } else if (otherValue > r1.doubleValue()) {
                return new IntegerResult(-1);
            }

            return new IntegerResult(0);
        });
        OperationRegistry.registerCompare(DoubleResult.class, IntegerResult.class, (r1, r2) -> {
            double otherValue = r2.doubleValue();
            if (otherValue < r1.doubleValue()) {
                return new IntegerResult(1);
            } else if (otherValue > r1.doubleValue()) {
                return new IntegerResult(-1);
            }

            return new IntegerResult(0);
        });
        OperationRegistry.registerCompare(IntegerResult.class, DoubleResult.class, (r1, r2) -> {
            double otherValue = r2.doubleValue();
            if (otherValue < r1.doubleValue()) {
                return new IntegerResult(1);
            } else if (otherValue > r1.doubleValue()) {
                return new IntegerResult(-1);
            }

            return new IntegerResult(0);
        });
    }

    private final int numerator;
    private final int denominator;

    private final Fraction number;

    public DoubleResult(Double number) {
        this(Fraction.getFraction(number));
    }

    public DoubleResult(Fraction number) {
        this.numerator = number.getNumerator();
        this.denominator = number.getDenominator();
        this.number = number;
    }

    public DoubleResult(int numerator, int denominator) {
        this.numerator = numerator;
        this.denominator = denominator;
        this.number = Fraction.getReducedFraction(numerator, denominator);
    }

    @Override
    public boolean isPositive() {
        return (number.getNumerator() >= 0 && number.getDenominator() > 0) || (number.getNumerator() < 0 && number.getDenominator() < 0);
    }

    @Override
    public DoubleResult invert() {
        return new DoubleResult(-numerator, denominator);
    }

    public Fraction getFraction() {
        return number;
    }

    public Double get() {
        return number.doubleValue();
    }

    public int getNumerator() {
        return numerator;
    }

    public int getDenominator() {
        return denominator;
    }

    public Integer round() {
        return Math.round(floatValue());
    }

    @Override
    public int intValue() {
        return number.intValue();
    }

    @Override
    public long longValue() {
        return number.longValue();
    }

    @Override
    public float floatValue() {
        return number.floatValue();
    }

    @Override
    public double doubleValue() {
        return number.doubleValue();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof DoubleResult other)) return false;
        return Objects.equals(get(), other.get());
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
