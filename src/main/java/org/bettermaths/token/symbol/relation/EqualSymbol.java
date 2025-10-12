package org.bettermaths.token.symbol.relation;

import org.bettermaths.result.Result;
import org.bettermaths.token.symbol.Identifier;

import java.util.Objects;

public class EqualSymbol extends RelationSymbol<Result<?>> {

    public EqualSymbol() {
        super(new Identifier("="), 0, Objects::equals);
    }
}