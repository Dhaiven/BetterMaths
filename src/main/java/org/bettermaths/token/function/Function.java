package org.bettermaths.token.function;

import org.bettermaths.token.function.argument.Arguments;
import org.bettermaths.result.Result;
import org.bettermaths.token.symbol.delimiter.Delimiter;
import org.bettermaths.token.symbol.Identifier;
import org.bettermaths.token.Token;

public abstract class Function implements Token {

    private final String name;
    private final Delimiter delimiter;
    private final Identifier separator;
    private final Arguments arguments;

    public Function(String name, Delimiter delimiter, Arguments arguments) {
        this(name, delimiter, new Identifier(","), arguments);
    }

    public Function(String name, Delimiter delimiter, Identifier separator, Arguments arguments) {
        this.name = name;
        this.delimiter = delimiter;
        this.separator = separator;
        this.arguments = arguments;
    }

    public String getName() {
        return name;
    }

    public Delimiter getDelimiter() {
        return delimiter;
    }

    public Identifier getSeparator() {
        return separator;
    }

    public int getMinimumNumberOfArguments() {
        return arguments.getMinimumNumber();
    }

    public int getMaximumNumberOfArguments() {
        return arguments.getMaximumNumber();
    }

    public boolean canExecute(Params params) {
        if (getMinimumNumberOfArguments() > params.size()) return false;
        if (params.size() > getMaximumNumberOfArguments()) return false;

        for (int i = 0; i < params.size(); i++) {
            if (!arguments.matches(i, params.get(i))) {
                return false;
            }
        }

        return true;
    }

    public abstract Result<?> onExecute(Params params);
}
