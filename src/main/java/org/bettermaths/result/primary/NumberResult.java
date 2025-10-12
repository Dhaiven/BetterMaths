package org.bettermaths.result.primary;

import org.bettermaths.result.ComparableResult;
import org.bettermaths.result.OperationalResult;

public abstract class NumberResult<N extends Number> extends Number
    implements OperationalResult<N>, ComparableResult<N> {

    abstract public boolean isPositive();

    public OperationalResult<N> abs() {
        return isPositive() ? this : invert();
    }

    abstract public Integer round();
}
