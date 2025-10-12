package org.bettermaths.token.symbol.relation;

import org.bettermaths.result.ComparableResult;
import org.bettermaths.token.symbol.Identifier;

public class LessThanSymbol extends RelationSymbol<ComparableResult<?>> {

    public LessThanSymbol() {
        super(new Identifier("<"), 5, ComparableResult::isLessThan);
    }
}