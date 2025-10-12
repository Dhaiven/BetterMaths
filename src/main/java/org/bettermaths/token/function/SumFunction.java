package org.bettermaths.token.function;

import org.bettermaths.token.function.argument.Arguments;
import org.bettermaths.token.function.argument.InfiniteArgument;
import org.bettermaths.token.function.argument.RangeArgument;
import org.bettermaths.result.OperationalResult;
import org.bettermaths.token.symbol.delimiter.Parentheses;

public class SumFunction extends Function {

    public SumFunction() {
        super("sum", new Parentheses(), new Arguments(
                new RangeArgument<>(OperationalResult.class, 2),
                new InfiniteArgument<>(OperationalResult.class, 2, true)
        ));
    }

    @Override
    public OperationalResult<?> onExecute(Params params) {
        OperationalResult<?> result = params.get(0);
        for (int i = 1; i < params.size(); i++) {
            result = result.add(params.get(i));
        }

        return result;
    }
}
