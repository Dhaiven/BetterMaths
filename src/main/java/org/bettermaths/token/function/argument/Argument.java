package org.bettermaths.token.function.argument;

import org.bettermaths.result.Result;

public abstract class Argument<T extends Result<?>> {

    protected final Class<T> type;
    protected final boolean optional;

    public Argument(Class<T> type, boolean optional) {
        this.type = type;
        this.optional = optional;
    }

    abstract boolean canResolve(int pos);

    abstract int startAt();
    abstract int endAt();

    public boolean isOptional() {
        return optional;
    }

    public boolean isSameType(Result<?> other) {
        return this.type.isAssignableFrom(other.getClass());
    }
}
