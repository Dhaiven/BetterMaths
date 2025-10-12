package org.bettermaths.token.function;

import org.bettermaths.token.function.argument.Arguments;
import org.bettermaths.token.function.argument.InfiniteArgument;
import org.bettermaths.token.function.argument.RangeArgument;
import org.bettermaths.result.ComparableResult;
import org.bettermaths.token.symbol.delimiter.Parentheses;

public class MinimumFunction extends Function {

    public MinimumFunction() {
        super("min", new Parentheses(), new Arguments(
                new RangeArgument<>(ComparableResult.class, 2),
                new InfiniteArgument<>(ComparableResult.class, 2, true)
        ));
    }

    @Override
    public ComparableResult<?> onExecute(Params params) {
        ComparableResult<?> result = params.get(0);
        for (int i = 1; i < params.size(); i++) {
            if (result.isGreaterThan(params.get(i))) {
                result = params.get(i);
            }
        }

        return result;
    }
}
