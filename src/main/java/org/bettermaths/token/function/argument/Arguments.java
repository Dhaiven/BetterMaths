package org.bettermaths.token.function.argument;

import org.bettermaths.result.Result;

public class Arguments {

    private final Argument<?>[] args;

    private int minimalNumberOfArguments = -1;
    private int maximalNumberOfArguments = -1;

    public Arguments(Argument<?> ...args) {
        this.args = args;

        for (var arg : args) {
            if (!arg.isOptional()) {
                if (arg.endAt() > minimalNumberOfArguments) {
                    minimalNumberOfArguments = arg.endAt();
                }
            }

            if (arg.endAt() > maximalNumberOfArguments) {
                maximalNumberOfArguments = arg.endAt();
            }

            if (!arg.isOptional()) {
                if (arg.startAt() > minimalNumberOfArguments) {
                    minimalNumberOfArguments = arg.startAt();
                }
            }
        }
    }

    public Argument<?>[] getArguments() {
        return args;
    }

    public int getMinimumNumber() {
        return minimalNumberOfArguments;
    }

    public int getMaximumNumber() {
        return maximalNumberOfArguments;
    }

    public boolean matches(int pos, Result<?> value) {
        for (Argument<?> arg : args) {
            if (arg.canResolve(pos)) {
                return arg.isSameType(value);
            }
        }

        return false;
    }
}
