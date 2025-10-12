package org.bettermaths.token.function.argument;

import org.bettermaths.result.Result;

public class InfiniteArgument<T extends Result<?>> extends Argument<T> {

    private final int startAt;

    public InfiniteArgument(Class<T> type) {
        this(type, false);
    }

    public InfiniteArgument(Class<T> type, boolean optional) {
        this(type, 0, optional);
    }

    public InfiniteArgument(Class<T> type, int startAt) {
        this(type, startAt, false);
    }

    public InfiniteArgument(Class<T> type, int startAt, boolean optional) {
        super(type, optional);
        this.startAt = startAt;
    }

    @Override
    int startAt() {
        return startAt;
    }

    @Override
    int endAt() {
        return Integer.MAX_VALUE;
    }

    @Override
    boolean canResolve(int pos) {
        return pos >= startAt;
    }
}
