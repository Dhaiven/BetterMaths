package org.bettermaths.set.type;

import org.bettermaths.result.Result;
import org.bettermaths.result.primary.IntegerResult;
import org.bettermaths.set.Set;

public class NaturalSet implements Set {

    @Override
    public boolean contains(Set other) {
        return other instanceof NaturalSet;
    }

    @Override
    public boolean strictContains(Set other) {
        return other instanceof NaturalSet && !this.equals(other);
    }

    @Override
    public boolean belongs(Result<?> other) {
        return other instanceof IntegerResult integerResult && integerResult.get() >= 0;
    }
}
