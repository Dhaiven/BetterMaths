package org.bettermaths.token.function;

import org.bettermaths.result.primary.NumberResult;
import org.bettermaths.token.function.argument.Arguments;
import org.bettermaths.token.function.argument.RangeArgument;
import org.bettermaths.token.symbol.delimiter.Parentheses;

public class AbsoluteFunction extends Function {

    public AbsoluteFunction() {
        super("abs", new Parentheses(), new Arguments(
                new RangeArgument<>(NumberResult.class, 1)
        ));
    }

    @Override
    public NumberResult<?> onExecute(Params params) {
        NumberResult<?> result = params.get(0);
        return (NumberResult<?>) result.abs();
    }
}
