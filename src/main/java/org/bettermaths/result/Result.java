package org.bettermaths.result;

import org.bettermaths.token.Token;

public interface Result<T> extends java.io.Serializable, Token {
    T get();

    default boolean equivalent(Result<?> other) {
        return OperationRegistry.equivalent(this, other);
    }
}
