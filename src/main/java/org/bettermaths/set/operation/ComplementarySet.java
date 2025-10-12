package org.bettermaths.set.operation;

import org.bettermaths.result.Result;
import org.bettermaths.set.Set;

public class ComplementarySet implements Set {

    protected final Set baseSet;

    public ComplementarySet(Set baseSet) {
        this.baseSet = baseSet;
    }

    public Set getBaseSet() {
        return baseSet;
    }

    @Override
    public boolean contains(Set other) {
        return other instanceof ComplementarySet complementarySet && baseSet.contains(complementarySet.getBaseSet());
    }

    @Override
    public boolean strictContains(Set other) {
        return other instanceof ComplementarySet complementarySet && baseSet.strictContains(complementarySet.getBaseSet());
    }

    @Override
    public boolean belongs(Result<?> other) {
        return !baseSet.belongs(other);
    }
}
