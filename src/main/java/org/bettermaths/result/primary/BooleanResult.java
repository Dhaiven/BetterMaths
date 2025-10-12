package org.bettermaths.result.primary;

import org.bettermaths.result.Result;

import java.util.Objects;

public class BooleanResult extends Number implements Result<Boolean> {

    public static final BooleanResult TRUE = new BooleanResult(true);
    public static final BooleanResult FALSE = new BooleanResult(false);

    public static BooleanResult from(final Object o) {
        if (o instanceof Boolean booleanObject) {
            return booleanObject ? TRUE : FALSE;
        } else if (o instanceof String stringObject) {
            if ("true".equalsIgnoreCase(stringObject)) {
                return TRUE;
            } else if ("false".equalsIgnoreCase(stringObject)) {
                return FALSE;
            }
        }

        return null;
    }

    private final Boolean number;

    private BooleanResult(boolean number) {
        this.number = number;
    }

    public BooleanResult and(BooleanResult result) {
        return new BooleanResult(number && result.get());
    }

    public BooleanResult or(BooleanResult result) {
        return new BooleanResult(number || result.get());
    }

    public BooleanResult xor(BooleanResult result) {
        return new BooleanResult(number ^ result.get());
    }

    public Boolean get() {
        return number;
    }

    @Override
    public int intValue() {
        return number ? 1 : 0;
    }

    @Override
    public long longValue() {
        return intValue();
    }

    @Override
    public float floatValue() {
        return intValue();
    }

    @Override
    public double doubleValue() {
        return intValue();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof BooleanResult other)) return false;
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
