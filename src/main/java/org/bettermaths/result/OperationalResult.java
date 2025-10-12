package org.bettermaths.result;

public interface OperationalResult<T> extends Result<T> {

    default OperationalResult<?> add(OperationalResult<?> result) {
        return (OperationalResult<?>) OperationRegistry.execute(OperationRegistry.ADD_KEY, this, result);
    }

    default OperationalResult<?> subtract(OperationalResult<?> result) {
        return (OperationalResult<?>) OperationRegistry.execute(OperationRegistry.SUBTRACT_KEY, this, result);
    }

    default OperationalResult<?> pow(OperationalResult<?> result) {
        return (OperationalResult<?>) OperationRegistry.execute(OperationRegistry.MULTIPLY_KEY, this, result);
    }

    default OperationalResult<?> div(OperationalResult<?> result) {
        return (OperationalResult<?>) OperationRegistry.execute(OperationRegistry.DIVIDE_KEY, this, result);
    }

    OperationalResult<T> invert();
}
