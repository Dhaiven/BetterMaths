package org.bettermaths.token.symbol;

import org.bettermaths.token.function.Function;
import org.bettermaths.token.function.Params;
import org.bettermaths.result.Result;
import org.bettermaths.result.custom.ErrorResult;

public class AliasFunctionSymbol extends Symbol {

    private final Function function;

    public AliasFunctionSymbol(Identifier identifier, int priority, boolean supportUnary, Function function) {
        super(identifier, priority, supportUnary);
        this.function = function;
    }

    @Override
    public Result<?> apply(Params params) {
        if (!function.canExecute(params)) {
            if (params.size() > 0) {
                return params.get(0);
            }
            return ErrorResult.ERROR;
        }

        return function.onExecute(params);
    }
}
