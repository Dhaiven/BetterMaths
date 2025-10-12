package org.bettermaths.token.function.argument;

import org.bettermaths.result.Result;

public class RangeArgument<T extends Result<?>> extends Argument<T> {

    private final int start;
    private final int end;
    private final int step;

    public RangeArgument(Class<T> type, int end) {
        this(type, end, false);
    }

    public RangeArgument(Class<T> type, int end, boolean optional) {
        this(type, 0, end, optional);
    }

    public RangeArgument(Class<T> type, int start, int end) {
        this(type, start, end, false);
    }

    public RangeArgument(Class<T> type, int start, int end, int step) {
        this(type, start, end, step, false);
    }

    public RangeArgument(Class<T> type, int start, int end, boolean optional) {
        this(type, start, end, 1, optional);
    }

    /**
     * @param start (inclusive)
     * @param end (exclusive)
     */
    public RangeArgument(Class<T> type, int start, int end, int step, boolean optional) {
        super(type, optional);
        this.start = start;
        this.end = end;
        this.step = step;
    }

    @Override
    int startAt() {
        return start;
    }

    @Override
    int endAt() {
        return end;
    }

    @Override
    boolean canResolve(int pos) {
        if (pos >= start && pos < end) {
            return pos % step == start;
        }

        return false;
    }
}