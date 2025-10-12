package org.bettermaths.result;

public interface ComparableResult<T> extends Result<T>, Comparable<ComparableResult<?>> {

    default boolean isGreaterThan(ComparableResult<?> result) {
        return compareTo(result) > 0;
    }

    default boolean isGreaterOrEqualThan(ComparableResult<?> result) {
        return compareTo(result) >= 0;
    }

    default boolean isSmallerThan(ComparableResult<?> result) {
        return compareTo(result) < 0;
    }

    default boolean isSmallerOrEqualThan(ComparableResult<?> result) {
        return compareTo(result) <= 0;
    }

    @Override
    default int compareTo(ComparableResult<?> o) {
        return OperationRegistry.compare(this, o);
    }
}
